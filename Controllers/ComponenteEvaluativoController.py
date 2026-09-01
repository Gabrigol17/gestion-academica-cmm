from flask import jsonify
from Services.ComponenteEvaluativoService import ComponenteEvaluativoService


class ComponenteEvaluativoController:

    def __init__(self):
        self.componente_evaluativo_service = ComponenteEvaluativoService()

    def obtener_todos(self):
        componentes = self.componente_evaluativo_service.obtener_todos()
        return jsonify(componentes), 200

    def obtener_por_id(self, com_eva_id):
        componente = self.componente_evaluativo_service.obtener_por_id(com_eva_id)
        if componente is None:
            return jsonify({'mensaje': 'Componente evaluativo no encontrado'}), 404
        return jsonify(componente), 200

    def crear(self, data):
        campos_requeridos = ['COM_EVA_PORCENTAJE', 'COM_EVA_PER_ACA_ID', 'COM_EVA_TIPO_COMP_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos COM_EVA_PORCENTAJE, COM_EVA_PER_ACA_ID y COM_EVA_TIPO_COMP_ID son requeridos'}), 400

        self.componente_evaluativo_service.crear(
            data['COM_EVA_PORCENTAJE'],
            data['COM_EVA_PER_ACA_ID'],
            data['COM_EVA_TIPO_COMP_ID']
        )
        return jsonify({'mensaje': 'Componente evaluativo creado exitosamente'}), 201

    def actualizar(self, com_eva_id, data):
        campos_requeridos = ['COM_EVA_PORCENTAJE', 'COM_EVA_PER_ACA_ID', 'COM_EVA_TIPO_COMP_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos COM_EVA_PORCENTAJE, COM_EVA_PER_ACA_ID y COM_EVA_TIPO_COMP_ID son requeridos'}), 400

        componente = self.componente_evaluativo_service.obtener_por_id(com_eva_id)
        if componente is None:
            return jsonify({'mensaje': 'Componente evaluativo no encontrado'}), 404

        self.componente_evaluativo_service.actualizar(
            data['COM_EVA_PORCENTAJE'],
            data['COM_EVA_PER_ACA_ID'],
            data['COM_EVA_TIPO_COMP_ID'],
            com_eva_id
        )
        return jsonify({'mensaje': 'Componente evaluativo actualizado exitosamente'}), 200

    def eliminar(self, com_eva_id):
        componente = self.componente_evaluativo_service.obtener_por_id(com_eva_id)
        if componente is None:
            return jsonify({'mensaje': 'Componente evaluativo no encontrado'}), 404

        self.componente_evaluativo_service.eliminar(com_eva_id)
        return jsonify({'mensaje': 'Componente evaluativo eliminado exitosamente'}), 200
