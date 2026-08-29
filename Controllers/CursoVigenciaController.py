from flask import Blueprint, request, jsonify
from Services.CursoVigenciaService import CursoVigenciaService

curso_vigencia_bp = Blueprint('curso_vigencia', __name__)
service = CursoVigenciaService()

@curso_vigencia_bp.route('/curso-vigencias', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({"message": "Creado", "result": service.add(data)}), 201

@curso_vigencia_bp.route('/curso-vigencias', methods=['GET'])
@curso_vigencia_bp.route('/curso-vigencias/<int:id_curso_vigencia>', methods=['GET'])
def read(id_curso_vigencia=None):
    return jsonify(service.read(id_curso_vigencia)), 200

@curso_vigencia_bp.route('/curso-vigencias/<int:id_curso_vigencia>', methods=['PUT'])
def update(id_curso_vigencia):
    data = request.get_json()
    return jsonify({"message": "Actualizado", "result": service.update(id_curso_vigencia, data)}), 200

@curso_vigencia_bp.route('/curso-vigencias/<int:id_curso_vigencia>', methods=['DELETE'])
def delete(id_curso_vigencia):
    return jsonify({"message": "Eliminado", "result": service.delete(id_curso_vigencia)}), 200