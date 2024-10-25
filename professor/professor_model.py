from config import db

class Professor(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nome = db.Column(db.String(80))
      idade = db.Column(db.Integer)
      materia = db.Column(db.String(20))
      observacoes = db.Column(db.String(50)) 
      turmas = db.relationship('Turma', backref='professor', lazy=True)
      
      def __init__(self, id):
         self.id = id
      
      def __init__(self, nome):
         self.nome = nome
      
      def __init__(self, idade):
         self.idade = idade
      
      def __init__(self, materia):
         self.materia = materia
      
      def __init__(self, observacoes):
         self.observacoes = observacoes
      
      def to_dict(self):
         return {
        'id': self.id, 
        'nome': self.nome, 
        'idade': self.idade, 
        'materia': self.materia, 
        'obervacoes': self.obervacoes 
      }

class ProfessorDemitido(Exception):
   pass

def prof_por_id(id_professor):
   prof = Professor.query.get(id_professor)
   if not prof:
        raise ProfessorDemitido
   return prof.to_dict()

def list_profs():
   profs = Professor.query.all()
   return [professor.to_dict() for professor in profs]

def add_prof(professor_data):
   novo_prof = Professor(nome=professor_data['nome'])
   db.session.add(novo_prof)
   db.session.commit()

def update_aluno(id_professor, novos_dados):
   professor = Professor.query.get(id_professor)
   if not professor:
      raise ProfessorDemitido
   professor.nome = novos_dados['nome']
   db.session.commit()

def delete_prof(id_professor):
   professor = Professor.query.get(id_professor)
   if not professor:
      raise ProfessorDemitido
   db.session.delete(professor)
   db.session.commit()