from flask import Blueprint
from .turma_model import Turma

turma_blueprint = Blueprint('turmas', __name__)

@turma_blueprint.route('/turma', methods=['GET'])
def get_turma():
  return 'turrrminhas'