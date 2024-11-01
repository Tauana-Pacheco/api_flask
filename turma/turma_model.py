from config import db

class Turma(db.Model):
  __tablename__ = 'turma'
  id = db.Column(db.Integer, primary_key=True)
  descricao = db.Column(db.String(80))
  professor_id = db.Column(db.Integer, db.ForeignKey("professor.id"), nullable=False)
  ativo = db.Column(db.Boolean, default=True)

  def __init__(self, descricao, professor_id):
    self.descricao = descricao
    self.professor_id = professor_id

  def to_dict(self):
      return {
          'id': self.id,
          'descricao': self.descricao,
          'professor_id': self.professor_id,
      }

class TurmaNaoEncontrado(Exception):
    pass

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrado
    return turma.to_dict()

def listar_turmas():
   turmas = Turma.query.all()
   return [turma.to_dict() for turma in turmas]

def adicionar_turma(turma_data):
    nova_turma = Turma( 
        descricao=turma_data['descricao'],
        professor_id=turma_data['professor_id'],
        )
    db.session.add(nova_turma)
    db.session.commit()

def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrado
    turma.descricao = novos_dados['descricao']
    turma.professor_id = novos_dados['professor_id']
    db.session.commit()

def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrado
    db.session.delete(turma)
    db.session.commit()