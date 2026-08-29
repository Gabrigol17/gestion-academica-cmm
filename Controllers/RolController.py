from flask import Blueprint, request, jsonify
from Services.RolService import RolService

rol_bp = Blueprint('rol', __name__)
service = RolService()

@rol_bp.route('/roles', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@rol_bp.route('/roles', methods=['GET'])
@rol_bp.route('/roles/<int:id_rol>', methods=['GET'])
def read(id_rol=None):
    return jsonify(service.read(id_rol)), 200

@rol_bp.route('/roles/<int:id_rol>', methods=['PUT'])
def update(id_rol):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_rol, data)}), 200

@rol_bp.route('/roles/<int:id_rol>', methods=['DELETE'])
def delete(id_rol):
    return jsonify({"message": "Eliminado", "result": service.delete(id_rol)}), 200