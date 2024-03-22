from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, Optional
import bleach
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


class TextAnalysisForm(FlaskForm):
    class Meta:
        csrf = False  # Disable CSRF for this form
    text = StringField('Text', validators=[DataRequired(), Length(min=1, max=1000)])


class StyleSuggestionsForm(FlaskForm):
    class Meta:
        csrf = False  # Disable CSRF for this form
    text = StringField('Text', validators=[DataRequired(), Length(min=1, max=1000)])
    profession = StringField('Profession', validators=[Optional(), Length(max=50)])
    target_audience = StringField('Target Audience', validators=[Optional(), Length(max=50)])


# Home endpoint
@app.route('/')
def home():
    return "Welcome to the SuperClone AI!"


# analyze_text endpoint
# sample command -
# curl -X POST http://127.0.0.1:5000/analyze_text -d "text=Hello World" -H "Content-Type: application/x-www-form-urlencoded"
# Data sanitization - https://www.educative.io/answers/how-to-sanitize-user-input-in-python
@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    form = TextAnalysisForm()
    if form.validate_on_submit(): # data validation check
        text = bleach.clean(form.text.data) # data sanitization
        # Process the text and return the result
        return {'analysis': '...', 'text': text}
    return {'error': 'Invalid input'}, 400


# suggest_style endpoint
@app.route('/suggest_style', methods=['POST'])
def suggest_style():
    form = StyleSuggestionsForm()
    if form.validate_on_submit(): # data validation check
        text = bleach.clean(form.text.data) # data sanitization
        profession = bleach.clean(form.profession.data) # data sanitization
        target_audience = bleach.clean(form.target_audience.data) # data sanitization
        # Process the data and return suggestions
        return {'suggestions': '...', 'profession': profession, 'target audience': target_audience,
                'text': text}
    return {'error': 'Invalid input'}, 400


if __name__ == '__main__':
    app.run(debug=True)
