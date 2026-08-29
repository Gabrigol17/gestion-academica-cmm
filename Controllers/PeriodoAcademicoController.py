from flask import Blueprint, request, jsonify
from Services.PeriodoAcademicoService import PeriodoAcademicoService

periodo_academico_bp = Blueprint('periodo_academico', __name__)
service = PeriodoAcademicoService()

@periodo_academico_bp.route('/periodos-academicos', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@periodo_academico_bp.route('/periodos-academicos', methods=['GET'])
@periodo_academico_bp.route('/periodos-academicos/<int:id_periodo>', methods=['GET'])
def read(id_periodo=None):
    return jsonify(service.read(id_periodo)), 200

@periodo_academico_bp.route('/periodos-academicos/<int:id_periodo>', methods=['PUT'])
def update(id_periodo):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_periodo, data)}), 200

@periodo_academico_bp.route('/periodos-academicos/<int:id_periodo>', methods=['DELETE'])
def delete(id_periodo):
    return jsonify({"message": "Eliminado", "result": service.delete(id_periodo)}), 200