from flask import Blueprint, request
from Controllers.GradoController import GradoController

grado_bp = Blueprint('grado', __name__)
grado_controller = GradoController()


@grado_bp.route('/grados', methods=['GET'])
def obtener_todos():
    return grado_controller.obtener_todos()


@grado_bp.route('/grados/<int:grad_id>', methods=['GET'])
def obtener_por_id(grad_id):
    return grado_controller.obtener_por_id(grad_id)


@grado_bp.route('/grados', methods=['POST'])
def crear():
    return grado_controller.crear(request.get_json())


@grado_bp.route('/grados/<string:grad_uuid>', methods=['PUT'])
def actualizar(grad_uuid):
    return grado_controller.actualizar(grad_uuid, request.get_json())


@grado_bp.route('/grados/<string:grad_uuid>', methods=['DELETE'])
def eliminar(grad_uuid):
    return grado_controller.eliminar(grad_uuid)
