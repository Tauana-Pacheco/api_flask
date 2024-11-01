from flask import Blueprint
from .prof_model import Professor

profs_blueprint = Blueprint('profs', __name__)

@profs_blueprint.route('/professs', methods=['GET'])
def getIndex():
    return 'professssss'
