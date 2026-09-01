from flask import jsonify
from Services.MateriaService import MateriaService


class MateriaController:

    def __init__(self):
        self.materia_service = MateriaService()

    def obtener_todos(self):
        materias = self.materia_service.obtener_todos()
        return jsonify(materias), 200

    def obtener_por_id(self, mat_id):
        materia = self.materia_service.obtener_por_id(mat_id)
        if materia is None:
            return jsonify({'mensaje': 'Materia no encontrada'}), 404
        return jsonify(materia), 200

    def crear(self, data):
        if not data or 'MAT_NOMBRE' not in data:
            return jsonify({'mensaje': 'El campo MAT_NOMBRE es requerido'}), 400

        self.materia_service.crear(data['MAT_NOMBRE'])
        return jsonify({'mensaje': 'Materia creada exitosamente'}), 201

    def actualizar(self, mat_id, data):
        if not data or 'MAT_NOMBRE' not in data:
            return jsonify({'mensaje': 'El campo MAT_NOMBRE es requerido'}), 400

        materia = self.materia_service.obtener_por_id(mat_id)
        if materia is None:
            return jsonify({'mensaje': 'Materia no encontrada'}), 404

        self.materia_service.actualizar(data['MAT_NOMBRE'], mat_id)
        return jsonify({'mensaje': 'Materia actualizada exitosamente'}), 200

    def eliminar(self, mat_id):
        materia = self.materia_service.obtener_por_id(mat_id)
        if materia is None:
            return jsonify({'mensaje': 'Materia no encontrada'}), 404

        self.materia_service.eliminar(mat_id)
        return jsonify({'mensaje': 'Materia eliminada exitosamente'}), 200
