from flask import Flask, render_template, request, flash, redirect
from database import db
from flask_migrate import Migrate
from models import Professores

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ebe6f92407c97b3f989420e0e6bebcf9d1976b2e230acf9faf4783f5adffe1b'

# --> drive://usuario:senha@servidor/banco_de_dados

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/Professor_lilo"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def professores():
    u = Professores.query.all()
    return render_template("professores_lista.html", dados = u)

@app.route("/professores/add")
def professores_add():
    return render_template("professores_add.html")

@app.route("/professores/save", methods=['POST'])
def professores_save():
    nome = request.form.get('nome')
    disciplina = request.form.get('disciplina')
    idade = request.form.get('idade')
    if nome and disciplina and idade:
        professores = Professores(nome, disciplina, idade)
        db.session.add(professores)
        db.session.commit()
        flash('Professor salvo com sucesso!!!')
        return redirect('/')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/professores/add')

if __name__ == '__main__':
    app.run()