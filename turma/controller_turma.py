from flask import Blueprint, request, jsonify
from .module_turma import list_turma, add_turma, delete_turma

turma_blueprint = Blueprint('turma', __name__) 

@turma_blueprint.route('/turma/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    print('lista turmas')
    return jsonify(list_turma(id_turma))

@turma_blueprint.route("/turma", methods=["POST"])
def create_turma():
    dict = request.json
    dict['id'] = int(dict['id'])
    add_turma(dict)
    return jsonify(list_turma())

@turma_blueprint.route("/turma/<int:id_turma>", methods=["DELETE"])
def delete_turma(id_turma):
    delete_turma(id_turma)
    return "turma deletada" 
