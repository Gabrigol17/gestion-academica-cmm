from flask import Blueprint, request, jsonify
from Services.PersonaService import PersonaService

persona_bp = Blueprint('persona', __name__)
service = PersonaService()

@persona_bp.route('/personas', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@persona_bp.route('/personas', methods=['GET'])
@persona_bp.route('/personas/<int:id_persona>', methods=['GET'])
def read(id_persona=None):
    return jsonify(service.read(id_persona)), 200

@persona_bp.route('/personas/<int:id_persona>', methods=['PUT'])
def update(id_persona):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_persona, data)}), 200

@persona_bp.route('/personas/<int:id_persona>', methods=['DELETE'])
def delete(id_persona):
    return jsonify({"message": "Eliminado", "result": service.delete(id_persona)}), 200