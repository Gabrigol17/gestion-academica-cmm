from flask import jsonify
from Services.NivelEducativoService import NivelEducativoService


class NivelEducativoController:

    CAMPOS_REQUERIDOS = ['NIV_EDUC_NOMBRE']

    def __init__(self):
        self.nivel_educativo_service = NivelEducativoService()

    def obtener_todos(self):
        niveles = self.nivel_educativo_service.obtener_todos()
        return jsonify(niveles), 200

    def obtener_por_id(self, niv_educ_id):
        nivel = self.nivel_educativo_service.obtener_por_id(niv_educ_id)
        if nivel is None:
            return jsonify({'mensaje': 'Nivel educativo no encontrado'}), 404
        return jsonify(nivel), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        nivel = self.nivel_educativo_service.crear(data['NIV_EDUC_NOMBRE'])
        if nivel is None:
            return jsonify({'mensaje': 'No se pudo crear el nivel educativo'}), 500
        return jsonify({'mensaje': 'Nivel educativo creado exitosamente', 'nivel_educativo': nivel}), 201

    def actualizar(self, niv_educ_uuid, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        if not self.nivel_educativo_service.actualizar(data['NIV_EDUC_NOMBRE'], niv_educ_uuid):
            return jsonify({'mensaje': 'Nivel educativo no encontrado'}), 404
        return jsonify({'mensaje': 'Nivel educativo actualizado exitosamente'}), 200

    def eliminar(self, niv_educ_uuid):
        if not self.nivel_educativo_service.eliminar(niv_educ_uuid):
            return jsonify({'mensaje': 'Nivel educativo no encontrado'}), 404
        return jsonify({'mensaje': 'Nivel educativo eliminado exitosamente'}), 200
