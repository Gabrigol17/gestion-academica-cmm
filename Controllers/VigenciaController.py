from flask import Blueprint, request, jsonify
from Services.VigenciaService import VigenciaService

vigencia_bp = Blueprint('vigencia', __name__)
service = VigenciaService()

@vigencia_bp.route('/vigencias', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@vigencia_bp.route('/vigencias', methods=['GET'])
@vigencia_bp.route('/vigencias/<int:id_vigencia>', methods=['GET'])
def read(id_vigencia=None):
    return jsonify(service.read(id_vigencia)), 200

@vigencia_bp.route('/vigencias/<int:id_vigencia>', methods=['PUT'])
def update(id_vigencia):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_vigencia, data)}), 200

@vigencia_bp.route('/vigencias/<int:id_vigencia>', methods=['DELETE'])
def delete(id_vigencia):
    return jsonify({"message": "Eliminado", "result": service.delete(id_vigencia)}), 200