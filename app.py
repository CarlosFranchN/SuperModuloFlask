from flask import Flask,render_template as rt, request
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

@app.route("/exemplo")
def exemplo():
    nome = request.args.get('nome','Anonimo')
    idade = request.args.get('idade',"indefinido")

    return f'Nome:{nome}, Idade:{idade}'
@app.route("/info2")
@app.route("/info2/<string:nome>")
@app.route("/info2/<int:idade>")
@app.route("/info2/<int:idade>/<string:nome>")
@app.route("/info2/<string:nome>/<int:idade>")
def info2(nome = "Anonimo",idade = "indefinida"):

    return f'Nome:{nome}, Idade:{idade}'
    

@app.route("/indexForm", methods=["GET","POST"])
def indexForm():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")

        return f"""
            <script>
                alert("nome: {nome}, idade : {idade}")
                window.location.href = "/indexForm"
            </script>
        """

    return rt("indexForm.html")

@app.route("/imc",methods = ["GET","POST"])
def calcularIMC():
    if request.method == "POST":
        altura = request.form.get("altura")
        peso = request.form.get("peso")

        imc =  float(peso) / (float(altura) ** 2)
        # imc =  peso / (altura ** 2)
        return f"""
            <script>
                alert("SEU IMC É {imc:.2f}!")
                window.location.href = "/imc"
            </script>
        """
    return rt("imc.html")





if __name__ == "__main__":
    app.run(debug=True)