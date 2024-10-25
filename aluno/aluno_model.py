from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer) # not null redundante?
    turma = db.Column(db.String(5))
    data_nasc = db.Column(db.Date) # not nul redundante?
    nota_1st = db.Column(db.Decimal)
    nota_2nd = db.Column(db.Decimal)

    def __init__(self, id):
         self.id = id
      
    def __init__(self, nome):
        self.nome = nome
    
    def __init__(self, idade):
        self.idade = idade
    
    def __init__(self, turma):
        self.turma = turma
    
    def __str__(self, nota_1s):
        self.nota_1st = nota_1s
      
    def __str__(self, nota_2s):
        self.nota_2st = nota_2s

    def to_dict(self):
        return {
        'id': self.id, 
        'nome': self.nome,
        'idade': self.idade, 
        'turma': self.turma,
        'nota_1s': self.nota_1st,
        'nota_2s': self.nota_2st,
        }
  
class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def list_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def add_aluno(aluno_data):
    novo_aluno = Aluno(nome=aluno_data['nome'])
    db.session.add(novo_aluno)
    db.session.commit()

def update_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    aluno.nome = novos_dados['nome']
    db.session.commit()
    
def delete_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()