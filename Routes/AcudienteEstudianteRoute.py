from flask import Blueprint, request
from Controllers.AcudienteEstudianteController import AcudienteEstudianteController

acudiente_estudiante_bp = Blueprint('acudiente_estudiante', __name__)
acudiente_estudiante_controller = AcudienteEstudianteController()


@acudiente_estudiante_bp.route('/acudientes-estudiantes', methods=['GET'])
def obtener_todos():
    return acudiente_estudiante_controller.obtener_todos()


@acudiente_estudiante_bp.route('/acudientes-estudiantes/<int:acu_est_id>', methods=['GET'])
def obtener_por_id(acu_est_id):
    return acudiente_estudiante_controller.obtener_por_id(acu_est_id)


@acudiente_estudiante_bp.route('/acudientes-estudiantes', methods=['POST'])
def crear():
    return acudiente_estudiante_controller.crear(request.get_json())


@acudiente_estudiante_bp.route('/acudientes-estudiantes/<int:acu_est_id>', methods=['PUT'])
def actualizar(acu_est_id):
    return acudiente_estudiante_controller.actualizar(acu_est_id, request.get_json())


@acudiente_estudiante_bp.route('/acudientes-estudiantes/<int:acu_est_id>', methods=['DELETE'])
def eliminar(acu_est_id):
    return acudiente_estudiante_controller.eliminar(acu_est_id)
