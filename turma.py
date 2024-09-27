from flask import Flask, jsonify

app = Flask(__name__) 

turma = {
  "id": "turmaId",
  "descricao": "turmaX",
  "professor": "joana",
  "ativo": "ativo",
}

@app.route('/turma', methods=['GET'])
def get_turma():
    return jsonify({'turma': turma})

if __name__ == '__main__':
    app.run(debug=True)