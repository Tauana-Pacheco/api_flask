from config import db

class Turma(db.Model):
  __tablename__ = 'turma'
  id = db.Column(db.Integer, primary_key=True)
  descricao = db.Column(db.String(80))
  professor_id = db.Column(db.Integer, db.ForeignKey("professor.id"), nullable=False)
  ativo = db.Column(db.Boolean)

  alunos = db.relationship('Aluno', backref='turma', lazy=True)

  def __init__(self, descricao, professor_id, ativo, alunos):
    self.descricao = descricao
    self.professor_id = professor_id
    self.ativo = ativo
    self.alunos = alunos

  def to_dict(self):
      return {
          'id': self.id,
          'descricao': self.descricao,
          'professor_id': self.professor_id,
          'ativo': self.ativo,
          'alunos': [aluno.to_dict() for aluno in self.alunos]
      }
