from flask import Blueprint, request, jsonify
from Services.AsignacionAcademicaService import AsignacionAcademicaService

asignacion_bp = Blueprint('asignacion_academica', __name__)
service = AsignacionAcademicaService()

@asignacion_bp.route('/asignaciones', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@asignacion_bp.route('/asignaciones', methods=['GET'])
@asignacion_bp.route('/asignaciones/<int:id_asignacion>', methods=['GET'])
def read(id_asignacion=None):
    return jsonify(service.read(id_asignacion)), 200

@asignacion_bp.route('/asignaciones/<int:id_asignacion>', methods=['PUT'])
def update(id_asignacion):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_asignacion, data)}), 200

@asignacion_bp.route('/asignaciones/<int:id_asignacion>', methods=['DELETE'])
def delete(id_asignacion):
    return jsonify({"message": "Eliminado", "result": service.delete(id_asignacion)}), 200