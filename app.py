import os, datetime, math, re # re is regular extension
import json
from bson.json_util import dumps
from os import path
if path.exists("env.py"):
    import env
#from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_pymongo import PyMongo, pymongo # for paginate functionality
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash  
from forms import CommentForm # flask wtf from form.py e.g. ReviewForm
from flask_wtf import csrf

app = Flask(__name__) #dunder 
#app.config['MONGODB_NAME']= os.environ.get('MONGODB_NAME') 
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)

# MDB Collections

users_coll = mongo.db.users 
books_coll = mongo.db.books
removed_coll = mongo.db.removed_by
comment_coll = mongo.db.comments

"""
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


# paginate code has been taken and modifed/adapted from 'ShaneMuir_Alumni' via a Slack Thread 
@app.route('/all_reviews')
def all_reviews():
    
    """
    This route decorator allows users to see a specific amount of the book reivews 
    with the paginate function.
    """
    page_limit = 4  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.books.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    books = mongo.db.books.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
            
    if 'user' in session: 
        _user = books_coll.find_one({"_id" : ObjectId(session['user_id'])})
            
        return render_template('all_reviews.html', books=books,
                               title='Home', current_page=current_page,
                               pages=pages, _user=_user)
    else:
        return render_template('all_reviews.html', books=books,
                               title='Home', current_page=current_page,
                               pages=pages)
    

@app.route('/review_page')
def review_page():
    return render_template("add_review.html")


## Book Image/Pic Link Function ##
    ## code taken and adapted from fellow coding student MS3 project - https://github.com/JBroks/booksy-reviews

def book_image(cover_pic):
    if cover_pic == '':
        # if no link provide then implement placeholder
        
        pic = "https://via.placeholder.com/468x60?text=No+Image+Available+on+Bukish"
    
    else:
        # correct link provided
        if any(re.findall(r'jpeg|jpg|png', cover_pic, re.IGNORECASE)):
            pic = cover_pic
        # incorrect or no link provided 
        else:
            pic = "https://via.placeholder.com/468x60?text=No+Image+Available+on+Bukish"
            
    return pic 

@app.route('/add_review', methods=['POST'] )
def add_review():
    books=mongo.db.books
    pic = book_image(request.form.get('pic'))
    books.insert_one({
        'book_title' : request.form.get('book_title'),
        'book_author' : request.form.get('book_author'),
        'category_name' : request.form.get('category_name'),
        'pic' : pic,
        'summary' : request.form.get('summary'),
        'stars' : request.form.get('stars'),
        'date' : datetime.datetime.utcnow(), #get the time and date in mdb
        'is_available' : request.form.get('is_available'),
        'added_by' : {
            '_id': ObjectId(session['user_id'])} 
        })
    return redirect(url_for('all_reviews'))

# COMMENT FORM SECTION #

# display comment form with wtf 


"""
@app.route('/add_comment', methods=['POST'] )
def add_comment():
    books=mongo.db.comments
    books.insert_one({
        'book_title' : request.form.get('book_title'),
        'comment' : request.form.get('comment'),
        'added_by' : {
            '_id': ObjectId(session['user_id'])} 
        }) 
""" 

# form = RecipeForm(request.form)

@app.route('/all_comments')
def all_comments():
    #comments=mongo.db.comments
    #return render_template("all_comments.html", comments=comments)
    
    form = CommentForm()
    
    page_limit = 4  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.comments.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    comments = mongo.db.comments.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
            
    if 'user' in session: 
        _user = comment_coll.find_one({"_id" : ObjectId(session['user_id'])})
            
        return render_template('all_comments.html', comments=comments,
                               title='Home', current_page=current_page,
                               pages=pages, _user=_user, form=form)
    else:
        return render_template('all_comments.html', comments=comments,
                               title='Home', current_page=current_page,
                               pages=pages, form=form)

# Get Comment Form #
    
@app.route('/comment_page')
def comment_page():
    form = CommentForm()
    #books=mongo.db.books
    #comments=mongo.db.comments
    return render_template("comment_form.html", form=form)
    
    
@app.route('/comment_form', methods=('GET', 'POST'))
def comment_form():
    
    form = CommentForm()
    
    if 'user_id' in session:   
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    if form.validate_on_submit(): # if form is submitted comments are added to DB
        comments=mongo.db.comments
        comments.insert_one({
            'book_title' : request.form.get('book_title'),
            'user_comments' : request.form.get('user_comments'),
            'added_by' : {
                '_id': ObjectId(session['user_id'])} 
                })
        flash('COMMENT ADDED!')
        return redirect(url_for('all_comments', user=_user, form=form))
    return render_template('comment_form.html', user=_user, form=form, books=mongo.db.books.find())

"""
@app.route('/comment_form', methods=('GET', 'POST'))
def comment_form():
    
    # books=mongo.db.books # for the book selection maybe
    
    form = CommentForm(request.form) # boot up comment_form 
    if 'user_id' in session:   
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    #import pdb;pdb.set_trace()
    #csrf.generate_csrf()
    if request.method == 'POST' and form.validate_on_submit(): # if form is submitted comments are added to DB
        comments=mongo.db.comments
        comments.insert_one({
            'book_title' : request.form.get('book_title'),
            'user_comments' : request.form.get('user_comments'),
            'added_by' : {
                '_id': ObjectId(session['user_id'])} 
                })
        flash('COMMENT ADDED!')
        return redirect(url_for('all_comments', form=form)) #adds review formerly - all_reviews
        
    return render_template('comment_form.html', form=form,  user=_user)

"""


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    
    if 'user_id' in session:   
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        return render_template('comments.html', user=_user, books=mongo.db.books.find())
        


"""
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId('book_title')})
    return redirect(url_for('bio'))

"""


@app.route('/login', methods=['GET'])
def login():
    if 'user' in session: #session id from Flask stored as cookie
        _user = users_coll.find_one({"_id" : ObjectId(session['user_id'])})
        if _user:
            flash("you're already logged in!")  
            return redirect(url_for('bio')) #get_reviews formerly 
    else:
        return render_template('login.html')
        
        

@app.route('/user_login', methods=['POST'])
def user_login():
    form = request.form.to_dict()
    _user = users_coll.find_one({"username" : form['username']}) # user
    
    # to see if the user in in the mdb
    if _user:
        
        # werkzeug checking hash(stored) with real passwd
        if check_password_hash(_user['password'], form['user_password']):
            _dump = dumps(_user['_id']) 
            _dump = json.loads(_dump)
            #import pdb; pdb.set_trace() # used to trace the source of the json error
            session['user_id'] = _dump['$oid']
            
            #  redirect to admin section 
            # import pdb; pdb.set_trace() #### 
            if _user['username'] == "admin":
                    return redirect(url_for('admin'))
            else:
                flash("welcome back!")
                return redirect(url_for('bio')) #get_reviews formerly 
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
				
				# next step is create a new user bio
				users_coll.insert_one(
					{
						'username': form['username'],
						'email': form['email'],
						'password': hash_pass
					}
				)
				
				# this section is to ensure that the user is recorded in the db
				
				_user = users_coll.find_one(
				    {"username": form['username']})
				if _user:
				   _dump = dumps(_user['_id']) 
				   _dump = json.loads(_dump)
				   session['user_id'] = _dump['$oid']
				   return redirect(url_for('bio'))
				   
				   
				   """
				user_db = users_coll.find_one(
				    {"username": form['username']})
				if user_db:
					session['user'] = user_db['username']
					return redirect(url_for('bio', user=user_db['username']))
					"""
					
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
    if session['user_id'] == "admin":
        return render_template('admin.html')  
    else:
        flash("restricted area!")
        return render_template('index.html')


@app.route('/bio')
def bio():
    # if if block checks if the user is signed in
    if 'user_id' in session:   
        # and if they are, it returns the template 
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        return render_template('bio.html', user=_user) #remove sending pw, create new dict e.g. new user. Remove key from dict in py
    else:
        flash('you have to log in!')
        return render_template('index.html')


if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)