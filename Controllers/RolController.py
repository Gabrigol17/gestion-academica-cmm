from flask import jsonify
from Services.RolService import RolService


class RolController:

    CAMPOS_REQUERIDOS = ['ROL_NOMBRE']

    def __init__(self):
        self.rol_service = RolService()

    def obtener_todos(self):
        roles = self.rol_service.obtener_todos()
        return jsonify(roles), 200

    def obtener_por_id(self, rol_id):
        rol = self.rol_service.obtener_por_id(rol_id)
        if rol is None:
            return jsonify({'mensaje': 'Rol no encontrado'}), 404
        return jsonify(rol), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.rol_service.crear(data['ROL_NOMBRE'])
        return jsonify({'mensaje': 'Rol creado exitosamente'}), 201

    def actualizar(self, rol_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        rol = self.rol_service.obtener_por_id(rol_id)
        if rol is None:
            return jsonify({'mensaje': 'Rol no encontrado'}), 404

        self.rol_service.actualizar(data['ROL_NOMBRE'], rol_id)
        return jsonify({'mensaje': 'Rol actualizado exitosamente'}), 200

    def eliminar(self, rol_id):
        rol = self.rol_service.obtener_por_id(rol_id)
        if rol is None:
            return jsonify({'mensaje': 'Rol no encontrado'}), 404

        self.rol_service.eliminar(rol_id)
        return jsonify({'mensaje': 'Rol eliminado exitosamente'}), 200
