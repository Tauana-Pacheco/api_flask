turma = {"turma":[{
  "id": "turmaId",
  "descricao": "turmaX",
  "professor": "joana",
  "ativo": "ativo",
}]}

class Aluno(Exception):
  pass

def lista_turma():
  return turma["alunos"]

def adiciona_turma(dict):
  turma['turma'].append(dict)

def deleta_turma():
    turma['turma'] = []