from flask import jsonify
from Services.PeriodoAcademicoService import PeriodoAcademicoService


class PeriodoAcademicoController:

    def __init__(self):
        self.periodo_academico_service = PeriodoAcademicoService()

    def obtener_todos(self):
        periodos = self.periodo_academico_service.obtener_todos()
        return jsonify(periodos), 200

    def obtener_por_id(self, per_aca_id):
        periodo = self.periodo_academico_service.obtener_por_id(per_aca_id)
        if periodo is None:
            return jsonify({'mensaje': 'Período académico no encontrado'}), 404
        return jsonify(periodo), 200

    def crear(self, data):
        campos_requeridos = ['PER_ACA_NUMERO', 'PER_ACA_FECHA_INICIO', 'PER_ACA_FECHA_FIN', 'PER_ACA_VIG_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos PER_ACA_NUMERO, PER_ACA_FECHA_INICIO, PER_ACA_FECHA_FIN y PER_ACA_VIG_ID son requeridos'}), 400

        self.periodo_academico_service.crear(
            data['PER_ACA_NUMERO'],
            data['PER_ACA_FECHA_INICIO'],
            data['PER_ACA_FECHA_FIN'],
            data['PER_ACA_VIG_ID']
        )
        return jsonify({'mensaje': 'Período académico creado exitosamente'}), 201

    def actualizar(self, per_aca_id, data):
        campos_requeridos = ['PER_ACA_NUMERO', 'PER_ACA_FECHA_INICIO', 'PER_ACA_FECHA_FIN', 'PER_ACA_VIG_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos PER_ACA_NUMERO, PER_ACA_FECHA_INICIO, PER_ACA_FECHA_FIN y PER_ACA_VIG_ID son requeridos'}), 400

        periodo = self.periodo_academico_service.obtener_por_id(per_aca_id)
        if periodo is None:
            return jsonify({'mensaje': 'Período académico no encontrado'}), 404

        self.periodo_academico_service.actualizar(
            data['PER_ACA_NUMERO'],
            data['PER_ACA_FECHA_INICIO'],
            data['PER_ACA_FECHA_FIN'],
            data['PER_ACA_VIG_ID'],
            per_aca_id
        )
        return jsonify({'mensaje': 'Período académico actualizado exitosamente'}), 200

    def eliminar(self, per_aca_id):
        periodo = self.periodo_academico_service.obtener_por_id(per_aca_id)
        if periodo is None:
            return jsonify({'mensaje': 'Período académico no encontrado'}), 404

        self.periodo_academico_service.eliminar(per_aca_id)
        return jsonify({'mensaje': 'Período académico eliminado exitosamente'}), 200
