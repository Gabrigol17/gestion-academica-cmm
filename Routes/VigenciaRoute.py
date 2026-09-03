from flask import Blueprint, request
from Controllers.VigenciaController import VigenciaController

vigencia_bp = Blueprint('vigencia', __name__)
vigencia_controller = VigenciaController()


@vigencia_bp.route('/vigencias', methods=['GET'])
def obtener_todos():
    return vigencia_controller.obtener_todos()


@vigencia_bp.route('/vigencias/<int:vig_id>', methods=['GET'])
def obtener_por_id(vig_id):
    return vigencia_controller.obtener_por_id(vig_id)


@vigencia_bp.route('/vigencias', methods=['POST'])
def crear():
    return vigencia_controller.crear(request.get_json())


@vigencia_bp.route('/vigencias/<int:vig_id>', methods=['PUT'])
def actualizar(vig_id):
    return vigencia_controller.actualizar(vig_id, request.get_json())


@vigencia_bp.route('/vigencias/<int:vig_id>', methods=['DELETE'])
def eliminar(vig_id):
    return vigencia_controller.eliminar(vig_id)
