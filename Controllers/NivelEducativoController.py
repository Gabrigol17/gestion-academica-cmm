from flask import Blueprint, request, jsonify
from Services.NivelEducativoService import NivelEducativoService

nivel_educativo_bp = Blueprint('nivel_educativo', __name__)
service = NivelEducativoService()

@nivel_educativo_bp.route('/niveles-educativos', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@nivel_educativo_bp.route('/niveles-educativos', methods=['GET'])
@nivel_educativo_bp.route('/niveles-educativos/<int:id_nivel>', methods=['GET'])
def read(id_nivel=None):
    return jsonify(service.read(id_nivel)), 200

@nivel_educativo_bp.route('/niveles-educativos/<int:id_nivel>', methods=['PUT'])
def update(id_nivel):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_nivel, data)}), 200

@nivel_educativo_bp.route('/niveles-educativos/<int:id_nivel>', methods=['DELETE'])
def delete(id_nivel):
    return jsonify({"message": "Eliminado", "result": service.delete(id_nivel)}), 200