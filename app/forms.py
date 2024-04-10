from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ClaimForm(FlaskForm):
    claim = StringField("Enter a claim:")
    submit = SubmitField("Submit")