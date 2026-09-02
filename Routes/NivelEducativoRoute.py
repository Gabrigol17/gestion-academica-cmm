from flask import Blueprint, request
from Controllers.NivelEducativoController import NivelEducativoController

nivel_educativo_bp = Blueprint('nivel_educativo', __name__)
nivel_educativo_controller = NivelEducativoController()


@nivel_educativo_bp.route('/niveles-educativos', methods=['GET'])
def obtener_todos():
    return nivel_educativo_controller.obtener_todos()


@nivel_educativo_bp.route('/niveles-educativos/<int:niv_educ_id>', methods=['GET'])
def obtener_por_id(niv_educ_id):
    return nivel_educativo_controller.obtener_por_id(niv_educ_id)


@nivel_educativo_bp.route('/niveles-educativos', methods=['POST'])
def crear():
    return nivel_educativo_controller.crear(request.get_json())


@nivel_educativo_bp.route('/niveles-educativos/<int:niv_educ_id>', methods=['PUT'])
def actualizar(niv_educ_id):
    return nivel_educativo_controller.actualizar(niv_educ_id, request.get_json())


@nivel_educativo_bp.route('/niveles-educativos/<int:niv_educ_id>', methods=['DELETE'])
def eliminar(niv_educ_id):
    return nivel_educativo_controller.eliminar(niv_educ_id)
