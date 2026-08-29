from flask import Blueprint, request, jsonify
from Services.DetalleHorarioService import DetalleHorarioService

detalle_horario_bp = Blueprint('detalle_horario', __name__)
service = DetalleHorarioService()

@detalle_horario_bp.route('/detalle-horarios', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@detalle_horario_bp.route('/detalle-horarios', methods=['GET'])
@detalle_horario_bp.route('/detalle-horarios/<int:id_detalle_horario>', methods=['GET'])
def read(id_detalle_horario=None):
    return jsonify(service.read(id_detalle_horario)), 200

@detalle_horario_bp.route('/detalle-horarios/<int:id_detalle_horario>', methods=['PUT'])
def update(id_detalle_horario):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_detalle_horario, data)}), 200

@detalle_horario_bp.route('/detalle-horarios/<int:id_detalle_horario>', methods=['DELETE'])
def delete(id_detalle_horario):
    return jsonify({"message": "Eliminado", "result": service.delete(id_detalle_horario)}), 200