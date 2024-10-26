from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(30))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    ativo = db.Column(db.Boolean)

    def __init__(self, id):
         self.id = id
      
    def __init__(self, descricao):
         self.descricao = descricao
      
    def __init__(self, professor_id):
         self.professor_id = professor_id
      
    def __init__(self, ativo):
         self.ativo = ativo
    
    def to_dict(self):
         return {
        'id': self.id, 
        'descricao': self.descricao, 
        'professor_id': self.professor_id, 
        'ativo': self.ativo, 
      }

class Turma_Excluida(Exception):
   pass

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise Turma_Excluida
    return turma.to_dict()

def list_turma():
  turmas = Turma.query.all()
  return [turma.to_dict() for turma in turmas]

def add_turma(nome, professor_id):
    nova_turma = Turma(nome=nome, professor_id=professor_id)
    db.session.add(nova_turma)
    db.session.commit()
  
def delete_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise Turma_Excluida
    db.session.delete(turma)
    db.session.commit()