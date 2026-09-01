from flask import jsonify
from Services.EstudianteService import EstudianteService


class EstudianteController:

    CAMPOS_REQUERIDOS = ['EST_ESTADO_INSTITUCIONAL', 'EST_PER_ID']

    def __init__(self):
        self.estudiante_service = EstudianteService()

    def obtener_todos(self):
        estudiantes = self.estudiante_service.obtener_todos()
        return jsonify(estudiantes), 200

    def obtener_por_id(self, est_id):
        estudiante = self.estudiante_service.obtener_por_id(est_id)
        if estudiante is None:
            return jsonify({'mensaje': 'Estudiante no encontrado'}), 404
        return jsonify(estudiante), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.estudiante_service.crear(data['EST_ESTADO_INSTITUCIONAL'], data['EST_PER_ID'])
        return jsonify({'mensaje': 'Estudiante creado exitosamente'}), 201

    def actualizar(self, est_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        estudiante = self.estudiante_service.obtener_por_id(est_id)
        if estudiante is None:
            return jsonify({'mensaje': 'Estudiante no encontrado'}), 404

        self.estudiante_service.actualizar(data['EST_ESTADO_INSTITUCIONAL'], data['EST_PER_ID'], est_id)
        return jsonify({'mensaje': 'Estudiante actualizado exitosamente'}), 200

    def eliminar(self, est_id):
        estudiante = self.estudiante_service.obtener_por_id(est_id)
        if estudiante is None:
            return jsonify({'mensaje': 'Estudiante no encontrado'}), 404

        self.estudiante_service.eliminar(est_id)
        return jsonify({'mensaje': 'Estudiante eliminado exitosamente'}), 200
