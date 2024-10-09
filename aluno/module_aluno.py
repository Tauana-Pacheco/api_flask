aluno = {"alunos": [{
  "id": "aluno02",
  "nome": "Mariazinha",
  "turma": "3A",
  "data_nascimento": "10/03/2000",
  "nota_primeiro_semestre": "8",
  "nota_segundo_semestre": "6",
  "media_final": "7",
}, 
{
  "id": "aluno02",
  "nome": "Jose ",
  "turma": "3A",
  "data_nascimento": "10/03/2002",
  "nota_primeiro_semestre": "9.5",
  "nota_segundo_semestre": "6",
  "media_final": "8",
}]}

class Aluno(Exception):
  pass

def aluno_por_id(id_aluno):
    lista_alunos = aluno['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise Aluno

def list_alunos():
   return aluno["alunos"]

def add_aluno(dict):
   aluno['alunos'].append(dict)

def delete_aluno(id_aluno):
    alunos = aluno_por_id(id_aluno)
    aluno['alunos'].remove(alunos)