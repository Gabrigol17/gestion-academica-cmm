from flask import Blueprint, request
from Controllers.ResultadoEvaluativoController import ResultadoEvaluativoController

resultado_evaluativo_bp = Blueprint('resultado_evaluativo', __name__)
resultado_evaluativo_controller = ResultadoEvaluativoController()


@resultado_evaluativo_bp.route('/resultados-evaluativos', methods=['GET'])
def obtener_todos():
    return resultado_evaluativo_controller.obtener_todos()


@resultado_evaluativo_bp.route('/resultados-evaluativos/<int:res_eva_id>', methods=['GET'])
def obtener_por_id(res_eva_id):
    return resultado_evaluativo_controller.obtener_por_id(res_eva_id)


@resultado_evaluativo_bp.route('/resultados-evaluativos', methods=['POST'])
def crear():
    return resultado_evaluativo_controller.crear(request.get_json())


@resultado_evaluativo_bp.route('/resultados-evaluativos/<int:res_eva_id>', methods=['PUT'])
def actualizar(res_eva_id):
    return resultado_evaluativo_controller.actualizar(res_eva_id, request.get_json())


@resultado_evaluativo_bp.route('/resultados-evaluativos/<int:res_eva_id>', methods=['DELETE'])
def eliminar(res_eva_id):
    return resultado_evaluativo_controller.eliminar(res_eva_id)
