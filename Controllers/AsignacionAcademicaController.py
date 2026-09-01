from flask import jsonify
from Services.AsignacionAcademicaService import AsignacionAcademicaService


class AsignacionAcademicaController:

    def __init__(self):
        self.asignacion_academica_service = AsignacionAcademicaService()

    def obtener_todos(self):
        asignaciones = self.asignacion_academica_service.obtener_todos()
        return jsonify(asignaciones), 200

    def obtener_por_id(self, asig_aca_id):
        asignacion = self.asignacion_academica_service.obtener_por_id(asig_aca_id)
        if asignacion is None:
            return jsonify({'mensaje': 'Asignación académica no encontrada'}), 404
        return jsonify(asignacion), 200

    def crear(self, data):
        campos_requeridos = ['ASIG_ACA_ESTADO', 'ASIG_ACA_DOC_ID', 'ASIG_ACA_MAT_ID', 'ASIG_ACA_CUR_VIG_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ASIG_ACA_ESTADO, ASIG_ACA_DOC_ID, ASIG_ACA_MAT_ID y ASIG_ACA_CUR_VIG_ID son requeridos'}), 400

        self.asignacion_academica_service.crear(
            data['ASIG_ACA_ESTADO'],
            data['ASIG_ACA_DOC_ID'],
            data['ASIG_ACA_MAT_ID'],
            data['ASIG_ACA_CUR_VIG_ID']
        )
        return jsonify({'mensaje': 'Asignación académica creada exitosamente'}), 201

    def actualizar(self, asig_aca_id, data):
        campos_requeridos = ['ASIG_ACA_ESTADO', 'ASIG_ACA_DOC_ID', 'ASIG_ACA_MAT_ID', 'ASIG_ACA_CUR_VIG_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ASIG_ACA_ESTADO, ASIG_ACA_DOC_ID, ASIG_ACA_MAT_ID y ASIG_ACA_CUR_VIG_ID son requeridos'}), 400

        asignacion = self.asignacion_academica_service.obtener_por_id(asig_aca_id)
        if asignacion is None:
            return jsonify({'mensaje': 'Asignación académica no encontrada'}), 404

        self.asignacion_academica_service.actualizar(
            data['ASIG_ACA_ESTADO'],
            data['ASIG_ACA_DOC_ID'],
            data['ASIG_ACA_MAT_ID'],
            data['ASIG_ACA_CUR_VIG_ID'],
            asig_aca_id
        )
        return jsonify({'mensaje': 'Asignación académica actualizada exitosamente'}), 200

    def eliminar(self, asig_aca_id):
        asignacion = self.asignacion_academica_service.obtener_por_id(asig_aca_id)
        if asignacion is None:
            return jsonify({'mensaje': 'Asignación académica no encontrada'}), 404

        self.asignacion_academica_service.eliminar(asig_aca_id)
        return jsonify({'mensaje': 'Asignación académica eliminada exitosamente'}), 200
