from flask import Blueprint, request
from Controllers.ComponenteEvaluativoController import ComponenteEvaluativoController

componente_evaluativo_bp = Blueprint('componente_evaluativo', __name__)
componente_evaluativo_controller = ComponenteEvaluativoController()


@componente_evaluativo_bp.route('/componentes-evaluativos', methods=['GET'])
def obtener_todos():
    return componente_evaluativo_controller.obtener_todos()


@componente_evaluativo_bp.route('/componentes-evaluativos/<int:com_eva_id>', methods=['GET'])
def obtener_por_id(com_eva_id):
    return componente_evaluativo_controller.obtener_por_id(com_eva_id)


@componente_evaluativo_bp.route('/componentes-evaluativos', methods=['POST'])
def crear():
    return componente_evaluativo_controller.crear(request.get_json())


@componente_evaluativo_bp.route('/componentes-evaluativos/<int:com_eva_id>', methods=['PUT'])
def actualizar(com_eva_id):
    return componente_evaluativo_controller.actualizar(com_eva_id, request.get_json())


@componente_evaluativo_bp.route('/componentes-evaluativos/<int:com_eva_id>', methods=['DELETE'])
def eliminar(com_eva_id):
    return componente_evaluativo_controller.eliminar(com_eva_id)
