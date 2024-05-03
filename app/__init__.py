from flask import Flask
from dotenv import load_dotenv

import os

load_dotenv()

# Create the Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
progress_store = {}

# Specify parameters for evidence retrieval using environment variables
title_match_docs_limit = int(os.getenv("TITLE_MATCH_DOCS_LIMIT"))
text_match_search_db_limit = int(os.getenv("TEXT_MATCH_SEARCH_DB_LIMIT"))
title_match_search_threshold = float(os.getenv("TITLE_MATCH_SEARCH_THRESHOLD"))
answerability_threshold = float(os.getenv("ANSWERABILITY_THRESHOLD"))
reader_threshold = float(os.getenv("READER_THRESHOLD"))

# Load evidence retriever
from app.ESOTERIC.evidence_retrieval import EvidenceRetriever
evidence_retriever = EvidenceRetriever(
    title_match_docs_limit=title_match_docs_limit,
    text_match_search_db_limit=text_match_search_db_limit,
    title_match_search_threshold=title_match_search_threshold,
    answerability_threshold=answerability_threshold,
    reader_threshold=reader_threshold
)
print("App created")

from app import routes