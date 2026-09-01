from flask import jsonify
from Services.CursoService import CursoService


class CursoController:

    CAMPOS_REQUERIDOS = ['CUR_NOMBRE', 'CUR_DESCRIPCION']

    def __init__(self):
        self.curso_service = CursoService()

    def obtener_todos(self):
        cursos = self.curso_service.obtener_todos()
        return jsonify(cursos), 200

    def obtener_por_id(self, cur_id):
        curso = self.curso_service.obtener_por_id(cur_id)
        if curso is None:
            return jsonify({'mensaje': 'Curso no encontrado'}), 404
        return jsonify(curso), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.curso_service.crear(data['CUR_NOMBRE'], data['CUR_DESCRIPCION'])
        return jsonify({'mensaje': 'Curso creado exitosamente'}), 201

    def actualizar(self, cur_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        curso = self.curso_service.obtener_por_id(cur_id)
        if curso is None:
            return jsonify({'mensaje': 'Curso no encontrado'}), 404

        self.curso_service.actualizar(data['CUR_NOMBRE'], data['CUR_DESCRIPCION'], cur_id)
        return jsonify({'mensaje': 'Curso actualizado exitosamente'}), 200

    def eliminar(self, cur_id):
        curso = self.curso_service.obtener_por_id(cur_id)
        if curso is None:
            return jsonify({'mensaje': 'Curso no encontrado'}), 404

        self.curso_service.eliminar(cur_id)
        return jsonify({'mensaje': 'Curso eliminado exitosamente'}), 200
