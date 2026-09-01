from flask import current_app

from Models.Persona import Persona

class PersonaService:

    def crear(self, per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_correo_institucional, per_fecha_nacimiento, per_rol_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_PERSONA "
            "(PER_UUID, PER_TIPO_DOCUMENTO, PER_NUMERO_DOCUMENTO, PER_PRIMER_NOMBRE, PER_SEGUNDO_NOMBRE, "
            "PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO, PER_CORREO_INSTITUCIONAL, PER_FECHA_NACIMIENTO, PER_ROL_ID) "
            "VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        cursor.execute(query, (per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_correo_institucional, per_fecha_nacimiento, per_rol_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_PERSONA"
        cursor.execute(query)

        data = cursor.fetchall()

        personas = [Persona(col[0], col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10]).to_dict() for col in data]

        cursor.close()
        return personas

    def obtener_por_id(self, per_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        cursor.execute(query, (per_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            persona = Persona(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]).to_dict()
            return persona
        else:
            return None

    def actualizar(self, per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_correo_institucional, per_fecha_nacimiento, per_rol_id, per_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_PERSONA "
            "SET PER_TIPO_DOCUMENTO = %s, PER_NUMERO_DOCUMENTO = %s, "
            "PER_PRIMER_NOMBRE = %s, PER_SEGUNDO_NOMBRE = %s, PER_PRIMER_APELLIDO = %s, "
            "PER_SEGUNDO_APELLIDO = %s, PER_CORREO_INSTITUCIONAL = %s, "
            "PER_FECHA_NACIMIENTO = %s, PER_ROL_ID = %s "
            "WHERE PER_ID = %s"
        )
        cursor.execute(query, (per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_correo_institucional, per_fecha_nacimiento, per_rol_id, per_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, per_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_PERSONA WHERE PER_ID = %s"
        cursor.execute(query, (per_id,))

        current_app.mysql.connection.commit()
        cursor.close()
