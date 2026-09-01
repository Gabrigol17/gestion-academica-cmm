from flask import jsonify
from Services.CursoVigenciaService import CursoVigenciaService


class CursoVigenciaController:

    def __init__(self):
        self.curso_vigencia_service = CursoVigenciaService()

    def obtener_todos(self):
        cursos = self.curso_vigencia_service.obtener_todos()
        return jsonify(cursos), 200

    def obtener_por_id(self, cur_vig_id):
        curso = self.curso_vigencia_service.obtener_por_id(cur_vig_id)
        if curso is None:
            return jsonify({'mensaje': 'Curso vigencia no encontrado'}), 404
        return jsonify(curso), 200

    def crear(self, data):
        campos_requeridos = ['CUR_VIG_LETRA', 'CUR_VIG_VIG_ID', 'CUR_VIG_GRAD_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos CUR_VIG_LETRA, CUR_VIG_VIG_ID y CUR_VIG_GRAD_ID son requeridos'}), 400

        self.curso_vigencia_service.crear(data['CUR_VIG_LETRA'], data['CUR_VIG_VIG_ID'], data['CUR_VIG_GRAD_ID'])
        return jsonify({'mensaje': 'Curso vigencia creado exitosamente'}), 201

    def actualizar(self, cur_vig_id, data):
        campos_requeridos = ['CUR_VIG_LETRA', 'CUR_VIG_VIG_ID', 'CUR_VIG_GRAD_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos CUR_VIG_LETRA, CUR_VIG_VIG_ID y CUR_VIG_GRAD_ID son requeridos'}), 400

        curso = self.curso_vigencia_service.obtener_por_id(cur_vig_id)
        if curso is None:
            return jsonify({'mensaje': 'Curso vigencia no encontrado'}), 404

        self.curso_vigencia_service.actualizar(data['CUR_VIG_LETRA'], data['CUR_VIG_VIG_ID'], data['CUR_VIG_GRAD_ID'], cur_vig_id)
        return jsonify({'mensaje': 'Curso vigencia actualizado exitosamente'}), 200

    def eliminar(self, cur_vig_id):
        curso = self.curso_vigencia_service.obtener_por_id(cur_vig_id)
        if curso is None:
            return jsonify({'mensaje': 'Curso vigencia no encontrado'}), 404

        self.curso_vigencia_service.eliminar(cur_vig_id)
        return jsonify({'mensaje': 'Curso vigencia eliminado exitosamente'}), 200
