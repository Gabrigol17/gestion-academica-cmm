from flask import jsonify
from Services.AcudienteTelefonoService import AcudienteTelefonoService


class AcudienteTelefonoController:

    def __init__(self):
        self.acudiente_telefono_service = AcudienteTelefonoService()

    def obtener_todos(self):
        telefonos = self.acudiente_telefono_service.obtener_todos()
        return jsonify(telefonos), 200

    def obtener_por_id(self, acu_tel_id):
        telefono = self.acudiente_telefono_service.obtener_por_id(acu_tel_id)
        if telefono is None:
            return jsonify({'mensaje': 'Teléfono de acudiente no encontrado'}), 404
        return jsonify(telefono), 200

    def crear(self, data):
        campos_requeridos = ['ACU_TEL_ACU_ID', 'ACU_TEL_NUMERO']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ACU_TEL_ACU_ID y ACU_TEL_NUMERO son requeridos'}), 400

        self.acudiente_telefono_service.crear(data['ACU_TEL_ACU_ID'], data['ACU_TEL_NUMERO'])
        return jsonify({'mensaje': 'Teléfono de acudiente creado exitosamente'}), 201

    def actualizar(self, acu_tel_id, data):
        campos_requeridos = ['ACU_TEL_ACU_ID', 'ACU_TEL_NUMERO']
        if not data or not all(campo in data for campo in campos_requeridos):
            return jsonify({'mensaje': 'Los campos ACU_TEL_ACU_ID y ACU_TEL_NUMERO son requeridos'}), 400

        telefono = self.acudiente_telefono_service.obtener_por_id(acu_tel_id)
        if telefono is None:
            return jsonify({'mensaje': 'Teléfono de acudiente no encontrado'}), 404

        self.acudiente_telefono_service.actualizar(data['ACU_TEL_ACU_ID'], data['ACU_TEL_NUMERO'], acu_tel_id)
        return jsonify({'mensaje': 'Teléfono de acudiente actualizado exitosamente'}), 200

    def eliminar(self, acu_tel_id):
        telefono = self.acudiente_telefono_service.obtener_por_id(acu_tel_id)
        if telefono is None:
            return jsonify({'mensaje': 'Teléfono de acudiente no encontrado'}), 404

        self.acudiente_telefono_service.eliminar(acu_tel_id)
        return jsonify({'mensaje': 'Teléfono de acudiente eliminado exitosamente'}), 200
