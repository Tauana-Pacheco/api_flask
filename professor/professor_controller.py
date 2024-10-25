from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .professor_model import ProfessorDemitido, list_profs, add_prof, delete_prof, update_aluno, prof_por_id
from config import db

professor_blueprint = Blueprint('professor', __name__) 

@professor_blueprint.route('/professor/<int:id_professor>', methods=['GET'])
def get_prof(id_professor):
    return list_profs(id_professor)

@professor_blueprint.route("/professor", methods=["POST"])
def create_prof():
    data = request.json
    return jsonify(data)

@professor_blueprint.route('/professor/<int:id_professor>', methods=['PUT'])
def update_aluno(id_professor):
    data = request.json
    try:
        add_prof(id_professor, data)
        return jsonify(prof_por_id(id_professor))
    except ProfessorDemitido:
        return jsonify({'message': 'Professor não encontrado, verifique novamente!'}), 404

@professor_blueprint.route("/professor/<int:id_professor>", methods=["DELETE"])
def delete_prof(id_professor):
    delete_prof(id_professor)
    return "professor demitido" 