from flask import Blueprint, request, jsonify
from Services.AcudienteService import AcudienteService

acudiente_bp = Blueprint('acudiente', __name__)
service = AcudienteService()

@acudiente_bp.route('/acudientes', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@acudiente_bp.route('/acudientes', methods=['GET'])
@acudiente_bp.route('/acudientes/<int:id_acudiente>', methods=['GET'])
def read(id_acudiente=None):
    return jsonify(service.read(id_acudiente)), 200

@acudiente_bp.route('/acudientes/<int:id_acudiente>', methods=['PUT'])
def update(id_acudiente):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_acudiente, data)}), 200

@acudiente_bp.route('/acudientes/<int:id_acudiente>', methods=['DELETE'])
def delete(id_acudiente):
    return jsonify({"message": "Eliminado", "result": service.delete(id_acudiente)}), 200