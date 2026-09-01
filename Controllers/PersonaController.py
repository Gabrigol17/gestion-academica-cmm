from flask import jsonify
from Services.PersonaService import PersonaService


class PersonaController:

    CAMPOS_REQUERIDOS = [
        'PER_TIPO_DOCUMENTO', 'PER_NUMERO_DOCUMENTO', 'PER_PRIMER_NOMBRE',
        'PER_PRIMER_APELLIDO', 'PER_CORREO_INSTITUCIONAL',
        'PER_FECHA_NACIMIENTO', 'PER_ROL_ID'
    ]

    def __init__(self):
        self.persona_service = PersonaService()

    def obtener_todos(self):
        personas = self.persona_service.obtener_todos()
        return jsonify(personas), 200

    def obtener_por_id(self, per_id):
        persona = self.persona_service.obtener_por_id(per_id)
        if persona is None:
            return jsonify({'mensaje': 'Persona no encontrada'}), 404
        return jsonify(persona), 200

    def crear(self, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        self.persona_service.crear(
            data['PER_TIPO_DOCUMENTO'],
            data['PER_NUMERO_DOCUMENTO'],
            data['PER_PRIMER_NOMBRE'],
            data.get('PER_SEGUNDO_NOMBRE', ''),
            data['PER_PRIMER_APELLIDO'],
            data.get('PER_SEGUNDO_APELLIDO', ''),
            data['PER_CORREO_INSTITUCIONAL'],
            data['PER_FECHA_NACIMIENTO'],
            data['PER_ROL_ID']
        )
        return jsonify({'mensaje': 'Persona creada exitosamente'}), 201

    def actualizar(self, per_id, data):
        if not data or not all(campo in data for campo in self.CAMPOS_REQUERIDOS):
            return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

        persona = self.persona_service.obtener_por_id(per_id)
        if persona is None:
            return jsonify({'mensaje': 'Persona no encontrada'}), 404

        self.persona_service.actualizar(
            data['PER_TIPO_DOCUMENTO'],
            data['PER_NUMERO_DOCUMENTO'],
            data['PER_PRIMER_NOMBRE'],
            data.get('PER_SEGUNDO_NOMBRE', ''),
            data['PER_PRIMER_APELLIDO'],
            data.get('PER_SEGUNDO_APELLIDO', ''),
            data['PER_CORREO_INSTITUCIONAL'],
            data['PER_FECHA_NACIMIENTO'],
            data['PER_ROL_ID'],
            per_id
        )
        return jsonify({'mensaje': 'Persona actualizada exitosamente'}), 200

    def eliminar(self, per_id):
        persona = self.persona_service.obtener_por_id(per_id)
        if persona is None:
            return jsonify({'mensaje': 'Persona no encontrada'}), 404

        self.persona_service.eliminar(per_id)
        return jsonify({'mensaje': 'Persona eliminada exitosamente'}), 200
