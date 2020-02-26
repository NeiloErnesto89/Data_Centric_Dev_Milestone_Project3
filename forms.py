from flask_wtf import FlaskForm # , RecaptchaField
from wtforms import StringField, TextField, SubmitField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length # , ValidationError, Optional


""" taken and adapted from  https://hackersandslackers.com/flask-wtforms-forms/ """ 

"""Comment form"""

class CommentForm(FlaskForm):
    
    
    book_hook = StringField('Note Header', validators=[DataRequired("Enter the header"), Length(max=15)])
    user_comments = TextAreaField ('Your Comments', validators=[DataRequired("Enter your internal notes"), Length(min=4), Length(max=50)])
    submit = SubmitField('Submit')   
    

"""

#Login Form

class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired("Please enter your Username")])
    user_password = PasswordField('Password', validators=[DataRequired("Please enter your Password")])
    submit = SubmitField('Submit')
    
"""