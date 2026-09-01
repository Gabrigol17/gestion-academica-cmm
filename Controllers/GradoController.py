from flask import jsonify
from Services.GradoService import GradoService


class GradoController:

    def __init__(self):
        self.grado_service = GradoService()

    def obtener_todos(self):
        grados = self.grado_service.obtener_todos()
        return jsonify(grados), 200

    def obtener_por_id(self, grad_id):
        grado = self.grado_service.obtener_por_id(grad_id)
        if grado is None:
            return jsonify({'mensaje': 'Grado no encontrado'}), 404
        return jsonify(grado), 200

    def crear(self, data):
        campos_requeridos = ['GRAD_NOMBRE', 'GRAD_NIV_EDUC_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos GRAD_NOMBRE y GRAD_NIV_EDUC_ID son requeridos'}), 400

        self.grado_service.crear(data['GRAD_NOMBRE'], data['GRAD_NIV_EDUC_ID'])
        return jsonify({'mensaje': 'Grado creado exitosamente'}), 201

    def actualizar(self, grad_id, data):
        campos_requeridos = ['GRAD_NOMBRE', 'GRAD_NIV_EDUC_ID']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos GRAD_NOMBRE y GRAD_NIV_EDUC_ID son requeridos'}), 400

        grado = self.grado_service.obtener_por_id(grad_id)
        if grado is None:
            return jsonify({'mensaje': 'Grado no encontrado'}), 404

        self.grado_service.actualizar(data['GRAD_NOMBRE'], data['GRAD_NIV_EDUC_ID'], grad_id)
        return jsonify({'mensaje': 'Grado actualizado exitosamente'}), 200

    def eliminar(self, grad_id):
        grado = self.grado_service.obtener_por_id(grad_id)
        if grado is None:
            return jsonify({'mensaje': 'Grado no encontrado'}), 404

        self.grado_service.eliminar(grad_id)
        return jsonify({'mensaje': 'Grado eliminado exitosamente'}), 200
