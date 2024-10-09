turma = {"turma":[{
  "id": "turmaId",
  "descricao": "turmaX",
  "professor": "joana",
  "ativo": "ativo",
}]}

class Turma(Exception):
  pass

def turma_por_id(id_turma):
    list_turma = turma['alunos']
    for dicionario in list_turma:
        if dicionario['id'] == id_turma:
            return dicionario
    raise Turma

def list_turma():
  return turma["turma"]

def add_turma(dict):
  turma['turma'].append(dict)

def delete_turma(id_turma):
    turmas = turma_por_id(id_turma)
    turma['turma'].remove(turmas)