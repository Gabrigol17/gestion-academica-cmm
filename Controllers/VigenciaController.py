from flask import jsonify
from Services.VigenciaService import VigenciaService


class VigenciaController:

    CAMPOS_REQUERIDOS = ['VIG_AÑO']

    def __init__(self):
        self.vigencia_service = VigenciaService()

    def obtener_todos(self):
        vigencias = self.vigencia_service.obtener_todos()
        return jsonify(vigencias), 200

    def obtener_por_id(self, vig_id):
        vigencia = self.vigencia_service.obtener_por_id(vig_id)
        if vigencia is None:
            return jsonify({'mensaje': 'Vigencia no encontrada'}), 404
        return jsonify(vigencia), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        vigencia = self.vigencia_service.crear(data['VIG_AÑO'])
        if vigencia is None:
            return jsonify({'mensaje': 'No se pudo crear la vigencia'}), 500
        return jsonify({'mensaje': 'Vigencia creada exitosamente', 'vigencia': vigencia}), 201

    def actualizar(self, vig_uuid, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        if not self.vigencia_service.actualizar(data['VIG_AÑO'], vig_uuid):
            return jsonify({'mensaje': 'Vigencia no encontrada'}), 404
        return jsonify({'mensaje': 'Vigencia actualizada exitosamente'}), 200

    def eliminar(self, vig_uuid):
        if not self.vigencia_service.eliminar(vig_uuid):
            return jsonify({'mensaje': 'Vigencia no encontrada'}), 404
        return jsonify({'mensaje': 'Vigencia eliminada exitosamente'}), 200
