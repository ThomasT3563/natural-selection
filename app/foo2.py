import os
from flask import Flask,render_template,request

#déclare le serveur flask
app = Flask(__name__)

#crée la route web de la racine du site
#et la lie à la fonction index
@app.route("/")
def index():
    return "ceci est la page index"

#on crée la nouvelle route et on la lie à fonction Hello
@app.route('/hello')
def hello():
    return render_template('/usr/src/app/hello.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port) 