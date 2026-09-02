from flask import Blueprint, request
from Controllers.TipoComponenteController import TipoComponenteController

tipo_componente_bp = Blueprint('tipo_componente', __name__)
tipo_componente_controller = TipoComponenteController()


@tipo_componente_bp.route('/tipos-componente', methods=['GET'])
def obtener_todos():
    return tipo_componente_controller.obtener_todos()


@tipo_componente_bp.route('/tipos-componente/<int:tipo_comp_id>', methods=['GET'])
def obtener_por_id(tipo_comp_id):
    return tipo_componente_controller.obtener_por_id(tipo_comp_id)


@tipo_componente_bp.route('/tipos-componente', methods=['POST'])
def crear():
    return tipo_componente_controller.crear(request.get_json())


@tipo_componente_bp.route('/tipos-componente/<int:tipo_comp_id>', methods=['PUT'])
def actualizar(tipo_comp_id):
    return tipo_componente_controller.actualizar(tipo_comp_id, request.get_json())


@tipo_componente_bp.route('/tipos-componente/<int:tipo_comp_id>', methods=['DELETE'])
def eliminar(tipo_comp_id):
    return tipo_componente_controller.eliminar(tipo_comp_id)
