from flask import Blueprint, request, jsonify
from Services.GradoService import GradoService

grado_bp = Blueprint('grado', __name__)
service = GradoService()

@grado_bp.route('/grados', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@grado_bp.route('/grados', methods=['GET'])
@grado_bp.route('/grados/<int:id_grado>', methods=['GET'])
def read(id_grado=None):
    return jsonify(service.read(id_grado)), 200

@grado_bp.route('/grados/<int:id_grado>', methods=['PUT'])
def update(id_grado):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_grado, data)}), 200

@grado_bp.route('/grados/<int:id_grado>', methods=['DELETE'])
def delete(id_grado):
    return jsonify({"message": "Eliminado", "result": service.delete(id_grado)}), 200