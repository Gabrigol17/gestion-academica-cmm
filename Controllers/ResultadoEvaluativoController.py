from flask import Blueprint, request, jsonify
from Services.ResultadoEvaluativoService import ResultadoEvaluativoService

resultado_evaluativo_bp = Blueprint('resultado_evaluativo', __name__)
service = ResultadoEvaluativoService()

@resultado_evaluativo_bp.route('/resultados-evaluativos', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@resultado_evaluativo_bp.route('/resultados-evaluativos', methods=['GET'])
@resultado_evaluativo_bp.route('/resultados-evaluativos/<int:id_resultado>', methods=['GET'])
def read(id_resultado=None):
    return jsonify(service.read(id_resultado)), 200

@resultado_evaluativo_bp.route('/resultados-evaluativos/<int:id_resultado>', methods=['PUT'])
def update(id_resultado):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_resultado, data)}), 200

@resultado_evaluativo_bp.route('/resultados-evaluativos/<int:id_resultado>', methods=['DELETE'])
def delete(id_resultado):
    return jsonify({"message": "Eliminado", "result": service.delete(id_resultado)}), 200