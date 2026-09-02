from flask import Blueprint, request
from Controllers.DiaSemanaController import DiaSemanaController

dia_semana_bp = Blueprint('dia_semana', __name__)
dia_semana_controller = DiaSemanaController()


@dia_semana_bp.route('/dias-semana', methods=['GET'])
def obtener_todos():
    return dia_semana_controller.obtener_todos()


@dia_semana_bp.route('/dias-semana/<int:dia_sem_id>', methods=['GET'])
def obtener_por_id(dia_sem_id):
    return dia_semana_controller.obtener_por_id(dia_sem_id)


@dia_semana_bp.route('/dias-semana', methods=['POST'])
def crear():
    return dia_semana_controller.crear(request.get_json())


@dia_semana_bp.route('/dias-semana/<int:dia_sem_id>', methods=['PUT'])
def actualizar(dia_sem_id):
    return dia_semana_controller.actualizar(dia_sem_id, request.get_json())


@dia_semana_bp.route('/dias-semana/<int:dia_sem_id>', methods=['DELETE'])
def eliminar(dia_sem_id):
    return dia_semana_controller.eliminar(dia_sem_id)
