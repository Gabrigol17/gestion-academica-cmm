from flask import current_app

class GradoService:

    def crear(self, grad_uuid, grad_nombre, grad_niv_edu_id):
        # 1. Obtenemos cursor de MySQL
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos el grado especificando el nivel educativo al que pertenece
        query = (
            "INSERT INTO T_GRADO "
            "(GRAD_UUID, GRAD_NOMBRE, GRAD_NIV_EDU_ID) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Ejecutamos enviando los datos
        cursor.execute(query, (grad_uuid, grad_nombre, grad_niv_edu_id))
        
        # 4. Guardamos cambios
        current_app.mysql.connection.commit()
        
        # 5. Liberamos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_GRADO"
        cursor.execute(query)
        
        data = cursor.fetchall()
        grados = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return grados

    def obtener_por_id(self, grad_id):
        cursor = current_app.mysql.connection.cursor()
        # Consulta de filtrado por GRAD_ID
        query = "SELECT * FROM T_GRADO WHERE GRAD_ID = %s"
        cursor.execute(query, (grad_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, grad_id, grad_uuid, grad_nombre, grad_niv_edu_id):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia UPDATE para modificar los datos del grado
        query = (
            "UPDATE T_GRADO "
            "SET GRAD_UUID = %s, GRAD_NOMBRE = %s, GRAD_NIV_EDU_ID = %s "
            "WHERE GRAD_ID = %s"
        )
        cursor.execute(query, (grad_uuid, grad_nombre, grad_niv_edu_id, grad_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, grad_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos el registro del grado por su ID
        query = "DELETE FROM T_GRADO WHERE GRAD_ID = %s"
        cursor.execute(query, (grad_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()