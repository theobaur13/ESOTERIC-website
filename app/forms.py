from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ClaimForm(FlaskForm):
    claim = StringField(render_kw={"placeholder": "Enter a claim"})
    submit = SubmitField("Submit")