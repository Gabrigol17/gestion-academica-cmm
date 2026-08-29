from flask import Blueprint, request, jsonify
from Services.MateriaService import MateriaService

materia_bp = Blueprint('materia', __name__)
service = MateriaService()

@materia_bp.route('/materias', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@materia_bp.route('/materias', methods=['GET'])
@materia_bp.route('/materias/<int:id_materia>', methods=['GET'])
def read(id_materia=None):
    return jsonify(service.read(id_materia)), 200

@materia_bp.route('/materias/<int:id_materia>', methods=['PUT'])
def update(id_materia):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_materia, data)}), 200

@materia_bp.route('/materias/<int:id_materia>', methods=['DELETE'])
def delete(id_materia):
    return jsonify({"message": "Eliminado", "result": service.delete(id_materia)}), 200