from flask import Blueprint, request
from Controllers.DetalleHorarioController import DetalleHorarioController

detalle_horario_bp = Blueprint('detalle_horario', __name__)
detalle_horario_controller = DetalleHorarioController()


@detalle_horario_bp.route('/detalles-horario', methods=['GET'])
def obtener_todos():
    return detalle_horario_controller.obtener_todos()


@detalle_horario_bp.route('/detalles-horario/<int:det_hor_id>', methods=['GET'])
def obtener_por_id(det_hor_id):
    return detalle_horario_controller.obtener_por_id(det_hor_id)


@detalle_horario_bp.route('/detalles-horario', methods=['POST'])
def crear():
    return detalle_horario_controller.crear(request.get_json())


@detalle_horario_bp.route('/detalles-horario/<int:det_hor_id>', methods=['PUT'])
def actualizar(det_hor_id):
    return detalle_horario_controller.actualizar(det_hor_id, request.get_json())


@detalle_horario_bp.route('/detalles-horario/<int:det_hor_id>', methods=['DELETE'])
def eliminar(det_hor_id):
    return detalle_horario_controller.eliminar(det_hor_id)
