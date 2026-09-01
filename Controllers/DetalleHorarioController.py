from flask import jsonify
from Services.DetalleHorarioService import DetalleHorarioService


class DetalleHorarioController:

    CAMPOS_REQUERIDOS = ['DET_HOR_ASIG_ACA_ID', 'DET_HOR_DIA_SEM_ID', 'DET_HOR_HORA_INICIO', 'DET_HOR_HORA_FIN']

    def __init__(self):
        self.detalle_horario_service = DetalleHorarioService()

    def obtener_todos(self):
        horarios = self.detalle_horario_service.obtener_todos()
        return jsonify(horarios), 200

    def obtener_por_id(self, det_hor_id):
        horario = self.detalle_horario_service.obtener_por_id(det_hor_id)
        if horario is None:
            return jsonify({'mensaje': 'Detalle de horario no encontrado'}), 404
        return jsonify(horario), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.detalle_horario_service.crear(
            data['DET_HOR_ASIG_ACA_ID'],
            data['DET_HOR_DIA_SEM_ID'],
            data['DET_HOR_HORA_INICIO'],
            data['DET_HOR_HORA_FIN']
        )
        return jsonify({'mensaje': 'Detalle de horario creado exitosamente'}), 201

    def actualizar(self, det_hor_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        horario = self.detalle_horario_service.obtener_por_id(det_hor_id)
        if horario is None:
            return jsonify({'mensaje': 'Detalle de horario no encontrado'}), 404

        self.detalle_horario_service.actualizar(
            data['DET_HOR_ASIG_ACA_ID'],
            data['DET_HOR_DIA_SEM_ID'],
            data['DET_HOR_HORA_INICIO'],
            data['DET_HOR_HORA_FIN'],
            det_hor_id
        )
        return jsonify({'mensaje': 'Detalle de horario actualizado exitosamente'}), 200

    def eliminar(self, det_hor_id):
        horario = self.detalle_horario_service.obtener_por_id(det_hor_id)
        if horario is None:
            return jsonify({'mensaje': 'Detalle de horario no encontrado'}), 404

        self.detalle_horario_service.eliminar(det_hor_id)
        return jsonify({'mensaje': 'Detalle de horario eliminado exitosamente'}), 200
