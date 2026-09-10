from flask import jsonify
from Services.DiaSemanaService import DiaSemanaService


class DiaSemanaController:

    CAMPOS_REQUERIDOS = ['DIA_SEM_DIA']

    def __init__(self):
        self.dia_semana_service = DiaSemanaService()

    def obtener_todos(self):
        dias = self.dia_semana_service.obtener_todos()
        return jsonify(dias), 200

    def obtener_por_id(self, dia_sem_id):
        dia = self.dia_semana_service.obtener_por_id(dia_sem_id)
        if dia is None:
            return jsonify({'mensaje': 'Día de semana no encontrado'}), 404
        return jsonify(dia), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        dia = self.dia_semana_service.crear(data['DIA_SEM_DIA'])
        if dia is None:
            return jsonify({'mensaje': 'No se pudo crear el día de semana'}), 500
        return jsonify({'mensaje': 'Día de semana creado exitosamente', 'dia_semana': dia}), 201

    def actualizar(self, dia_sem_uuid, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        if not self.dia_semana_service.actualizar(data['DIA_SEM_DIA'], dia_sem_uuid):
            return jsonify({'mensaje': 'Día de semana no encontrado'}), 404
        return jsonify({'mensaje': 'Día de semana actualizada exitosamente'}), 200

    def eliminar(self, dia_sem_uuid):
        if not self.dia_semana_service.eliminar(dia_sem_uuid):
            return jsonify({'mensaje': 'Día de semana no encontrado'}), 404
        return jsonify({'mensaje': 'Día de semana eliminado exitosamente'}), 200
