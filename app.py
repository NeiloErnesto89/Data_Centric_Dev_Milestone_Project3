import os
from os import path
if path.exists("env.py"):
    import env
#from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#load_dotenv()

app = Flask(__name__) #dunder 
#app.config['MONGODB_NAME']= os.environ.get('MONGODB_NAME') 
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/') #proof of concept
@app.route('/get_reviews')
def get_reviews():
    return render_template("book_review.html",
    books=mongo.db.books.find()) 
    # supply collection here with find method to return book collection from mdb
    
    
if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)