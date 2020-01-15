import os
#import env
from flask import Flask 

#SECRET_KEY = os.getenv('MONGO_URI_SECRET_KEY')

app = Flask(__name__) #dunder 

@app.route('/') #proof of concept
def home():
    return "Hello you, World . . Me again!!"
    
if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)