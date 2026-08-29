from flask import Blueprint, request, jsonify
from Services.TipoComponenteService import TipoComponenteService

tipo_componente_bp = Blueprint('tipo_componente', __name__)
service = TipoComponenteService()

@tipo_componente_bp.route('/tipos-componente', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@tipo_componente_bp.route('/tipos-componente', methods=['GET'])
@tipo_componente_bp.route('/tipos-componente/<int:id_tipo_componente>', methods=['GET'])
def read(id_tipo_componente=None):
    return jsonify(service.read(id_tipo_componente)), 200

@tipo_componente_bp.route('/tipos-componente/<int:id_tipo_componente>', methods=['PUT'])
def update(id_tipo_componente):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_tipo_componente, data)}), 200

@tipo_componente_bp.route('/tipos-componente/<int:id_tipo_componente>', methods=['DELETE'])
def delete(id_tipo_componente):
    return jsonify({"message": "Eliminado", "result": service.delete(id_tipo_componente)}), 200