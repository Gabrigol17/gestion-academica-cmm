from flask import current_app

class PersonaService:

    def crear(self, per_uuid, per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_fecha_nacimiento, per_genero, per_direccion, per_telefono, per_correo, per_contrasena_hash, per_rol_id):
        # 1. Conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Consulta de inserción completa para la tabla central T_PERSONA
        query = (
            "INSERT INTO T_PERSONA "
            "(PER_UUID, PER_TIPO_DOCUMENTO, PER_NUMERO_DOCUMENTO, PER_PRIMER_NOMBRE, PER_SEGUNDO_NOMBRE, "
            "PER_PRIMER_APELLIDO, PER_SEGUNDO_APELLIDO, PER_FECHA_NACIMIENTO, PER_GENERO, PER_DIRECCION, "
            "PER_TELEFONO, PER_CORREO, PER_CONTRASENA_HASH, PER_ROL_ID) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        
        # 3. Pasamos todos los datos personales en la tupla
        cursor.execute(query, (per_uuid, per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_fecha_nacimiento, per_genero, per_direccion, per_telefono, per_correo, per_contrasena_hash, per_rol_id))
        
        # 4. Guardamos la transacción en MySQL
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_PERSONA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        personas = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return personas

    def obtener_por_id(self, per_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos a la persona por su clave primaria PER_ID
        query = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        cursor.execute(query, (per_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, per_id, per_uuid, per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_fecha_nacimiento, per_genero, per_direccion, per_telefono, per_correo, per_contrasena_hash, per_rol_id):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia UPDATE completa para actualizar la persona
        query = (
            "UPDATE T_PERSONA "
            "SET PER_UUID = %s, PER_TIPO_DOCUMENTO = %s, PER_NUMERO_DOCUMENTO = %s, "
            "PER_PRIMER_NOMBRE = %s, PER_SEGUNDO_NOMBRE = %s, PER_PRIMER_APELLIDO = %s, "
            "PER_SEGUNDO_APELLIDO = %s, PER_FECHA_NACIMIENTO = %s, PER_GENERO = %s, "
            "PER_DIRECCION = %s, PER_TELEFONO = %s, PER_CORREO = %s, "
            "PER_CONTRASENA_HASH = %s, PER_ROL_ID = %s "
            "WHERE PER_ID = %s"
        )
        cursor.execute(query, (per_uuid, per_tipo_documento, per_numero_documento, per_primer_nombre, per_segundo_nombre, per_primer_apellido, per_segundo_apellido, per_fecha_nacimiento, per_genero, per_direccion, per_telefono, per_correo, per_contrasena_hash, per_rol_id, per_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, per_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el registro de la persona
        query = "DELETE FROM T_PERSONA WHERE PER_ID = %s"
        cursor.execute(query, (per_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()