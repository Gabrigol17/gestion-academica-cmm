from flask import jsonify
from Services.CursoService import CursoService


class CursoController:

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
        campos_requeridos = ['CUR_NOMBRE', 'CUR_DESCRIPCION']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos CUR_NOMBRE y CUR_DESCRIPCION son requeridos'}), 400

        self.curso_service.crear(data['CUR_NOMBRE'], data['CUR_DESCRIPCION'])
        return jsonify({'mensaje': 'Curso creado exitosamente'}), 201

    def actualizar(self, cur_id, data):
        campos_requeridos = ['CUR_NOMBRE', 'CUR_DESCRIPCION']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos CUR_NOMBRE y CUR_DESCRIPCION son requeridos'}), 400

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
