from flask import Blueprint, request
from Controllers.PeriodoAcademicoController import PeriodoAcademicoController

periodo_academico_bp = Blueprint('periodo_academico', __name__)
periodo_academico_controller = PeriodoAcademicoController()


@periodo_academico_bp.route('/periodos-academicos', methods=['GET'])
def obtener_todos():
    return periodo_academico_controller.obtener_todos()


@periodo_academico_bp.route('/periodos-academicos/<int:per_aca_id>', methods=['GET'])
def obtener_por_id(per_aca_id):
    return periodo_academico_controller.obtener_por_id(per_aca_id)


@periodo_academico_bp.route('/periodos-academicos', methods=['POST'])
def crear():
    return periodo_academico_controller.crear(request.get_json())


@periodo_academico_bp.route('/periodos-academicos/<int:per_aca_id>', methods=['PUT'])
def actualizar(per_aca_id):
    return periodo_academico_controller.actualizar(per_aca_id, request.get_json())


@periodo_academico_bp.route('/periodos-academicos/<int:per_aca_id>', methods=['DELETE'])
def eliminar(per_aca_id):
    return periodo_academico_controller.eliminar(per_aca_id)
