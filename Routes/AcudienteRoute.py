from flask import Blueprint, request
from Controllers.AcudienteController import AcudienteController

acudiente_bp = Blueprint('acudiente', __name__)
acudiente_controller = AcudienteController()


@acudiente_bp.route('/acudientes', methods=['GET'])
def obtener_todos():
    return acudiente_controller.obtener_todos()


@acudiente_bp.route('/acudientes/<int:acu_id>', methods=['GET'])
def obtener_por_id(acu_id):
    return acudiente_controller.obtener_por_id(acu_id)


@acudiente_bp.route('/acudientes', methods=['POST'])
def crear():
    return acudiente_controller.crear(request.get_json())


@acudiente_bp.route('/acudientes/<int:acu_id>', methods=['PUT'])
def actualizar(acu_id):
    return acudiente_controller.actualizar(acu_id, request.get_json())


@acudiente_bp.route('/acudientes/<int:acu_id>', methods=['DELETE'])
def eliminar(acu_id):
    return acudiente_controller.eliminar(acu_id)
