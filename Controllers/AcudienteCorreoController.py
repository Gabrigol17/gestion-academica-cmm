from flask import Blueprint, request, jsonify
from Services.AcudienteEstudianteService import AcudienteEstudianteService

acudiente_estudiante_bp = Blueprint('acudiente_estudiante', __name__)
service = AcudienteEstudianteService()

@acudiente_estudiante_bp.route('/acudiente-estudiantes', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@acudiente_estudiante_bp.route('/acudiente-estudiantes', methods=['GET'])
@acudiente_estudiante_bp.route('/acudiente-estudiantes/<int:id_acudiente>/<int:id_estudiante>', methods=['GET'])
def read(id_acudiente=None, id_estudiante=None):
    return jsonify(service.read(id_acudiente, id_estudiante)), 200

@acudiente_estudiante_bp.route('/acudiente-estudiantes/<int:id_acudiente>/<int:id_estudiante>', methods=['PUT'])
def update(id_acudiente, id_estudiante):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_acudiente, id_estudiante, data)}), 200

@acudiente_estudiante_bp.route('/acudiente-estudiantes/<int:id_acudiente>/<int:id_estudiante>', methods=['DELETE'])
def delete(id_acudiente, id_estudiante):
    return jsonify({"message": "Eliminado", "result": service.delete(id_acudiente, id_estudiante)}), 200