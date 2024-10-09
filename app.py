import os
from config import app
from aluno.controller_aluno import alunos_blueprint
from professor.controller_professor import professor_blueprint
from turma.controller_turma import turma_blueprint

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(turma_blueprint)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'], debug=app.config['DEBUG'] )
