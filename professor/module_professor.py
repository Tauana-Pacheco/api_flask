professor = {"professor":[{
  "id": "profId",
  "nome": "Maria",
  "idade": "30",
  "materia": "biologia",
  "observacoes": "xxx",
}]}


class Professor(Exception):
   pass

def lista_professor():
   return professor["professor"]

def adiciona_aluno(dict):
   professor['professor'].append(dict)

def deleta_professor():
    professor['professor'] = []