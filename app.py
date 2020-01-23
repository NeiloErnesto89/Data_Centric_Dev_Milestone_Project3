import os
from datetime import datetime
from os import path
if path.exists("env.py"):
    import env
#from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash  


app = Flask(__name__) #dunder 
#app.config['MONGODB_NAME']= os.environ.get('MONGODB_NAME') 
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)

# DB Collections

users_coll = mongo.db.users 
books_coll = mongo.db.books
removed_coll = mongo.db.removed_by

"""
@app.route('/')
@app.route('/<password>')
def index(password):
    
    #hashed_value = generate_password_hash(password)
    
    stored_password = 'pbkdf2:sha256:150000$X3UrcT74$cf9a77f6f16f839369159274a32b2d136aea48c94aab1dafcfd56c33cf025e79'
    
    result = check_password_hash(stored_password, password)
    
    return str(result) # boolean so need to return string  #hashed_value
    
"""

@app.route('/')
@app.route('/index')
def index():
    books = mongo.db.books
    return render_template('index.html')


@app.route('/get_reviews')
def get_reviews():
    return render_template("book_review.html",
    books=mongo.db.books.find()) 
    
    # supply collection here with find method to return book collection from mdb
 
@app.route('/review_page')
def review_page():
    return render_template("add_review.html")

@app.route('/add_review', methods=['POST'] )
def add_review():
    books=mongo.db.books
    books.insert_one({
        'book_title' : request.form.get('book_title'),
        'book_author' : request.form.get('book_author'),
        'category_name' : request.form.get('category_name'),
        'publish_date ' : request.form.get('publish_date '),
        'summary' : request.form.get('summary'),
        'stars' : request.form.get('book_author'),
        'added_by' : request.form.getlist('added_by'), #array with object ID added 
        'is_available' : request.form.get('is_available')
        })
    return redirect(url_for('get_reviews'))

        
"""

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        form = request.form.to_dict()
		   books_coll.insert_one(form)
            return redirect(url_for('get_reviews'))
    
    books=mongo.db.books
    books.insert_one({
        'book_title' : request.form.get('book_title').upper(),
        'book_author' : request.form.get('book_author').upper(),
        'category_name' : request.form.get('category_name').upper(),
        'publish_date ' : request.form.get('publish_date '),
        'summary' : request.form.get('summary'),
        'stars' : request.form.get('book_author'),
        'is_available' : request.form.get('is_available')
        })
        
       # 'added_by' :request.form.getlist('added_by'),
       
       books.insert_one(request.form.to_dict()) # convert form to dict for mdb
       return redirect(url_for('get_reviews'))
 
@app.route('/show_user/<username>')
def show_user():

@app.route('/insert_books/<book_id>', methods=['POST'])
def insert_book(book_id):
    books = mongo.db.books
    books.find_one_and_update( {'_id': ObjectId(books_id)}, {'$push': {'title': request.form.getlist('book_title') }} )
    return redirect(url_for('added_books'))
""" 

@app.route('/login', methods=['GET'])
def login():
    if 'user' in session:
        user_db = users_coll.find_one({"username" : session['user']})
        if user_db:
            flash("you're already logged in!")  
            return redirect(url_for('bio', user=user_db['username'])) #get_reviews formerly 
    else:
        return render_template('login.html')
        
        

@app.route('/user_login', methods=['POST'])
def user_login():
    form = request.form.to_dict()
    user_db = users_coll.find_one({"username" : form['username']})
    if user_db:
        if check_password_hash(user_db['password'], form['user_password']):
            session['user'] = form['username']
            if session['user'] == "admin":
                    return redirect(url_for('admin'))
            else:
                flash("you're already logged in!")
                return redirect(url_for('bio', user=user_db['username'])) #get_reviews formerly 
        else:
             flash("password or username is incorrect")
             return redirect(url_for('login'))
    else:
        flash("You gotta sign up !")
        return redirect(url_for('signup'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	
	if 'user' in session:
		flash("you're already signed in !!")
		return redirect(url_for('get_reviews'))
		
	if request.method == 'POST':
		form = request.form.to_dict()
		 
		if form['user_password'] == form['confirm_password']: # need to insert a popup saying 'confirm pw'
			
			user = users_coll.find_one({"username" : form['username']})
			if user:
				flash(f"{form['username']} already exists!")
				return redirect(url_for('signup'))
			
			else:				
				# werkzeug generatre password hash
				
				hash_pass = generate_password_hash(form['user_password'])
				
				#Create new user with hashed password
				users_coll.insert_one(
					{
						'username': form['username'],
						'email': form['email'],
						'password': hash_pass
					}
				)
				
				# this section is to ensure that the user is in the db
				
				user_in_db = users_coll.find_one({"username": form['username']})
				
				if user_in_db:
					
					session['user'] = user_in_db['username']
					return redirect(url_for('get_reviews', user=user_in_db['username']))
				
				else:
					flash("There was a problem savaing your profile")
					return redirect(url_for('signup'))

		else:
			flash("Passwords dont match!")
			return redirect(url_for('signup'))
		
	return render_template("signup.html")
	

@app.route('/logout')
def logout():
    session.clear()
    flash("you're logged out !")
    return render_template('index.html')


@app.route('/admin')
def admin():
    if session['user'] == "admin":
        return render_template('admin.html')  
    else:
        flash("restricted area!")
        return render_template('index.html')


@app.route('/bio/<user>')
def bio(user):
    # if if block checks if the user is signed in
    if 'user' in session:   
        # and if they are, it returns the template 
        user_db = users_coll.find_one({"username": user })
        return render_template('bio.html', user=user_db)
    else:
        flash('you have to log in!')
        return render_template('index.html')


# <!-- {{ url_for('bio[user]') }} -->

if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)