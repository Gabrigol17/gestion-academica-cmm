from flask import jsonify
from Services.TipoComponenteService import TipoComponenteService


class TipoComponenteController:

    CAMPOS_REQUERIDOS = ['TIPO_COMP_NOMBRE']

    def __init__(self):
        self.tipo_componente_service = TipoComponenteService()

    def obtener_todos(self):
        tipos = self.tipo_componente_service.obtener_todos()
        return jsonify(tipos), 200

    def obtener_por_id(self, tipo_comp_id):
        tipo = self.tipo_componente_service.obtener_por_id(tipo_comp_id)
        if tipo is None:
            return jsonify({'mensaje': 'Tipo de componente no encontrado'}), 404
        return jsonify(tipo), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.tipo_componente_service.crear(data['TIPO_COMP_NOMBRE'])
        return jsonify({'mensaje': 'Tipo de componente creado exitosamente'}), 201

    def actualizar(self, tipo_comp_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        tipo = self.tipo_componente_service.obtener_por_id(tipo_comp_id)
        if tipo is None:
            return jsonify({'mensaje': 'Tipo de componente no encontrado'}), 404

        self.tipo_componente_service.actualizar(data['TIPO_COMP_NOMBRE'], tipo_comp_id)
        return jsonify({'mensaje': 'Tipo de componente actualizado exitosamente'}), 200

    def eliminar(self, tipo_comp_id):
        tipo = self.tipo_componente_service.obtener_por_id(tipo_comp_id)
        if tipo is None:
            return jsonify({'mensaje': 'Tipo de componente no encontrado'}), 404

        self.tipo_componente_service.eliminar(tipo_comp_id)
        return jsonify({'mensaje': 'Tipo de componente eliminado exitosamente'}), 200
