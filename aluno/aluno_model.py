from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70))
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.String(10), db.ForeignKey('turma.id'), nullable=False)
    nota_1st = db.Column(db.Float)
    nota_2st = db.Column(db.Float)

    def __init__(self, nome, idade, turma_id, nota_1st, nota_2st):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.nota_1st = nota_1st
        self.nota_2st = nota_2st

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'nota_1st': self.nota_1st,
            'nota_2st': self.nota_2st,
        }

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(aluno_data):
    novo_aluno = Aluno(
        nome=aluno_data['nome'], 
        idade=aluno_data['idade'],
        turma_id=aluno_data['turma_id'],
        nota_1st=aluno_data['nota_1st'],
        nota_2st=aluno_data['nota_2st'],
        )
    db.session.add(novo_aluno)
    db.session.commit()

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    aluno.nome = novos_dados['nome']
    aluno.idade = novos_dados['idade']
    db.session.commit()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()