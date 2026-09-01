from flask import jsonify
from Services.ResultadoEvaluativoService import ResultadoEvaluativoService


class ResultadoEvaluativoController:

    def __init__(self):
        self.resultado_evaluativo_service = ResultadoEvaluativoService()

    def obtener_todos(self):
        resultados = self.resultado_evaluativo_service.obtener_todos()
        return jsonify(resultados), 200

    def obtener_por_id(self, res_eva_id):
        resultado = self.resultado_evaluativo_service.obtener_por_id(res_eva_id)
        if resultado is None:
            return jsonify({'mensaje': 'Resultado evaluativo no encontrado'}), 404
        return jsonify(resultado), 200

    def crear(self, data):
        campos_requeridos = ['RES_EVA_NOTA', 'RES_EVA_AJUSTE', 'RES_EVA_OBSERVACION', 'RES_EVA_MAT_ID', 'RES_EVA_ACT_EVA_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos RES_EVA_NOTA, RES_EVA_AJUSTE, RES_EVA_OBSERVACION, RES_EVA_MAT_ID y RES_EVA_ACT_EVA_ID son requeridos'}), 400

        self.resultado_evaluativo_service.crear(
            data['RES_EVA_NOTA'],
            data['RES_EVA_AJUSTE'],
            data['RES_EVA_OBSERVACION'],
            data['RES_EVA_MAT_ID'],
            data['RES_EVA_ACT_EVA_ID']
        )
        return jsonify({'mensaje': 'Resultado evaluativo creado exitosamente'}), 201

    def actualizar(self, res_eva_id, data):
        campos_requeridos = ['RES_EVA_NOTA', 'RES_EVA_AJUSTE', 'RES_EVA_OBSERVACION', 'RES_EVA_MAT_ID', 'RES_EVA_ACT_EVA_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos RES_EVA_NOTA, RES_EVA_AJUSTE, RES_EVA_OBSERVACION, RES_EVA_MAT_ID y RES_EVA_ACT_EVA_ID son requeridos'}), 400

        resultado = self.resultado_evaluativo_service.obtener_por_id(res_eva_id)
        if resultado is None:
            return jsonify({'mensaje': 'Resultado evaluativo no encontrado'}), 404

        self.resultado_evaluativo_service.actualizar(
            data['RES_EVA_NOTA'],
            data['RES_EVA_AJUSTE'],
            data['RES_EVA_OBSERVACION'],
            data['RES_EVA_MAT_ID'],
            data['RES_EVA_ACT_EVA_ID'],
            res_eva_id
        )
        return jsonify({'mensaje': 'Resultado evaluativo actualizado exitosamente'}), 200

    def eliminar(self, res_eva_id):
        resultado = self.resultado_evaluativo_service.obtener_por_id(res_eva_id)
        if resultado is None:
            return jsonify({'mensaje': 'Resultado evaluativo no encontrado'}), 404

        self.resultado_evaluativo_service.eliminar(res_eva_id)
        return jsonify({'mensaje': 'Resultado evaluativo eliminado exitosamente'}), 200
