from flask import Blueprint, request, jsonify
from Services.AcudienteCorreoService import AcudienteCorreoService

acudiente_correo_bp = Blueprint('acudiente_correo', __name__)
service = AcudienteCorreoService()

@acudiente_correo_bp.route('/acudiente-correos', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@acudiente_correo_bp.route('/acudiente-correos', methods=['GET'])
@acudiente_correo_bp.route('/acudiente-correos/<int:id_acudiente_correo>', methods=['GET'])
def read(id_acudiente_correo=None):
    return jsonify(service.read(id_acudiente_correo)), 200

@acudiente_correo_bp.route('/acudiente-correos/<int:id_acudiente_correo>', methods=['PUT'])
def update(id_acudiente_correo):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_acudiente_correo, data)}), 200

@acudiente_correo_bp.route('/acudiente-correos/<int:id_acudiente_correo>', methods=['DELETE'])
def delete(id_acudiente_correo):
    return jsonify({"message": "Eliminado", "result": service.delete(id_acudiente_correo)}), 200