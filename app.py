from flask import Flask,render_template as rt, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "HELLO CARLOS"

@app.route("/hello")
def hello():
    nome = 'Usuario'
    idade = 18
    return f"<h1>{nome} ESTEVE AQUI</h1>"

# @app.route("/<username>")
# def helloUser(username):
#     return f"hello user {escape(username)}"

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
    

@app.route("/form", methods=["GET","POST"])
def indexForm():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")

        return f"""
            <script>
                alert("nome: {nome}, idade : {idade}")
                window.location.href = "/indexForm.html"
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

@app.route('/login')
def index2():
    nome = 'Carlos'
    idade = 16
    # usuario_logado = False
    return rt('index2.html', nome=nome, idade=idade)

@app.route('/lista')
def index3():
    titulo = 'MINHA LISTA'
    lista = ['Carlos', 'Aragorn', 'Aloy']
    return rt('index3.html', lista = lista, titulo = titulo)

lista_de_registro = []

@app.route("/registrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    lista_de_registro.append((nome,idade))
    print(f"{lista_de_registro}")
    return f"""
        <script>
                alert('Nome foi registrado');
                window.location.href = '/registrar';
         </script>
        """
    # return rt('cadastrar.html')
    # return rt('cadastrar.html')

@app.route("/vizualizar")
def printar():
    lista  = lista_de_registro
    return rt('printRegistros.html', lista = lista)





if __name__ == "__main__":
    app.run(debug=True)