professor = {"professor":[{
  "id": "profId",
  "nome": "Maria",
  "idade": "30",
  'id_professor': "1",
  "materia": "biologia",
  "observacoes": "xxx",
}]}

class Professor(Exception):
   pass

def prof_por_id(id_professor):
    lista_prof = professor['professor']
    for dicionario in lista_prof:
        if dicionario['id'] == id_professor:
            return dicionario
    raise Professor

def list_prof():
   return professor["professor"]

def add_prof(dict):
   professor['professor'].append(dict)

def delete_prof(id_professor):
    prof = prof_por_id(id_professor)
    professor['professor'].remove(prof)