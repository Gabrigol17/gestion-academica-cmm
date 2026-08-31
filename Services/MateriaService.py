from flask import current_app

class MateriaService:

    def crear(self, mat_uuid, mat_nombre, mat_descripcion):
        # 1. Abrimos conexión con la BD
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos la materia en T_MATERIA
        query = (
            "INSERT INTO T_MATERIA "
            "(MAT_UUID, MAT_NOMBRE, MAT_DESCRIPCION) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Ejecutamos la consulta
        cursor.execute(query, (mat_uuid, mat_nombre, mat_descripcion))
        
        # 4. Confirmamos la transacción
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_MATERIA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        materias = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return materias

    def obtener_por_id(self, mat_id):
        cursor = current_app.mysql.connection.cursor()
        # Filtramos la materia por MAT_ID
        query = "SELECT * FROM T_MATERIA WHERE MAT_ID = %s"
        cursor.execute(query, (mat_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, mat_id, mat_uuid, mat_nombre, mat_descripcion):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos la materia
        query = (
            "UPDATE T_MATERIA "
            "SET MAT_UUID = %s, MAT_NOMBRE = %s, MAT_DESCRIPCION = %s "
            "WHERE MAT_ID = %s"
        )
        cursor.execute(query, (mat_uuid, mat_nombre, mat_descripcion, mat_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, mat_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos la materia por su ID
        query = "DELETE FROM T_MATERIA WHERE MAT_ID = %s"
        cursor.execute(query, (mat_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()