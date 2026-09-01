from flask import jsonify
from Services.AcudienteCorreoService import AcudienteCorreoService


class AcudienteCorreoController:

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
        campos_requeridos = ['ACU_CORR_ACU_ID', 'ACU_CORR_CORREO']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ACU_CORR_ACU_ID y ACU_CORR_CORREO son requeridos'}), 400

        self.acudiente_correo_service.crear(data['ACU_CORR_ACU_ID'], data['ACU_CORR_CORREO'])
        return jsonify({'mensaje': 'Correo de acudiente creado exitosamente'}), 201

    def actualizar(self, acu_corr_id, data):
        campos_requeridos = ['ACU_CORR_ACU_ID', 'ACU_CORR_CORREO']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ACU_CORR_ACU_ID y ACU_CORR_CORREO son requeridos'}), 400

        correo = self.acudiente_correo_service.obtener_por_id(acu_corr_id)
        if correo is None:
            return jsonify({'mensaje': 'Correo de acudiente no encontrado'}), 404

        self.acudiente_correo_service.actualizar(data['ACU_CORR_ACU_ID'], data['ACU_CORR_CORREO'], acu_corr_id)
        return jsonify({'mensaje': 'Correo de acudiente actualizado exitosamente'}), 200

    def eliminar(self, acu_corr_id):
        correo = self.acudiente_correo_service.obtener_por_id(acu_corr_id)
        if correo is None:
            return jsonify({'mensaje': 'Correo de acudiente no encontrado'}), 404

        self.acudiente_correo_service.eliminar(acu_corr_id)
        return jsonify({'mensaje': 'Correo de acudiente eliminado exitosamente'}), 200
