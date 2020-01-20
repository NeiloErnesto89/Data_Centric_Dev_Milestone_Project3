"""
from flask import Flask
#from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signups = signup_coll.find() # signups = mongo.db.signup_forms.find()
    if request.method == 'POST':
        user_db = users_coll.find_one({"username": request.form['username']})
        if user_db:
            flash("Sorry profile already exists!")
            return render_template("signup.html", signups=signups)
        hashed_pass = generate_password_hash(request.form['users_password'])
        users_coll.insert_one(
        {'username': request.form['username'],
            'email': request.form['email'],
            'password': hashed_pass})
        user_db = users_coll.find_one({"username": request.form['username']})
        session['user'] = request.form['username']
        return redirect(url_for('bio', user_id=user_db['_id']), signups=signups)
    if 'user' in session:
        user_db = mongo.db.users.find_one(
            {'username': session['user']})
        return render_template('signup.html', user_id=user_db['_id'], username=session['user'], signups=signups)
    return render_template("signup.html", signups=signups)
    


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username == 'Neilo':
            username = 'NEILO'
        password = request.form['users_password']
        try:
            user_db = users_coll.find_one({"username": username})
        except:
            flash("Sorry, there's an issue !")
            return redirect(url_for('login'))
        if user_db:
            if check_password_hash(user_db['password'], password):
                session['user'] = username
                flash(f"You are logged in as {username}")
                redirect_url = request.referrer
                return redirect(redirect_url)
        else:
            flash('Opps, something is in invalid!')
            return redirect(url_for('login'))

    else:
        return redirect(url_for('login'))
        
@app.route('/logout')
def logout():
    session.pop('user')
    flash('Successfully logged out')
    redirect_url = request.referrer
    return redirect(redirect_url)
    
@app.route('/bio/<user_id>')
def bio(user_id):
    signups = signup_coll.find()
    if 'user' in session:
        user_db = mongo.db.users.find_one(
            {'username': session['user']})
        return render_template("bio.html")
    return redirect(url_for('index', signups=signups))

def index(password):
    if request.method == 'POST':
        form = request.form
    
    #hashed_value = generate_password_hash(password)
    
    stored_password = 'pbkdf2:sha256:150000$X3UrcT74$cf9a77f6f16f839369159274a32b2d136aea48c94aab1dafcfd56c33cf025e79'
    
    result = check_password_hash(stored_password, password)
    
    return str(result) # boolean so need to return string  #hashed_value
       
    return render_template('signup.html')
      
    
if __name__ == '__main__' :
    app.run(debug=True)
    
"""

