from flask_wtf import FlaskForm # , RecaptchaField
from wtforms import StringField, TextField, SubmitField, TextAreaField #, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length # , ValidationError, Optional


""" taken from  https://hackersandslackers.com/flask-wtforms-forms/ """ 

class CommentForm(FlaskForm):
    
    """Review form"""
    
    book_title = StringField('Book Title', validators=[DataRequired("Enter the book title")])
    user_comments = TextAreaField ('Your Comments', validators=[DataRequired("Enter your comments"), Length(min=4)])
    submit = SubmitField('Submit')   
    
   