from flask import current_app

class NivelEducativoService:

    def crear(self, niv_edu_uuid, niv_edu_nombre, niv_edu_descripcion):
        # 1. Abrimos conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Sentencia para registrar un nivel educativo (Ej: Primaria, Secundaria)
        query = (
            "INSERT INTO T_NIVEL_EDUCATIVO "
            "(NIV_EDU_UUID, NIV_EDU_NOMBRE, NIV_EDU_DESCRIPCION) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Ejecutamos la consulta
        cursor.execute(query, (niv_edu_uuid, niv_edu_nombre, niv_edu_descripcion))
        
        # 4. Guardamos los cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_NIVEL_EDUCATIVO"
        cursor.execute(query)
        
        data = cursor.fetchall()
        niveles = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return niveles

    def obtener_por_id(self, niv_edu_id):
        cursor = current_app.mysql.connection.cursor()
        # Filtramos el nivel por NIV_EDU_ID
        query = "SELECT * FROM T_NIVEL_EDUCATIVO WHERE NIV_EDU_ID = %s"
        cursor.execute(query, (niv_edu_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, niv_edu_id, niv_edu_uuid, niv_edu_nombre, niv_edu_descripcion):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos la información del nivel educativo
        query = (
            "UPDATE T_NIVEL_EDUCATIVO "
            "SET NIV_EDU_UUID = %s, NIV_EDU_NOMBRE = %s, NIV_EDU_DESCRIPCION = %s "
            "WHERE NIV_EDU_ID = %s"
        )
        cursor.execute(query, (niv_edu_uuid, niv_edu_nombre, niv_edu_descripcion, niv_edu_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, niv_edu_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el nivel educativo
        query = "DELETE FROM T_NIVEL_EDUCATIVO WHERE NIV_EDU_ID = %s"
        cursor.execute(query, (niv_edu_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()