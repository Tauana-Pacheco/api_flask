from flask import Blueprint, request, jsonify
from .module_professor import list_prof, add_prof, delete_prof

professor_blueprint = Blueprint('professor', __name__) 

@professor_blueprint.route('/professor/<int:id_professor>', methods=['GET'])
def get_prof(id_professor):
    return jsonify(list_prof(id_professor))

@professor_blueprint.route("/professor", methods=["POST"])
def create_prof():
    dict = request.json
    dict['id'] = int(dict['id'])
    add_prof(dict)
    return jsonify(list_prof())

@professor_blueprint.route("/professor/<int:id_professor>", methods=["DELETE"])
def delete_prof(id_professor):
    delete_prof(id_professor)
    return "professor deletado" 
