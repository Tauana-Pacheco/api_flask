from config import db

class Professor(db.Model):
  __tablename__ = 'professor'
  id =  db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(60))
  idade = db.Column(db.Integer)
  materia = db.Column(db.String(60))
  observacoes = db.Column(db.String(80))
  turmas = db.relationship('Turma', backref='professor', lazy=True)


  def __init__(self, nome, idade, materia, observacoes, turmas):
    self.nome = nome
    self.idade = idade
    self.materia  = materia
    self.observacoes = observacoes
    self.turmas = turmas

  def to_dict(self):
    return {
          'id': self.id,
          'nome': self.nome,
          'idade': self.idade,
          'materia': self.materia,
          'observacoes': self.observacoes,
          'turmas': [turma.to_dict() for turma in self.turmas]
        }
