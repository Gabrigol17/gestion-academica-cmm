from flask import jsonify
from Services.DocenteService import DocenteService


class DocenteController:

    def __init__(self):
        self.docente_service = DocenteService()

    def obtener_todos(self):
        docentes = self.docente_service.obtener_todos()
        return jsonify(docentes), 200

    def obtener_por_id(self, doc_id):
        docente = self.docente_service.obtener_por_id(doc_id)
        if docente is None:
            return jsonify({'mensaje': 'Docente no encontrado'}), 404
        return jsonify(docente), 200

    def crear(self, data):
        campos_requeridos = ['DOC_ESTADO', 'DOC_PER_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos DOC_ESTADO y DOC_PER_ID son requeridos'}), 400

        self.docente_service.crear(data['DOC_ESTADO'], data['DOC_PER_ID'])
        return jsonify({'mensaje': 'Docente creado exitosamente'}), 201

    def actualizar(self, doc_id, data):
        campos_requeridos = ['DOC_ESTADO', 'DOC_PER_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos DOC_ESTADO y DOC_PER_ID son requeridos'}), 400

        docente = self.docente_service.obtener_por_id(doc_id)
        if docente is None:
            return jsonify({'mensaje': 'Docente no encontrado'}), 404

        self.docente_service.actualizar(data['DOC_ESTADO'], data['DOC_PER_ID'], doc_id)
        return jsonify({'mensaje': 'Docente actualizado exitosamente'}), 200

    def eliminar(self, doc_id):
        docente = self.docente_service.obtener_por_id(doc_id)
        if docente is None:
            return jsonify({'mensaje': 'Docente no encontrado'}), 404

        self.docente_service.eliminar(doc_id)
        return jsonify({'mensaje': 'Docente eliminado exitosamente'}), 200
