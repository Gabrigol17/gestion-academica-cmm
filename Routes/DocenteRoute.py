from flask import Blueprint, request
from Controllers.DocenteController import DocenteController

docente_bp = Blueprint('docente', __name__)
docente_controller = DocenteController()


@docente_bp.route('/docentes', methods=['GET'])
def obtener_todos():
    return docente_controller.obtener_todos()


@docente_bp.route('/docentes/<int:doc_id>', methods=['GET'])
def obtener_por_id(doc_id):
    return docente_controller.obtener_por_id(doc_id)


@docente_bp.route('/docentes', methods=['POST'])
def crear():
    return docente_controller.crear(request.get_json())


@docente_bp.route('/docentes/<int:doc_id>', methods=['PUT'])
def actualizar(doc_id):
    return docente_controller.actualizar(doc_id, request.get_json())


@docente_bp.route('/docentes/<int:doc_id>', methods=['DELETE'])
def eliminar(doc_id):
    return docente_controller.eliminar(doc_id)
