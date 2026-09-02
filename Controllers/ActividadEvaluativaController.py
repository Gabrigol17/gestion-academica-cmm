from flask import jsonify
from Services.ActividadEvaluativaService import ActividadEvaluativaService


class ActividadEvaluativaController:

    CAMPOS_REQUERIDOS = ['ACT_EVA_NOMBRE', 'ACT_EVA_DESCRIPCION', 'ACT_EVA_ASIG_ACA_ID', 'ACT_EVA_COM_EVA_ID']

    def __init__(self):
        self.actividad_evaluativa_service = ActividadEvaluativaService()

    def obtener_todos(self):
        actividades = self.actividad_evaluativa_service.obtener_todos()
        return jsonify(actividades), 200

    def obtener_por_id(self, act_eva_id):
        actividad = self.actividad_evaluativa_service.obtener_por_id(act_eva_id)
        if actividad is None:
            return jsonify({'mensaje': 'Actividad evaluativa no encontrada'}), 404
        return jsonify(actividad), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.actividad_evaluativa_service.crear(
            data['ACT_EVA_NOMBRE'],
            data['ACT_EVA_DESCRIPCION'],
            data['ACT_EVA_ASIG_ACA_ID'],
            data['ACT_EVA_COM_EVA_ID']
        )
        return jsonify({'mensaje': 'Actividad evaluativa creada exitosamente'}), 201

    def actualizar(self, act_eva_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        actividad = self.actividad_evaluativa_service.obtener_por_id(act_eva_id)
        if actividad is None:
            return jsonify({'mensaje': 'Actividad evaluativa no encontrada'}), 404

        self.actividad_evaluativa_service.actualizar(
            data['ACT_EVA_NOMBRE'],
            data['ACT_EVA_DESCRIPCION'],
            data['ACT_EVA_ASIG_ACA_ID'],
            data['ACT_EVA_COM_EVA_ID'],
            act_eva_id
        )
        return jsonify({'mensaje': 'Actividad evaluativa actualizada exitosamente'}), 200

    def eliminar(self, act_eva_id):
        actividad = self.actividad_evaluativa_service.obtener_por_id(act_eva_id)
        if actividad is None:
            return jsonify({'mensaje': 'Actividad evaluativa no encontrada'}), 404

        self.actividad_evaluativa_service.eliminar(act_eva_id)
        return jsonify({'mensaje': 'Actividad evaluativa eliminada exitosamente'}), 200
