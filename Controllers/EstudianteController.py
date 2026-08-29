from flask import Blueprint, request, jsonify
from Services.EstudianteService import EstudianteService

estudiante_bp = Blueprint('estudiante', __name__)
service = EstudianteService()

@estudiante_bp.route('/estudiantes', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@estudiante_bp.route('/estudiantes', methods=['GET'])
@estudiante_bp.route('/estudiantes/<int:id_estudiante>', methods=['GET'])
def read(id_estudiante=None):
    return jsonify(service.read(id_estudiante)), 200

@estudiante_bp.route('/estudiantes/<int:id_estudiante>', methods=['PUT'])
def update(id_estudiante):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_estudiante, data)}), 200

@estudiante_bp.route('/estudiantes/<int:id_estudiante>', methods=['DELETE'])
def delete(id_estudiante):
    return jsonify({"message": "Eliminado", "result": service.delete(id_estudiante)}), 200