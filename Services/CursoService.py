from flask import current_app

class CursoService:

    def crear(self, cur_uuid, cur_nombre, cur_descripcion):
        # 1. Conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Sentencia INSERT para la tabla T_CURSO
        query = (
            "INSERT INTO T_CURSO "
            "(CUR_UUID, CUR_NOMBRE, CUR_DESCRIPCION) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Pasamos los parámetros del curso
        cursor.execute(query, (cur_uuid, cur_nombre, cur_descripcion))
        
        # 4. Guardamos la transacción en la base de datos
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_CURSO"
        cursor.execute(query)
        
        # Mapeamos los resultados devueltos a un diccionario
        data = cursor.fetchall()
        cursos = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return cursos

    def obtener_por_id(self, cur_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos el curso especificando su CUR_ID
        query = "SELECT * FROM T_CURSO WHERE CUR_ID = %s"
        cursor.execute(query, (cur_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, cur_id, cur_uuid, cur_nombre, cur_descripcion):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos los campos del curso
        query = (
            "UPDATE T_CURSO "
            "SET CUR_UUID = %s, CUR_NOMBRE = %s, CUR_DESCRIPCION = %s "
            "WHERE CUR_ID = %s"
        )
        cursor.execute(query, (cur_uuid, cur_nombre, cur_descripcion, cur_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, cur_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el registro del curso por ID
        query = "DELETE FROM T_CURSO WHERE CUR_ID = %s"
        cursor.execute(query, (cur_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()