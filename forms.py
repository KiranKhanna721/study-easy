from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,TextAreaField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired

class VideoAnalysisForm(FlaskForm):
    input_text= TextAreaField('Input Text', validators=[DataRequired()])
    submit = SubmitField('Analyze')

    
class TextTopicModeling(FlaskForm):          
    input_text= TextAreaField('Input Text', validators=[DataRequired()])
    submit = SubmitField('Analyze') 
    
class SentimentModeling(FlaskForm):          
    input_text= TextAreaField('Input Text', validators=[DataRequired()])
    submit = SubmitField('Analyze') 
