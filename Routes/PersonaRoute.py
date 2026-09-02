from flask import Blueprint, request
from Controllers.PersonaController import PersonaController

persona_bp = Blueprint('persona', __name__)
persona_controller = PersonaController()


@persona_bp.route('/personas', methods=['GET'])
def obtener_todos():
    return persona_controller.obtener_todos()


@persona_bp.route('/personas/<int:per_id>', methods=['GET'])
def obtener_por_id(per_id):
    return persona_controller.obtener_por_id(per_id)


@persona_bp.route('/personas', methods=['POST'])
def crear():
    return persona_controller.crear(request.get_json())


@persona_bp.route('/personas/<int:per_id>', methods=['PUT'])
def actualizar(per_id):
    return persona_controller.actualizar(per_id, request.get_json())


@persona_bp.route('/personas/<int:per_id>', methods=['DELETE'])
def eliminar(per_id):
    return persona_controller.eliminar(per_id)
