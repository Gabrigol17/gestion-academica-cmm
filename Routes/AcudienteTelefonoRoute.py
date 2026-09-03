from flask import Blueprint, request
from Controllers.AcudienteTelefonoController import AcudienteTelefonoController

acudiente_telefono_bp = Blueprint('acudiente_telefono', __name__)
acudiente_telefono_controller = AcudienteTelefonoController()


@acudiente_telefono_bp.route('/acudientes-telefonos', methods=['GET'])
def obtener_todos():
    return acudiente_telefono_controller.obtener_todos()


@acudiente_telefono_bp.route('/acudientes-telefonos/<int:acu_tel_id>', methods=['GET'])
def obtener_por_id(acu_tel_id):
    return acudiente_telefono_controller.obtener_por_id(acu_tel_id)


@acudiente_telefono_bp.route('/acudientes-telefonos', methods=['POST'])
def crear():
    return acudiente_telefono_controller.crear(request.get_json())


@acudiente_telefono_bp.route('/acudientes-telefonos/<int:acu_tel_id>', methods=['PUT'])
def actualizar(acu_tel_id):
    return acudiente_telefono_controller.actualizar(acu_tel_id, request.get_json())


@acudiente_telefono_bp.route('/acudientes-telefonos/<int:acu_tel_id>', methods=['DELETE'])
def eliminar(acu_tel_id):
    return acudiente_telefono_controller.eliminar(acu_tel_id)
