from flask import Blueprint, request, jsonify
from Services.MatriculaService import MatriculaService

matricula_bp = Blueprint('matricula', __name__)
service = MatriculaService()

@matricula_bp.route('/matriculas', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@matricula_bp.route('/matriculas', methods=['GET'])
@matricula_bp.route('/matriculas/<int:id_matricula>', methods=['GET'])
def read(id_matricula=None):
    return jsonify(service.read(id_matricula)), 200

@matricula_bp.route('/matriculas/<int:id_matricula>', methods=['PUT'])
def update(id_matricula):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_matricula, data)}), 200

@matricula_bp.route('/matriculas/<int:id_matricula>', methods=['DELETE'])
def delete(id_matricula):
    return jsonify({"message": "Eliminado", "result": service.delete(id_matricula)}), 200