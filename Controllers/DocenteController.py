from flask import Blueprint, request, jsonify
from Services.DocenteService import DocenteService

docente_bp = Blueprint('docente', __name__)
service = DocenteService()

@docente_bp.route('/docentes', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@docente_bp.route('/docentes', methods=['GET'])
@docente_bp.route('/docentes/<int:id_docente>', methods=['GET'])
def read(id_docente=None):
    return jsonify(service.read(id_docente)), 200

@docente_bp.route('/docentes/<int:id_docente>', methods=['PUT'])
def update(id_docente):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_docente, data)}), 200

@docente_bp.route('/docentes/<int:id_docente>', methods=['DELETE'])
def delete(id_docente):
    return jsonify({"message": "Eliminado", "result": service.delete(id_docente)}), 200