from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .aluno_model import AlunoNaoEncontrado, list_alunos, aluno_por_id, add_aluno, delete_aluno
from config import db

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
   return list_alunos(id_aluno)

@alunos_blueprint.route("/alunos", methods=["POST"])
def create_aluno():
    data = request.json
    add_aluno(data)
    return jsonify(data), 201

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    data = request.json
    try:
        add_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrad, verifique novamente!'}), 404

@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def delete_aluno(id_aluno):
   try:
        delete_aluno(id_aluno)
        return '', 204
   except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado, verifique novamente!'}), 404