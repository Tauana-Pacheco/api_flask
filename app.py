import os
from config import app, db
from aluno.aluno_routes import alunos_blueprint
from professor.prof_routes import profs_blueprint
from turma.turma_routes import turma_blueprint

app.register_blueprint(alunos_blueprint)
app.register_blueprint(profs_blueprint)
app.register_blueprint(turma_blueprint)

with app.app_context():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )