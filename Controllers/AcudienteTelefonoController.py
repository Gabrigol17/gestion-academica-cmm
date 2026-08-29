from flask import Blueprint, request, jsonify
from Services.AcudienteTelefonoService import AcudienteTelefonoService

acudiente_telefono_bp = Blueprint('acudiente_telefono', __name__)
service = AcudienteTelefonoService()

@acudiente_telefono_bp.route('/acudiente-telefonos', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@acudiente_telefono_bp.route('/acudiente-telefonos', methods=['GET'])
@acudiente_telefono_bp.route('/acudiente-telefonos/<int:id_acudiente_telefono>', methods=['GET'])
def read(id_acudiente_telefono=None):
    return jsonify(service.read(id_acudiente_telefono)), 200

@acudiente_telefono_bp.route('/acudiente-telefonos/<int:id_acudiente_telefono>', methods=['PUT'])
def update(id_acudiente_telefono):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_acudiente_telefono, data)}), 200

@acudiente_telefono_bp.route('/acudiente-telefonos/<int:id_acudiente_telefono>', methods=['DELETE'])
def delete(id_acudiente_telefono):
    return jsonify({"message": "Eliminado", "result": service.delete(id_acudiente_telefono)}), 200