from flask import Blueprint, request
from Controllers.RolController import RolController

rol_bp = Blueprint('rol', __name__)
rol_controller = RolController()


@rol_bp.route('/roles', methods=['GET'])
def obtener_todos():
    return rol_controller.obtener_todos()


@rol_bp.route('/roles/<int:rol_id>', methods=['GET'])
def obtener_por_id(rol_id):
    return rol_controller.obtener_por_id(rol_id)


@rol_bp.route('/roles', methods=['POST'])
def crear():
    return rol_controller.crear(request.get_json())


@rol_bp.route('/roles/<int:rol_id>', methods=['PUT'])
def actualizar(rol_id):
    return rol_controller.actualizar(rol_id, request.get_json())


@rol_bp.route('/roles/<int:rol_id>', methods=['DELETE'])
def eliminar(rol_id):
    return rol_controller.eliminar(rol_id)
