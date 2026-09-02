from flask import Blueprint, request
from Controllers.EstudianteController import EstudianteController

estudiante_bp = Blueprint('estudiante', __name__)
estudiante_controller = EstudianteController()


@estudiante_bp.route('/estudiantes', methods=['GET'])
def obtener_todos():
    return estudiante_controller.obtener_todos()


@estudiante_bp.route('/estudiantes/<int:est_id>', methods=['GET'])
def obtener_por_id(est_id):
    return estudiante_controller.obtener_por_id(est_id)


@estudiante_bp.route('/estudiantes', methods=['POST'])
def crear():
    return estudiante_controller.crear(request.get_json())


@estudiante_bp.route('/estudiantes/<int:est_id>', methods=['PUT'])
def actualizar(est_id):
    return estudiante_controller.actualizar(est_id, request.get_json())


@estudiante_bp.route('/estudiantes/<int:est_id>', methods=['DELETE'])
def eliminar(est_id):
    return estudiante_controller.eliminar(est_id)
