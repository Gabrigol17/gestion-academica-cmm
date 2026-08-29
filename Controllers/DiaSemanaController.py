from flask import Blueprint, request, jsonify
from Services.DiaSemanaService import DiaSemanaService

dia_semana_bp = Blueprint('dia_semana', __name__)
service = DiaSemanaService()

@dia_semana_bp.route('/dias-semana', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@dia_semana_bp.route('/dias-semana', methods=['GET'])
@dia_semana_bp.route('/dias-semana/<int:id_dia>', methods=['GET'])
def read(id_dia=None):
    return jsonify(service.read(id_dia)), 200

@dia_semana_bp.route('/dias-semana/<int:id_dia>', methods=['PUT'])
def update(id_dia):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_dia, data)}), 200

@dia_semana_bp.route('/dias-semana/<int:id_dia>', methods=['DELETE'])
def delete(id_dia):
    return jsonify({"message": "Eliminado", "result": service.delete(id_dia)}), 200