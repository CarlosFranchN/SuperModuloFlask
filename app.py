from flask import Flask,render_template as rt
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "HELLO CARLOS"

@app.route("/hello")
def hello():
    return "<h1>CARLOS ESTEVE AQUI</h1>"

@app.route("/<username>")
def helloUser(username):
    return f"hello user {escape(username)}"

@app.route("/hello/<name>")
def pag(name=None):
    return rt("index.html" ,name = name)

@app.route("/home")
def home():
    return rt("home.html")

@app.route("/skills")
def skills():
    return rt("skills.html")

@app.route("/sobre")
def sobre():
    return rt("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)