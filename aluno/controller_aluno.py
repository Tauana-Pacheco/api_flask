from flask import Flask, request
import module_aluno as model

app = Flask(__name__) 

@app.route('/aluno', methods=['GET'])
def get_aluno():
   print('lista de alunos')
   return model.lista_alunos()

@app.route("/cria-aluno", methods=["POST"])
def cria_aluno():
    dict = request.json
    dict['id'] = int(dict['id'])
    model.adiciona_aluno(dict)
    return model.lista_alunos()

@app.route("/deleta-aluno", methods=["DELETE"])
def reseta():
    model.deleta_aluno()
    return "aluno deletada" 

if __name__ == '__main__':
   app.run(debug=True)