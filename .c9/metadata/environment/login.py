{"filter":false,"title":"login.py","tooltip":"/login.py","undoManager":{"mark":20,"position":20,"stack":[[{"start":{"row":0,"column":0},"end":{"row":51,"column":25},"action":"insert","lines":["class LoginForm(Form):","    \"\"\"Login form to access writing and settings pages\"\"\"","​","    username = StringField('Username', validators=[DataRequired()])","    password = PasswordField('Password', validators=[DataRequired()])","​","​","class User():","​","    def __init__(self, username):","        self.username = username","​","    def is_authenticated(self):","        return True","​","    def is_active(self):","        return True","​","    def is_anonymous(self):","        return False","​","    def get_id(self):","        return self.username","        ","    @staticmethod","    def validate_login(password_hash, password):","        return check_password_hash(password_hash, password)","​","@app.route('/login', methods=['GET', 'POST'])","def login():","    form = LoginForm()","    if request.method == 'POST' and form.validate_on_submit():","        user = mongo.db.users.find_one({\"_id\": form.username.data})","        if user and User.validate_login(user['password'], form.password.data):","            user_obj = User(user['_id'])","            login_user(user_obj)","            flash(\"Logged in successfully\", category='success')","            return redirect(request.args.get(\"next\") or url_for(\"mentors\"))","        flash(\"Wrong username or password\", category='error')","    return render_template('login.html', title='login', form=form)","    ","@app.route('/logout')","def logout():","    logout_user()","    return redirect(url_for('login'))","    ","@lm.user_loader","def load_user(username):","    u = mongo.db.users.find_one({\"_id\": username})","    if not u:","        return None","    return User(u['_id'])"],"id":1}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["​"],"id":2},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":["​"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["​"],"id":3}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"remove","lines":["​"],"id":4}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["​"],"id":5}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["​"],"id":6}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"remove","lines":["​"],"id":7}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["​"],"id":8}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":1},"action":"remove","lines":["​"],"id":9}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for, flash","from flask_pymongo import PyMongo","from bson.objectid import ObjectId","from werkzeug.urls import url_parse","from werkzeug.security import generate_password_hash, check_password_hash","from flask_login import current_user, login_user, logout_user, login_required, LoginManager","from flask_wtf import Form","from wtforms import StringField, PasswordField","from wtforms.validators import DataRequired"],"id":12}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["\"\""],"id":14}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["\""],"id":15}],[{"start":{"row":63,"column":25},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":4},"end":{"row":65,"column":0},"action":"insert","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"remove","lines":["    "],"id":17}],[{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["\"\""],"id":18}],[{"start":{"row":65,"column":2},"end":{"row":65,"column":3},"action":"insert","lines":["\""],"id":19}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["\""],"id":20},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["\""]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["\""]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["#"],"id":21}],[{"start":{"row":13,"column":52},"end":{"row":13,"column":55},"action":"remove","lines":["\"\"\""],"id":22}]]},"ace":{"folds":[],"scrolltop":349.84375,"scrollleft":0,"selection":{"start":{"row":19,"column":0},"end":{"row":38,"column":59},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":18,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1581508925315,"hash":"e28e0134b54d5c3c055d7893194e29ee14e0988f"}