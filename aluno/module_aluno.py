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

def lista_alunos():
   return aluno["alunos"]

def adiciona_aluno(dict):
   aluno['alunos'].append(dict)

def deleta_aluno():
    aluno['alunos'] = []