import os
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
    return render_template('index.html')


@app.route('/get_reviews')
def get_reviews():
    return render_template("book_review.html",
    books=mongo.db.books.find()) 
    # supply collection here with find method to return book collection from mdb



@app.route('/login', methods=['GET'])
def login():
    if 'user' in session:
        user_db = users_coll.find_one({"username" : session['user']})
        if user_db:
            flash("you're already logged in!")  
            return redirect(url_for('get_reviews', user=user_db['username']))
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
                return redirect(url_for('get_reviews', user=user_db['username']))
        else:
             flash("password or username is incorrect")
             return redirect(url_for('login'))
    else:
        flash("You gotta sign up !")
        return redirect(url_for('signup'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	
	if 'user' in session:
		flash("you're alreadty signed in like!")
		return redirect(url_for('get_reviews'))
		
	if request.method == 'POST':
		form = request.form.to_dict()
		 
		if form['user_password'] == form['confirm_password']: # need to insert a popup saying 'confirm pw'
			
			user = users_coll.find_one({"username" : form['username']})
			if user:
				flash(f"{form['username']} already exists!")
				return redirect(url_for('signup'))
			
			else:				
				# hash pass
				
				hash_pass = generate_password_hash(form['user_password'])
				
				#Create new user with hashed password
				users_coll.insert_one(
					{
						'username': form['username'],
						'email': form['email'],
						'password': hash_pass
					}
				)
				
				# Check if user is actualy saved
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

"""   
@app.route('/bio/<user>')
def bio():
    if 'user' in session:   
        user_db = users_coll.find_one({"username": user })
        return render_template('bio.html', user=user_db)
    else:
        flash('you have to log in!')


@app.route('/logout')
def logout():
    session.clear()
    flash("you're logged out !")
    return render_template('index.html')

@app.route('/admin')
def admin():
    if session['user'] == "Neil_Admin":
        return render_template('admin.html')  
    else:
        flash("restricted area!")
        return render_template('index.html')


"""

if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)