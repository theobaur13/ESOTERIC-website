import uuid
from app import app, evidence_retriever, progress_store
from flask import render_template, session, redirect, url_for, request, jsonify
from threading import Thread

from app.forms import ClaimForm
from app.models import Evidence, EvidenceWrapper, Sentence

@app.route("/", methods=["GET", "POST"])
def index():
    form = ClaimForm()
    if form.validate_on_submit():
        session["claim"] = form.claim.data
        return redirect(url_for("demo"))
    return render_template("index.html", form=form)

@app.route("/demo")
def demo():
    claim = session.get('claim', 'Not specified')
    task_id = str(uuid.uuid4())
    session["task_id"] = task_id
    Thread(target=background_task, args=(task_id, claim)).start()
    return render_template("demo.html", claim=claim, task_id=task_id)

@app.route("/progress/<task_id>")
def progress(task_id):
    return jsonify(progress_store.get(task_id, None))

def background_task(task_id, claim):
    evidence_retriever.flush_questions()
    evidence_wrapper = evidence_retriever.retrieve_evidence(claim, task_id)
    progress_store[task_id]["status"] = "completed"
    
    evidences = []
    for evidence in evidence_wrapper.get_evidences():
        evidence.merge_overlapping_sentences()
    
    evidence_wrapper.seperate_sort()
    for evidence in evidence_wrapper.get_evidences():
        evidence_dict = {
            "doc_id": evidence.doc_id,
            "doc_score": evidence.doc_score,
            "evidence_text": evidence.evidence_text,
            "sentences": []
        }
        for sentence in evidence.sentences:
            sentence_dict = {
                "sentence": sentence.sentence,
                "score": sentence.score,
                "start": sentence.start,
                "end": sentence.end
            }
            evidence_dict["sentences"].append(sentence_dict)
        evidences.append(evidence_dict)
    progress_store[task_id]["evidence"] = evidences