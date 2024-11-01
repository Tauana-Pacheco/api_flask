from config import db

class Professor(db.Model):
  __tablename__ = 'professor'
  id =  db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(60))
  idade = db.Column(db.Integer)
  materia = db.Column(db.String(60))
  observacoes = db.Column(db.String(80))
  turmas = db.relationship('Turma', backref='professor', lazy=True)

  def __init__(self, nome, idade, materia, observacoes):
    self.nome = nome
    self.idade = idade
    self.materia  = materia
    self.observacoes = observacoes

  def to_dict(self):
    return {
          'id': self.id,
          'nome': self.nome,
          'idade': self.idade,
          'materia': self.materia,
          'observacoes': self.observacoes,
          'turmas': [turma.to_dict() for turma in self.turmas]
        }

class ProfessorNaoEncontrado(Exception):
    pass

def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado
    return professor.to_dict()

def listar_professores():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def adicionar_professor(professor_data):
    novo_professor = Professor(
        nome=professor_data['nome'], 
        idade=professor_data['idade'],
        materia=professor_data['materia'],
        observacoes=professor_data['observacoes'],
        turmas=professor_data['turmas'],
        )
    db.session.add(novo_professor)
    db.session.commit()

def atualizar_professor(id_professor, novos_dados):
   professor = Professor.query.get(id_professor)
   if not professor:
      raise ProfessorNaoEncontrado
   professor.nome = novos_dados['nome']
   professor.idade = novos_dados['idade']
   professor.materia = novos_dados['materia']
   professor.observacoes = novos_dados['observacoes']
   professor.turmas = novos_dados['turmas']
   db.session.commit()

def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado
    db.session.delete(professor)
    db.session.commit()
