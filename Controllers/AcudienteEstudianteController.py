from flask import jsonify
from Services.AcudienteEstudianteService import AcudienteEstudianteService


class AcudienteEstudianteController:

    CAMPOS_REQUERIDOS = ['ACU_EST_PARENTESCO', 'ACU_EST_ACU_ID', 'ACU_EST_EST_ID', 'ACU_EST_ESPRINCIPAL']

    def __init__(self):
        self.acudiente_estudiante_service = AcudienteEstudianteService()

    def obtener_todos(self):
        relaciones = self.acudiente_estudiante_service.obtener_todos()
        return jsonify(relaciones), 200

    def obtener_por_id(self, acu_est_id):
        relacion = self.acudiente_estudiante_service.obtener_por_id(acu_est_id)
        if relacion is None:
            return jsonify({'mensaje': 'Relación acudiente-estudiante no encontrada'}), 404
        return jsonify(relacion), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.acudiente_estudiante_service.crear(
            data['ACU_EST_PARENTESCO'],
            data['ACU_EST_ACU_ID'],
            data['ACU_EST_EST_ID'],
            data['ACU_EST_ESPRINCIPAL']
        )
        return jsonify({'mensaje': 'Relación acudiente-estudiante creada exitosamente'}), 201

    def actualizar(self, acu_est_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        relacion = self.acudiente_estudiante_service.obtener_por_id(acu_est_id)
        if relacion is None:
            return jsonify({'mensaje': 'Relación acudiente-estudiante no encontrada'}), 404

        self.acudiente_estudiante_service.actualizar(
            data['ACU_EST_PARENTESCO'],
            data['ACU_EST_ACU_ID'],
            data['ACU_EST_EST_ID'],
            data['ACU_EST_ESPRINCIPAL'],
            acu_est_id
        )
        return jsonify({'mensaje': 'Relación acudiente-estudiante actualizada exitosamente'}), 200

    def eliminar(self, acu_est_id):
        relacion = self.acudiente_estudiante_service.obtener_por_id(acu_est_id)
        if relacion is None:
            return jsonify({'mensaje': 'Relación acudiente-estudiante no encontrada'}), 404

        self.acudiente_estudiante_service.eliminar(acu_est_id)
        return jsonify({'mensaje': 'Relación acudiente-estudiante eliminada exitosamente'}), 200
