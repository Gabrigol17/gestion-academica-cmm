from flask import Blueprint, request, jsonify
from Services.ComponenteEvaluativoService import ComponenteEvaluativoService

componente_bp = Blueprint('componente_evaluativo', __name__)
service = ComponenteEvaluativoService()

@componente_bp.route('/componentes', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@componente_bp.route('/componentes', methods=['GET'])
@componente_bp.route('/componentes/<int:id_componente>', methods=['GET'])
def read(id_componente=None):
    return jsonify(service.read(id_componente)), 200

@componente_bp.route('/componentes/<int:id_componente>', methods=['PUT'])
def update(id_componente):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_componente, data)}), 200

@componente_bp.route('/componentes/<int:id_componente>', methods=['DELETE'])
def delete(id_componente):
    return jsonify({"message": "Eliminado", "result": service.delete(id_componente)}), 200