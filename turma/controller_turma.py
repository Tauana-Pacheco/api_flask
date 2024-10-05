from flask import Flask, request
import module_turma as model

app = Flask(__name__) 

@app.route('/turma', methods=['GET'])
def get_turma():
    print('lista turmas')
    return model.lista_turma()

@app.route("/cria-turma", methods=["POST"])
def cria_turma():
    dict = request.json
    dict['id'] = int(dict['id'])
    model.adiciona_turma(dict)
    return model.lista_turma()

@app.route("/deleta-turma", methods=["DELETE"])
def reseta():
    model.deleta_turma()
    return "turma deletada" 

if __name__ == '__main__':
    app.run(debug=True)
