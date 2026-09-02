from flask import Blueprint, request
from Controllers.ActividadEvaluativaController import ActividadEvaluativaController

actividad_evaluativa_bp = Blueprint('actividad_evaluativa', __name__)
actividad_evaluativa_controller = ActividadEvaluativaController()


@actividad_evaluativa_bp.route('/actividades-evaluativas', methods=['GET'])
def obtener_todos():
    return actividad_evaluativa_controller.obtener_todos()


@actividad_evaluativa_bp.route('/actividades-evaluativas/<int:act_eva_id>', methods=['GET'])
def obtener_por_id(act_eva_id):
    return actividad_evaluativa_controller.obtener_por_id(act_eva_id)


@actividad_evaluativa_bp.route('/actividades-evaluativas', methods=['POST'])
def crear():
    return actividad_evaluativa_controller.crear(request.get_json())


@actividad_evaluativa_bp.route('/actividades-evaluativas/<int:act_eva_id>', methods=['PUT'])
def actualizar(act_eva_id):
    return actividad_evaluativa_controller.actualizar(act_eva_id, request.get_json())


@actividad_evaluativa_bp.route('/actividades-evaluativas/<int:act_eva_id>', methods=['DELETE'])
def eliminar(act_eva_id):
    return actividad_evaluativa_controller.eliminar(act_eva_id)
