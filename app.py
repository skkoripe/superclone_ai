from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, Optional
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
@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    form = TextAnalysisForm()
    if form.validate_on_submit():
        text = form.text.data
        # Process the text and return the result
        return {'analysis': '...', 'text': text}
    return {'error': 'Invalid input'}, 400


# suggest_style endpoint
@app.route('/suggest_style', methods=['POST'])
def suggest_style():
    form = StyleSuggestionsForm()
    if form.validate_on_submit():
        data = {
            'text': form.text.data,
            'profession': form.profession.data,
            'target_audience': form.target_audience.data
        }
        # Process the data and return suggestions
        return {'suggestions': '...', 'profession': form.profession.data, 'target audience': form.target_audience.data,
                'text': form.text.data}
    return {'error': 'Invalid input'}, 400


if __name__ == '__main__':
    app.run(debug=True)
