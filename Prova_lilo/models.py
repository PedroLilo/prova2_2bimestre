from database import db

class Professores(db.Model):
    __tablename__= "professores"
    id_professores = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    disciplina = db.Column(db.String(50))
    idade = db.Column(db.Integer)

    # construtor
    def __init__(self, nome, disciplina, idade):
        self.nome = nome
        self.disciplina = disciplina
        self.idade = idade

    # representação do objeto criado...
    def __repr__(self):
        return "<Profesor {}>".format(self.nome)