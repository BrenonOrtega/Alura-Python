from flask import Flask
from flask import render_template, request, Response, redirect
from flask.globals import session
from models.jogo import mock_jogos, Jogo

app = Flask(__name__)
app.secret_key='curso_bryan'

@app.route('/' )
def pagina_inicial():
    jogos = mock_jogos
    return render_template('index.html', titulo = pagina_inicial.__name__, jogos=jogos)

@app.route('/novo-jogo', methods=['GET',])
def novo_jogo():
    return render_template('create.html', titulo="Criar Jogo")

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form.get('nome')
    ano = request.form.get('ano')
    console = request.form.get('console')
    novo_jogo = Jogo(nome, int(ano), console)
    mock_jogos.append(novo_jogo)
    return redirect(location='/')

@app.route('/login')
def login():
    return render_template('login.html', titulo='pagina de login')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    username = request.form.get('input-usuario')
    password = request.form.get('input-senha') 
    session[username.__name__] = username
    session[password.__name__] = password
    autenticado = True if 'mestra' == password else False
    print(username, password)
    return redirect('/') if autenticado else Response(status='401 Forbidden')

if __name__ == '__main__':
    app.run(debug=True)