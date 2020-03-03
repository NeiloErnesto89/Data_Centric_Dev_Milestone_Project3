import os, datetime, math, re
# re is regular extension
import json
import random
from bson.json_util import dumps
from os import path
if path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_pymongo import PyMongo, pymongo # for paginate functionality
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CommentForm


app = Flask(__name__) # dunder
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# MDB Collections

users_coll = mongo.db.users
books_coll = mongo.db.books
removed_coll = mongo.db.removed_by
comment_coll = mongo.db.comments


"""
# taken and adapt from Werkzeug website - https://werkzeug.palletsprojects.com/en/1.0.x/utils/
@app.route('/<password>')
def index(password):
    #hashed_value = generate_password_hash(password)
    stored_password = 'pbkdf2:sha256:150000$X3UrcT74$cf9a77f6f16f839369159274a32b2d136aea48c94aab1dafcfd56c33cf025e79'
    result = check_password_hash(stored_password, password)
    return str(result) # boolean so need to return string  #hashed_value
"""

# INITIAL INDEX RENDERING WITH RANDOM QUOTES LIST FOR MODAL #
@app.route('/')
@app.route('/index')
def index():
    books = mongo.db.books
    book_quotes = ["'Well, you know, I love to read. Actually, I’m looking at a book, I’m reading a book, I’m trying to get started.' -- Donald Trump ",
        "'Classic’ – a book which people praise and don’t read.' --  Mark Twain  ",
        "'There is no such thing as a moral or an immoral book. Books are well written, or badly written.' -- Oscar Wilde",
        "'If you don’t like to read, you haven’t found the right book.' -- J.K. Rowling",
        "'Reading brings us unknown friends.' -- Honoré de Balzac",
        "'My problem with reading books is that I get distracted… by other books.' -- Anonymous"]

    random_quote = random.choice(book_quotes) 
    return render_template('index.html', random_quote=random_quote)
       
"""
RENDERING THE ALL REVIEWS SECTION - Paginate Code has been taken
and modifed/adapted from 'ShaneMuir_Alumni' via a Slack Thread and
further from the MS project https://github.com/ShaneMuir/Cookbook-Recipe-Manager
"""

@app.route('/all_reviews')
def all_reviews():
    # Allows users to see a specific amount of the book reivews with a paginate function.

    page_max = 3
    present_page = int(request.args.get('present_page', 1))  # request args requesting var name
    total = mongo.db.books.count()
    pages = range(1, int(math.ceil(total / page_max)) + 1)
    books = mongo.db.books.find().sort('_id', pymongo.ASCENDING).skip(  # Ascending = sort order (i.e. descending = -1)
        (present_page - 1)*page_max).limit(page_max)  # skip must be >= 0
         
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
 
        return render_template('all_reviews.html', books=books,
                               title='Home', present_page=present_page,
                               pages=pages, user=_user)

    else:
        flash('You Have To Be Logged In To Access This Area!')
        return render_template('index.html')

# To Render the Add_Review HTML #

@app.route('/review_page')
# @login_required
def review_page():
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        return render_template("add_review.html", user=_user)
    else:
        flash('You Have To Be Logged In To Access This Area!')
        return render_template('index.html')


# Book Image/Pic Link Function #
    # code taken and adapted from fellow coding student MS3 project - https://github.com/JBroks/booksy-reviews

def book_image(cover_pic):
    if cover_pic == '':
  
        # if no link provide then implement placeholder
   
        pic = "https://via.placeholder.com/700x700/BCBABA/FFFFFF/?text=No+Image+Available+on+Bukish"

    else:
        # correct link provided
        if any(re.findall(r'jpeg|jpg|png', cover_pic, re.IGNORECASE)):
            pic = cover_pic
        # incorrect or no link provided
        else:
            pic = "https://via.placeholder.com/700x700/BCBABA/FFFFFF/?text=No+Image+Available+on+Bukish"
        
    return pic

# Amazon Link Rendering Function - for add_review section #
    # code taken and adapted from fellow coding student MS3 project - https://github.com/JBroks/booksy-reviews
   
def open_amazon_link(book_title, book_author, amazon_url):
 
    if amazon_url == '':
        amazon_route = 'https://www.amazon.co.uk/s?k='
        amazon_add = amazon_route + book_title.replace(' ', '+')+ '+' + book_author.replace(' ', '+')
        amazon_tag = amazon_add.replace('&', 'and') + '&tag=neils'
  
    elif (amazon_url.find('&tag=neils') >=0):
     
        amazon_tag = amazon_url
 
    else:
        if any(re.findall(r'ref|keywords|k=', amazon_url, re.IGNORECASE)):
       
            amazon_tag = amazon_url +'&tag=neils'
       
        elif amazon_url.endswith('/'):
       
            amazon_tag = amazon_url +'&tag=neils'
        
        else:
           
            amazon_tag = amazon_url +'/&tag=neils'
      
    return amazon_tag

# the route decorator to add book review

@app.route('/add_review', methods=['POST'] )
def add_review():
    books=mongo.db.books
    
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    # amazon link 
    title = request.form['book_title']
    writer = request.form['book_author']
    amazon_line = request.form['amazon']
    buy_amazon = open_amazon_link(title, writer, amazon_line)
    
    
    pic = book_image(request.form.get('pic'))
    books.insert_one({
        'book_title': request.form.get('book_title'),
        'book_author': request.form.get('book_author'),
        'category_name': request.form.get('category_name'),
        'pic': pic,
        'amazon': buy_amazon, 
        'summary': request.form.get('summary'),
        'stars': request.form.get('stars'),
        'date': datetime.datetime.utcnow(), # get the time and date in mdb
        'is_available': request.form.get('is_available'),
        'added_by': _user
           # {'_id': ObjectId(session['user_id'])}
        })
    flash("Your Review Has Been Added!") 
    return redirect(url_for('all_reviews'))

# DELETE BOOK REVIEW

@app.route('/delete_review/<book_id>' )
def delete_review(book_id):
    
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        
    mongo.db.books.remove({'_id': ObjectId(book_id)})
    flash("Your Review Has Been Deleted!")
    return redirect(url_for('all_reviews'))
    
# EDIT (USERS) REVIEW 

@app.route('/adapt_review/<book_id>')
def adapt_review(book_id):

    individual_book = mongo.db.books.find_one({'_id': ObjectId(book_id)}) 
    
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        
    return render_template('adapt_review.html', book=individual_book, user=_user) # for jinja temps


@app.route('/edit_review/<book_id>', methods=['POST'])
def edit_review(book_id):

    # adapt_book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})

    # generate and retrieve review details from mdb
    title = request.form['book_title']
    writer = request.form['book_author']
    amazon_line = request.form['amazon']
    buy_amazon = open_amazon_link(title, writer, amazon_line)
    
    # print(request.form)
    pic = book_image(request.form.get('pic'))
    
    mongo.db.books.update({'_id': ObjectId(book_id)},
    {'$set':
        { 
        'book_title': request.form.get('book_title'), 
        'book_author': request.form.get('book_author'),
        'category_name': request.form.get('category_name'),
        'pic': pic,
        'amazon': buy_amazon,
        'summary': request.form.get('summary'),
        'stars': request.form.get('stars'),
        # 'modified_at' : datetime.datetime.utcnow(), # get the time and date in mdb
        # 'is_available' : request.form['is_available'],
        'added_by': _user # ObjectId(session['user_id']) ObjectId(book_id)
        }
        
    })
    flash("Your Review Has Been Updated!")
    return redirect(url_for('individual_reviews', book_id=book_id))
    
    
# ADMIN/ INTERNAL COMMENT/NOTE FORM SECTION #
# Display internal admin comment form with wtf displayed

# Paginate Code has been taken and modifed/adapted from 'ShaneMuir_Alumni' via a Slack Thread and further from the MS project https://github.com/ShaneMuir/Cookbook-Recipe-Manager

@app.route('/all_comments')
def all_comments():
    
    form = CommentForm()
    
    try:
        page_max = 3  #admin comments paginate 
        present_page = int(request.args.get('present_page', 1))
        total = mongo.db.comments.count()
        pages = range(1, int(math.ceil(total / page_max)) + 1)
        comments = mongo.db.comments.find().sort('_id', pymongo.ASCENDING).skip(
            (present_page - 1)*page_max).limit(page_max)
                
        if 'user_id' in session:
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        
        if session['user_id'] == "5e52eae5426c4d0b8d01cbc2":   
            return render_template('all_comments.html', comments=comments,
                                   title='Home', present_page=present_page,
                                   pages=pages, user=_user, form=form)
        else:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')
    
    except:
        if 'user_id' not in session:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')

# Retrieve Internal Comment Form #
    
@app.route('/comment_page')
def comment_page():
    
    form = CommentForm()
    try:
        if 'user_id' in session:
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        
        if session['user_id'] == "5e52eae5426c4d0b8d01cbc2": # admin Object ID
            flash('Welcome to the Internal Admin Forum')
            return render_template("comment_form.html", form=form, user=_user)
        
        else:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')
    
    except:
        if 'user_id' not in session:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')
            
# POSTS INTERNAL ADMIN COMMENT FORM USING FLASK-WTF
    
@app.route('/comment_form', methods=('GET', 'POST'))
def comment_form():
    
    form = CommentForm()
    
    try:
        if 'user_id' in session:   
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
            
        if session['user_id'] == "5e52eae5426c4d0b8d01cbc2": # admin Object ID
            
        # if form is submitted comments are added to DB
            if form.validate_on_submit():
                comments=mongo.db.comments
                comments.insert_one({
                    # 'book_title': books,
                    'book_hook': request.form.get('book_hook'),
                    'user_comments': request.form.get('user_comments'),
                    'added_by': _user
                        # {'_id': ObjectId(session['user_id'])} 
                        })
                flash('Your Note Has Been Added!')
                return redirect(url_for('all_comments', user=_user, form=form))
            return render_template('comment_form.html', user=_user, form=form, books=mongo.db.books.find())
        
        else:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')
     
    except:
        if 'user_id' not in session:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')
            

# DELETE ADMIN COMMENTS

@app.route('/delete_comments/<admin_id>')
def delete_comments(admin_id):
    
    if 'user_id' in session:
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})

    mongo.db.comments.remove({'_id': ObjectId(admin_id)})
    
    flash('Your Comment Has Been Deleted')
    return redirect(url_for('all_comments', admin=admin))


# INDIVIDUAL BOOK REVIEW SECTION

@app.route('/individual_reviews/<book_id>')
def individual_reviews(book_id):
    
    # book id url to match objectid
    
    individual_book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    
    # show comments underneath individual book, new coll bookcomms
    
    individ_comments = mongo.db.bookscomms.find({ 
       "book_id": ObjectId(book_id) }).sort([("_id", -1)])
    
    if 'user_id' in session:   
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    return render_template('individual_book.html', book=individual_book, book_id=book_id, user=_user, incomments=individ_comments) 


# ADD COMMENTS UNDERNEATH INDIVIDUAL REVIEWS #

@app.route('/add_individual/<book_id>', methods=['POST', 'GET'])
def add_individual(book_id):
    
    book_comments = mongo.db.bookscomms
    
    if 'user_id' in session:
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    individual_book = mongo.db.books.find_one({'_id': ObjectId(book_id)})
    
    #bookcom = request.form['individual']
    book_comments.insert_one({
        'individual' : request.form['individual'],
        'book_id': ObjectId(book_id), # if it's individual_book - it adds the details to the mdb
        'added_by' : _user
        })
    flash('Your Comment Has Been Added')
    return redirect(url_for('individual_reviews',
                            book_id=book_id,
                            user=_user))
                          
# DELETES INDIVIDUAL COMMENT # 

@app.route('/delete_individual/<book_id>/<indivd_id>')
def delete_individual(indivd_id, book_id ):
    
    if 'user_id' in session:   
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    indivd = mongo.db.bookscomms.find_one({'_id': ObjectId(book_id)})
    
    mongo.db.bookscomms.remove({'_id': ObjectId(indivd_id)})
    flash('Your Comment Has Been Deleted')
    return redirect(url_for('individual_reviews', indivd_id=indivd_id,
                    book_id=book_id, user=_user))  



# UPDATE INDIVIDUAL USERS COMMENT #

@app.route('/update_individual/<book_id>/<indivd_id>', methods=["POST"])
def update_individual(indivd_id, book_id):
    
    book_comments = mongo.db.bookscomms
   
    if 'user_id' in session:   
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
    
    indivd = mongo.db.bookscomms.find_one({'_id': ObjectId(book_id)})
    
    book_comments.update({'_id': ObjectId(indivd_id)}, 
            {'$set': 
               {'individual': request.form['individual']} 
            })
    flash("Your Comment Has Been Edited!")
    return redirect(url_for('individual_reviews', indivd_id=indivd_id,
                    book_id=book_id, user=_user))
    
        
# USER LOGIN PAGE #

@app.route('/login', methods=['GET'])
def login():
    if 'user_id' in session: # session id from Flask stored as cookie
        _user = users_coll.find_one({"_id" : ObjectId(session['user_id'])})
        if _user:
            flash("You're Already Logged In")
            return redirect(url_for('bio')) #get_reviews formerly 
    else:
        return render_template('login.html')
        
# USER LOGIN FUNCTION  #      

@app.route('/user_login', methods=['POST'])
def user_login():
    form = request.form.to_dict()
    _user = users_coll.find_one({"username": form['username']})  # user

    # to see if the user in in the mdb
    if _user:
   
        # werkzeug checking hash(stored) with real passwd
        if check_password_hash(_user['password'], form['user_password']):
            _dump = dumps(_user['_id'])
            _dump = json.loads(_dump)
            # import pdb; pdb.set_trace() # used to trace the source of the json error
            session['user_id'] = _dump['$oid']
            
            #  redirect to admin section 
            # import pdb; pdb.set_trace() #### 
            if _user['username'] == "admin":
                    flash("Admin Sign In Successful")
                    return redirect(url_for('admin'))
            else:
                flash("Thanks for Coming Back")
                return redirect(url_for('bio'))
        else:
             flash("Password Is Incorrect")
             return redirect(url_for('login'))
    else:
        flash("Oops.. It Looks Like You Have To Sign Up")
        return redirect(url_for('signup'))

# USER SIGNUP FUNCTION #

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	
	if 'user_id' in session:
		flash("You're Already Signed Up")
		return redirect(url_for('bio'))
		
	if request.method == 'POST':
		form = request.form.to_dict()
	 
		if form['user_password'] == form['confirm_password']: 
			
			user = users_coll.find_one({"username": form['username']})
			if user:
				flash(f"{form['username']} already exists! Please Choose Another Username")
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
				   flash("Congratulations on Successfully Signing Up to Bukish!")
				   return redirect(url_for('bio'))
				   
				else:
					flash("There Was A Problem Saving Your Profile")
					return redirect(url_for('signup'))

		else:
			flash("Passwords Dont Match!")
			return redirect(url_for('signup'))

	return render_template("signup.html")

# USER LOGOUT ROUTE DECORATOR #

"""
session.clear() removes all keys/values from session state collection [session.clear()](https://www.codepoc.io/blog/asp-net/5138/what-is-the-difference-between-session-abandon-and-session-clear)
"""

@app.route('/logout')
def logout():
    session.clear()
    flash("You're Currently Not Logged In")
    return render_template('index.html')


# USER BIO ROUTE DECORATOR #

@app.route('/bio')
def bio():
    # if if block checks if the user is signed in
    if 'user_id' in session:
        # and if they are, it returns the template
        _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})
        return render_template('bio.html', user=_user)
    else:
        flash('You Have To Log In Or Sign Up!')
        return render_template('index.html')


# USER BIO ROUTE DECORATOR ##

@app.route('/admin')
def admin():
    try:
        if 'user_id' in session:
            _user = users_coll.find_one({"_id": ObjectId(session['user_id'])})

        if session['user_id'] == "5e52eae5426c4d0b8d01cbc2":  # admin Object ID
            return render_template('admin.html', user=_user)

        else:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')
    except:
        if 'user_id' not in session:
            flash("Restricted Area - Access Denied!")
            return render_template('index.html')


if __name__ == '__main__':

    app.run(host=os.environ.get('IP', '0.0.0.0'),

        port=int(os.environ.get('PORT', 5000)),

        debug=True)

"""
# aws ide

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
"""
