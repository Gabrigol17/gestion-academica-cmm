from flask import Blueprint, request
from Controllers.AsignacionAcademicaController import AsignacionAcademicaController

asignacion_academica_bp = Blueprint('asignacion_academica', __name__)
asignacion_academica_controller = AsignacionAcademicaController()


@asignacion_academica_bp.route('/asignaciones-academicas', methods=['GET'])
def obtener_todos():
    return asignacion_academica_controller.obtener_todos()


@asignacion_academica_bp.route('/asignaciones-academicas/<int:asig_aca_id>', methods=['GET'])
def obtener_por_id(asig_aca_id):
    return asignacion_academica_controller.obtener_por_id(asig_aca_id)


@asignacion_academica_bp.route('/asignaciones-academicas', methods=['POST'])
def crear():
    return asignacion_academica_controller.crear(request.get_json())


@asignacion_academica_bp.route('/asignaciones-academicas/<int:asig_aca_id>', methods=['PUT'])
def actualizar(asig_aca_id):
    return asignacion_academica_controller.actualizar(asig_aca_id, request.get_json())


@asignacion_academica_bp.route('/asignaciones-academicas/<int:asig_aca_id>', methods=['DELETE'])
def eliminar(asig_aca_id):
    return asignacion_academica_controller.eliminar(asig_aca_id)
