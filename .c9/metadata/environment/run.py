{"filter":false,"title":"run.py","tooltip":"/run.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":15},"action":"insert","lines":["import os","#import env","from flask import Flask ","","#SECRET_KEY = os.getenv('MONGO_URI_SECRET_KEY')","","","app = Flask(__name__) #dunder ","","@app.route('/') #proof of concept","def home():","    return \"Hello World . . Me again!!\"","    ","if __name__ == '__main__': ","    app.run(host=os.environ.get('IP'),","    port=int(os.environ.get('PORT')),","    debug=True)"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":0},"end":{"row":5,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1579098763968,"hash":"78cd850101dc375034ecf8e190ca1425c1207d8b"}