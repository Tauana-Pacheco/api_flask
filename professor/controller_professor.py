from flask import Flask, request
import module_professor as model

app = Flask(__name__) 

@app.route('/professor', methods=['GET'])
def get_professor():
    return model.list_professor()

@app.route("/cria-professor", methods=["POST"])
def cria_professor():
    dict = request.json
    dict['id'] = int(dict['id'])
    model.adiciona_professor(dict)
    return model.lista_professor()

@app.route("/deleta-professor", methods=["DELETE"])
def deleta():
    model.deleta_professor()
    return "professor deletado" 

if __name__ == '__main__':
    app.run(debug=True)
