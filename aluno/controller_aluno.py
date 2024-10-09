from flask import Blueprint, request
from .module_aluno import list_alunos, add_aluno, delete_aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
   print('lista de alunos')
   return list_alunos(id_aluno)

@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
    dict = request.json
    dict['id'] = int(dict['id'])
    add_aluno(dict)
    return list_alunos()

@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def delete_aluno(id_aluno):
    delete_aluno(id_aluno)
    return "aluno deletada" 
