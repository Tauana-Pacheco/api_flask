from flask import Flask, jsonify

app = Flask(__name__) 

aluno = {
  "id": "alunoId",
  "nome": "Mariazinha",
  "turma": "3A",
  "data_nascimento": "10/03/2000",
  "nota_primeiro_semestre": "8",
  "nota_segundo_semestre": "6",
  "media_final": "7",
}

@app.route('/aluno', methods=['GET'])
def get_turma():
    return jsonify({'aluno': aluno})

if __name__ == '__main__':
    app.run(debug=True)