from flask import Blueprint, request
from Controllers.AcudienteCorreoController import AcudienteCorreoController

acudiente_correo_bp = Blueprint('acudiente_correo', __name__)
acudiente_correo_controller = AcudienteCorreoController()


@acudiente_correo_bp.route('/acudientes-correos', methods=['GET'])
def obtener_todos():
    return acudiente_correo_controller.obtener_todos()


@acudiente_correo_bp.route('/acudientes-correos/<int:acu_corr_id>', methods=['GET'])
def obtener_por_id(acu_corr_id):
    return acudiente_correo_controller.obtener_por_id(acu_corr_id)


@acudiente_correo_bp.route('/acudientes-correos', methods=['POST'])
def crear():
    return acudiente_correo_controller.crear(request.get_json())


@acudiente_correo_bp.route('/acudientes-correos/<int:acu_corr_id>', methods=['PUT'])
def actualizar(acu_corr_id):
    return acudiente_correo_controller.actualizar(acu_corr_id, request.get_json())


@acudiente_correo_bp.route('/acudientes-correos/<int:acu_corr_id>', methods=['DELETE'])
def eliminar(acu_corr_id):
    return acudiente_correo_controller.eliminar(acu_corr_id)
