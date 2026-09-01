from flask import jsonify
from Services.MatriculaService import MatriculaService


class MatriculaController:

    CAMPOS_REQUERIDOS = ['MATR_EST_ID', 'MATR_CUR_VIG_ID']

    def __init__(self):
        self.matricula_service = MatriculaService()

    def obtener_todos(self):
        matriculas = self.matricula_service.obtener_todos()
        return jsonify(matriculas), 200

    def obtener_por_id(self, matr_id):
        matricula = self.matricula_service.obtener_por_id(matr_id)
        if matricula is None:
            return jsonify({'mensaje': 'Matrícula no encontrada'}), 404
        return jsonify(matricula), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.matricula_service.crear(data['MATR_EST_ID'], data['MATR_CUR_VIG_ID'])
        return jsonify({'mensaje': 'Matrícula creada exitosamente'}), 201

    def actualizar(self, matr_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        matricula = self.matricula_service.obtener_por_id(matr_id)
        if matricula is None:
            return jsonify({'mensaje': 'Matrícula no encontrada'}), 404

        self.matricula_service.actualizar(data['MATR_EST_ID'], data['MATR_CUR_VIG_ID'], matr_id)
        return jsonify({'mensaje': 'Matrícula actualizada exitosamente'}), 200

    def eliminar(self, matr_id):
        matricula = self.matricula_service.obtener_por_id(matr_id)
        if matricula is None:
            return jsonify({'mensaje': 'Matrícula no encontrada'}), 404

        self.matricula_service.eliminar(matr_id)
        return jsonify({'mensaje': 'Matrícula eliminada exitosamente'}), 200
