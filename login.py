"""
import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    #Login form to access writing and settings pages

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class User():

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
        
    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("mentors"))
        flash("Wrong username or password", category='error')
    return render_template('login.html', title='login', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@lm.user_loader
def load_user(username):
    u = mongo.db.users.find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
    
"""