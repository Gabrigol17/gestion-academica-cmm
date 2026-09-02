from flask import Blueprint, request
from Controllers.MateriaController import MateriaController

materia_bp = Blueprint('materia', __name__)
materia_controller = MateriaController()


@materia_bp.route('/materias', methods=['GET'])
def obtener_todos():
    return materia_controller.obtener_todos()


@materia_bp.route('/materias/<int:mat_id>', methods=['GET'])
def obtener_por_id(mat_id):
    return materia_controller.obtener_por_id(mat_id)


@materia_bp.route('/materias', methods=['POST'])
def crear():
    return materia_controller.crear(request.get_json())


@materia_bp.route('/materias/<int:mat_id>', methods=['PUT'])
def actualizar(mat_id):
    return materia_controller.actualizar(mat_id, request.get_json())


@materia_bp.route('/materias/<int:mat_id>', methods=['DELETE'])
def eliminar(mat_id):
    return materia_controller.eliminar(mat_id)
