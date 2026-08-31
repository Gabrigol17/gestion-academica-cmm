from flask import current_app

class RolService:

    def crear(self, rol_uuid, rol_nombre, rol_descripcion):
        # 1. Abrimos conexión MySQL
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos el nuevo rol de usuario (Ej: Docente, Estudiante, Administrador)
        query = (
            "INSERT INTO T_ROL "
            "(ROL_UUID, ROL_NOMBRE, ROL_DESCRIPCION) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Ejecutamos la consulta pasándole la tupla
        cursor.execute(query, (rol_uuid, rol_nombre, rol_descripcion))
        
        # 4. Confirmamos la inserción
        current_app.mysql.connection.commit()
        
        # 5. Cerramos cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ROL"
        cursor.execute(query)
        
        data = cursor.fetchall()
        roles = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return roles

    def obtener_por_id(self, rol_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos el rol por su ROL_ID
        query = "SELECT * FROM T_ROL WHERE ROL_ID = %s"
        cursor.execute(query, (rol_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, rol_id, rol_uuid, rol_nombre, rol_descripcion):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos el rol de usuario
        query = (
            "UPDATE T_ROL "
            "SET ROL_UUID = %s, ROL_NOMBRE = %s, ROL_DESCRIPCION = %s "
            "WHERE ROL_ID = %s"
        )
        cursor.execute(query, (rol_uuid, rol_nombre, rol_descripcion, rol_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, rol_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el rol por su ID
        query = "DELETE FROM T_ROL WHERE ROL_ID = %s"
        cursor.execute(query, (rol_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()