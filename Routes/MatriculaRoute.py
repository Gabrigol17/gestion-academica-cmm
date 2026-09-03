from flask import Blueprint, request
from Controllers.MatriculaController import MatriculaController

matricula_bp = Blueprint('matricula', __name__)
matricula_controller = MatriculaController()


@matricula_bp.route('/matriculas', methods=['GET'])
def obtener_todos():
    return matricula_controller.obtener_todos()


@matricula_bp.route('/matriculas/<int:matr_id>', methods=['GET'])
def obtener_por_id(matr_id):
    return matricula_controller.obtener_por_id(matr_id)


@matricula_bp.route('/matriculas', methods=['POST'])
def crear():
    return matricula_controller.crear(request.get_json())


@matricula_bp.route('/matriculas/<int:matr_id>', methods=['PUT'])
def actualizar(matr_id):
    return matricula_controller.actualizar(matr_id, request.get_json())


@matricula_bp.route('/matriculas/<int:matr_id>', methods=['DELETE'])
def eliminar(matr_id):
    return matricula_controller.eliminar(matr_id)
