from flask import Flask, jsonify

app = Flask(__name__) 

professor = {
  "id": "profId",
  "nome": "Maria",
  "idade": "30",
  "materia": "biologia",
  "observacoes": "xxx",
}

@app.route('/professor', methods=['GET'])
def get_turma():
    return jsonify({'professor': professor})

if __name__ == '__main__':
    app.run(debug=True)