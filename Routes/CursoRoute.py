from flask import Blueprint, request
from Controllers.CursoController import CursoController

curso_bp = Blueprint('curso', __name__)
curso_controller = CursoController()


@curso_bp.route('/cursos', methods=['GET'])
def obtener_todos():
    return curso_controller.obtener_todos()


@curso_bp.route('/cursos/<int:cur_id>', methods=['GET'])
def obtener_por_id(cur_id):
    return curso_controller.obtener_por_id(cur_id)


@curso_bp.route('/cursos', methods=['POST'])
def crear():
    return curso_controller.crear(request.get_json())


@curso_bp.route('/cursos/<int:cur_id>', methods=['PUT'])
def actualizar(cur_id):
    return curso_controller.actualizar(cur_id, request.get_json())


@curso_bp.route('/cursos/<int:cur_id>', methods=['DELETE'])
def eliminar(cur_id):
    return curso_controller.eliminar(cur_id)
