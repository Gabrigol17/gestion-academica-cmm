from flask import jsonify
from Services.AcudienteService import AcudienteService


class AcudienteController:

    def __init__(self):
        self.acudiente_service = AcudienteService()

    def obtener_todos(self):
        acudientes = self.acudiente_service.obtener_todos()
        return jsonify(acudientes), 200

    def obtener_por_id(self, acu_id):
        acudiente = self.acudiente_service.obtener_por_id(acu_id)
        if acudiente is None:
            return jsonify({'mensaje': 'Acudiente no encontrado'}), 404
        return jsonify(acudiente), 200

    def crear(self, data):
        campos_requeridos = ['ACU_NOMBRES', 'ACU_APELLIDOS', 'ACU_ESTADO']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ACU_NOMBRES, ACU_APELLIDOS y ACU_ESTADO son requeridos'}), 400

        self.acudiente_service.crear(data['ACU_NOMBRES'], data['ACU_APELLIDOS'], data['ACU_ESTADO'])
        return jsonify({'mensaje': 'Acudiente creado exitosamente'}), 201

    def actualizar(self, acu_id, data):
        campos_requeridos = ['ACU_NOMBRES', 'ACU_APELLIDOS', 'ACU_ESTADO']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ACU_NOMBRES, ACU_APELLIDOS y ACU_ESTADO son requeridos'}), 400

        acudiente = self.acudiente_service.obtener_por_id(acu_id)
        if acudiente is None:
            return jsonify({'mensaje': 'Acudiente no encontrado'}), 404

        self.acudiente_service.actualizar(data['ACU_NOMBRES'], data['ACU_APELLIDOS'], data['ACU_ESTADO'], acu_id)
        return jsonify({'mensaje': 'Acudiente actualizado exitosamente'}), 200

    def eliminar(self, acu_id):
        acudiente = self.acudiente_service.obtener_por_id(acu_id)
        if acudiente is None:
            return jsonify({'mensaje': 'Acudiente no encontrado'}), 404

        self.acudiente_service.eliminar(acu_id)
        return jsonify({'mensaje': 'Acudiente eliminado exitosamente'}), 200
