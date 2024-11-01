from flask import Blueprint, request, render_template,redirect, url_for, jsonify
from .prof_model import Professor, ProfessorNaoEncontrado, atualizar_professor, adicionar_professor, listar_professores, professor_por_id, excluir_professor
from config import db
from turma.turma_model import Turma

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return render_template("professores.html", professores=professores)

## ROTA PARA UM PROFESSORES
@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor_id.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404

## ROTA ACESSAR O FORMULARIO DE CRIAÇÃO DE UM NOVOS PROFESSORES   
@professores_blueprint.route('/professores/adicionar', methods=['GET'])
def adicionar_professor_page():
    turmas = Turma.query.all()  # Busca todas as turmas
    return render_template('criarProfessor.html', turmas=turmas)

## ROTA QUE CRIA UM NOVO PROFESSOR
@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    nome = request.form['nome']
    idade = request.form['idade']
    materia = request.form['materia']
    observacoes = request.form['observacoes']
    turmas_ids = request.form.getlist('turmas')  # Captura as turmas selecionadas

    # Cria uma instância do novo professor
    novo_professor = Professor(nome=nome, idade=idade, materia=materia, observacoes=observacoes)

    # Adiciona o novo professor ao banco de dados
    db.session.add(novo_professor)
    db.session.commit()

    # Associa as turmas selecionadas ao novo professor
    for turma_id in turmas_ids:
        turma = Turma.query.get(turma_id)  # Busca a turma pelo ID
        if turma:
            turma.professor_id = novo_professor.id  # Associa a turma ao professor

    db.session.commit()

    return redirect(url_for('professores.get_professores'))

## ROTA PARA O FORMULARIO PARA EDITAR UM NOVO PROFESSOR
@professores_blueprint.route('/professores/<int:id_professor>/editar', methods=['GET'])
def editar_professor_page(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professores_update.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


## ROTA QUE EDITA UM ALUNO
@professores_blueprint.route('/professores/<int:id_professor>/editar', methods=['PUT',"POST"])
def update_professor(id_professor):
        print("Dados recebidos no formulário:", request.form)
        try:
            professor = professor_por_id(id_professor)
            nome = request.form['nome']
            professor['nome'] = nome
            idade = request.form['idade']
            professor['idade'] = idade
            materia = request.form['materia']
            professor['materia'] = materia
            observacoes = request.form['observacoes']
            professor['observacoes'] = observacoes
            atualizar_professor(id_professor, professor)
            return redirect(url_for('professores.get_professor', id_professor=id_professor))
        except ProfessorNaoEncontrado:
            return jsonify({'message': 'Professor não encontrado'}), 404
   

## ROTA QUE DELETA UM PROFESSOR
@professores_blueprint.route('/professores/delete/<int:id_professor>', methods=['DELETE','POST'])
def delete_professor(id_professor):
        try:
            excluir_professor(id_professor)
            return redirect(url_for('professores.get_professor'))
        except ProfessorNaoEncontrado:
            return jsonify({'message': 'Professor não encontrado'}), 404
  