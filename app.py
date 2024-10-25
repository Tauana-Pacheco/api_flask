import os
from config import app, db
#from aluno.aluno_controller import alunos_blueprint
from professor.professor_controller import professor_blueprint
from turma.turma_controller import turma_blueprint

#app.register_blueprint(alunos_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(turma_blueprint)

with app.app_context():
  db.create_all()
  
if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'], debug=app.config['DEBUG'] )
