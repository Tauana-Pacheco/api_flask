from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .turma_model import Turma, TurmaNaoEncontrado, turma_por_id, listar_turmas, atualizar_turma, adicionar_turma, excluir_turma
from professor.prof_model import Professor 

turma_blueprint = Blueprint('turmas', __name__)

## ROTA PARA TODOS AS TURMAS
@turma_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return render_template('turmas.html', turmas=turmas)

## ROTA PARA UMA TURMA
@turma_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_id.html', turma=turma)
    except TurmaNaoEncontrado:
        return jsonify({'message': 'Turma não encontrado'}), 404

## ROTA ACESSAR O FORMULARIO DE CRIAÇÃO DE UM NOVAS TURMAS
@turma_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turma_page():
    professores = Professor.query.all()  # Busca todos os professores
    return render_template('criarTurmas.html', professores=professores)

## ROTA QUE CRIA UM NOVA TURMA
@turma_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    descricao = request.form['descricao']
    professor_id = request.form['professor_id']
    nova_turma = Turma(descricao=descricao, professor_id=professor_id)
    adicionar_turma(nova_turma)
    return redirect(url_for('turmas.get_turmas'))

## ROTA PARA O FORMULARIO PARA EDITAR UM NOVO ALUNO
@turma_blueprint.route('/turmas/<int:id_turma>/editar', methods=['GET'])
def editar_turma_page(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_update.html', turma=turma)
    except TurmaNaoEncontrado:
        return jsonify({'message': 'Turma não encontrado'}), 404

## ROTA QUE EDITA UM ALUNO
@turma_blueprint.route('/turmas/<int:id_turma>/editar', methods=['PUT',"POST"])
def update_turma(id_turma):
        print("Dados recebidos no formulário:", request.form)
        try:
            turma = turma_por_id(id_turma)
            descricao = request.form['descricao']
            turma['descricao'] = descricao
            professor_id = request.form['professor_id']
            turma['professor_id'] = professor_id
            atualizar_turma(id_turma, turma)
            return redirect(url_for('turmas.get_turma', id_turma=id_turma))
        except TurmaNaoEncontrado:
            return jsonify({'message': 'Turma não encontrado'}), 404

## ROTA QUE DELETA UM ALUNO
@turma_blueprint.route('/turmas/delete/<int:id_turma>', methods=['DELETE','POST'])
def delete_turma(id_turma):
        try:
            excluir_turma(id_turma)
            return redirect(url_for('turmas.get_turmas'))
        except TurmaNaoEncontrado:
            return jsonify({'message': 'Turma não encontrada'}), 404
  
