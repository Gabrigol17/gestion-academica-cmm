from flask import Blueprint, request
from Controllers.CursoVigenciaController import CursoVigenciaController

curso_vigencia_bp = Blueprint('curso_vigencia', __name__)
curso_vigencia_controller = CursoVigenciaController()


@curso_vigencia_bp.route('/cursos-vigencia', methods=['GET'])
def obtener_todos():
    return curso_vigencia_controller.obtener_todos()


@curso_vigencia_bp.route('/cursos-vigencia/<int:cur_vig_id>', methods=['GET'])
def obtener_por_id(cur_vig_id):
    return curso_vigencia_controller.obtener_por_id(cur_vig_id)


@curso_vigencia_bp.route('/cursos-vigencia', methods=['POST'])
def crear():
    return curso_vigencia_controller.crear(request.get_json())


@curso_vigencia_bp.route('/cursos-vigencia/<string:cur_vig_uuid>', methods=['PUT'])
def actualizar(cur_vig_uuid):
    return curso_vigencia_controller.actualizar(cur_vig_uuid, request.get_json())


@curso_vigencia_bp.route('/cursos-vigencia/<string:cur_vig_uuid>', methods=['DELETE'])
def eliminar(cur_vig_uuid):
    return curso_vigencia_controller.eliminar(cur_vig_uuid)
