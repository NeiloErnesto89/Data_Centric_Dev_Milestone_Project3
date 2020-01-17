import os
from os import path
if path.exists("env.py"):
    import env
#from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
#from flask_bcrypt import Bcrypt

#load_dotenv()

app = Flask(__name__) #dunder 
#app.config['MONGODB_NAME']= os.environ.get('MONGODB_NAME') 
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

#bcrypt = Bcrypt(app)

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return "you're logged in"
        
    return render_template('index.html')

@app.route('/get_reviews')
def get_reviews():
    return render_template("book_review.html",
    books=mongo.db.books.find()) 
    # supply collection here with find method to return book collection from mdb

"""
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':        
        users = mongo.db.users
        live_user = users.find_one({'name' : request.form['username']}) # from signup.html name=username
        
        if live_user is None:
            hashingpw = bcrypt.hashpw(request.form['passwd'], bcrypt.genSalt())
            users.insert({'name' : request.form['username'], password : hashingpw}) # stores hashed version of pw
            session['username'] = request.form['username']
            return redirect(url_for('index.html'))
            
        return 'User already exists in this dimension'
       
       #else POST is not true i.e. it's a GET
       
    return render_template('signup.html')
"""             

@app.route('/signup')
def signup():
    return ''
  
@app.route('/login')
def login():
    return ''
    
    
    
if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)