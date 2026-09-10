from flask import jsonify
from Services.AcudienteCorreoService import AcudienteCorreoService


class AcudienteCorreoController:

    CAMPOS_REQUERIDOS = ['ACU_CORR_ACU_ID', 'ACU_CORR_CORREO']

    def __init__(self):
        self.acudiente_correo_service = AcudienteCorreoService()

    def obtener_todos(self):
        correos = self.acudiente_correo_service.obtener_todos()
        return jsonify(correos), 200

    def obtener_por_id(self, acu_corr_id):
        correo = self.acudiente_correo_service.obtener_por_id(acu_corr_id)
        if correo is None:
            return jsonify({'mensaje': 'Correo de acudiente no encontrado'}), 404
        return jsonify(correo), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        correo = self.acudiente_correo_service.crear(data['ACU_CORR_ACU_ID'], data['ACU_CORR_CORREO'])
        if correo is None:
            return jsonify({'mensaje': 'No se pudo crear el correo de acudiente'}), 500
        return jsonify({'mensaje': 'Correo de acudiente creado exitosamente', 'acudiente_correo': correo}), 201

    def actualizar(self, acu_corr_uuid, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        if not self.acudiente_correo_service.actualizar(data['ACU_CORR_ACU_ID'], data['ACU_CORR_CORREO'], acu_corr_uuid):
            return jsonify({'mensaje': 'Correo de acudiente no encontrado'}), 404
        return jsonify({'mensaje': 'Correo de acudiente actualizado exitosamente'}), 200

    def eliminar(self, acu_corr_uuid):
        if not self.acudiente_correo_service.eliminar(acu_corr_uuid):
            return jsonify({'mensaje': 'Correo de acudiente no encontrado'}), 404
        return jsonify({'mensaje': 'Correo de acudiente eliminado exitosamente'}), 200
