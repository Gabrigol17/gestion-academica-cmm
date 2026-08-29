from flask import Blueprint, request, jsonify
from Services.CursoService import CursoService

curso_bp = Blueprint('curso', __name__)
service = CursoService()

@curso_bp.route('/cursos', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@curso_bp.route('/cursos', methods=['GET'])
@curso_bp.route('/cursos/<int:id_curso>', methods=['GET'])
def read(id_curso=None):
    return jsonify(service.read(id_curso)), 200

@curso_bp.route('/cursos/<int:id_curso>', methods=['PUT'])
def update(id_curso):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_curso, data)}), 200

@curso_bp.route('/cursos/<int:id_curso>', methods=['DELETE'])
def delete(id_curso):
    return jsonify({"message": "Eliminado", "result": service.delete(id_curso)}), 200