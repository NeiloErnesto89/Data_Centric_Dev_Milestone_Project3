"""
# Taken and adapt from Werkzeug website - https://werkzeug.palletsprojects.com/en/1.0.x/utils/


@app.route('/<password>')
def index(password):
    #hashed_value = generate_password_hash(password)
    stored_password = 'pbkdf2:sha256:150000$X3UrcT74$cf9a77f6f16f839369159274a32b2d136aea48c94aab1dafcfd56c33cf025e79'
    result = check_password_hash(stored_password, password)
    return str(result) # boolean so need to return string  #hashed_value


# unused models.py file extracted from a mix of these 2 blogs: (https://hackersandslackers.com/flask-login-user-authentication) and (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)


from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User: #(UserMixin)
    def __init__(self, username):
        self.username = username
    
    @property   
    def is_authenticated(self):
        return True
        
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
        
    def get_id(self):
        return self.username
    
    def set_password(self, password):
       # Create hashed password.
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
       # Check hashed password.
        return check_password_hash(self.password, password)  

"""

