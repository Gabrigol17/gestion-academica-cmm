from flask import current_app

class MatriculaService:

    def crear(self, mat_uuid, mat_fecha_matricula, mat_estado, mat_est_id, mat_cur_vig_id):
        # 1. Abrimos conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos la matrícula asignando un estudiante a un curso vigencia
        query = (
            "INSERT INTO T_MATRICULA "
            "(MAT_UUID, MAT_FECHA_MATRICULA, MAT_ESTADO, MAT_EST_ID, MAT_CUR_VIG_ID) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos la consulta con la tupla
        cursor.execute(query, (mat_uuid, mat_fecha_matricula, mat_estado, mat_est_id, mat_cur_vig_id))
        
        # 4. Guardamos permanentemente los cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_MATRICULA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        matriculas = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return matriculas

    def obtener_por_id(self, mat_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos la matrícula por MAT_ID
        query = "SELECT * FROM T_MATRICULA WHERE MAT_ID = %s"
        cursor.execute(query, (mat_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, mat_id, mat_uuid, mat_fecha_matricula, mat_estado, mat_est_id, mat_cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos la matrícula
        query = (
            "UPDATE T_MATRICULA "
            "SET MAT_UUID = %s, MAT_FECHA_MATRICULA = %s, MAT_ESTADO = %s, "
            "MAT_EST_ID = %s, MAT_CUR_VIG_ID = %s "
            "WHERE MAT_ID = %s"
        )
        cursor.execute(query, (mat_uuid, mat_fecha_matricula, mat_estado, mat_est_id, mat_cur_vig_id, mat_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, mat_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos la matrícula por ID
        query = "DELETE FROM T_MATRICULA WHERE MAT_ID = %s"
        cursor.execute(query, (mat_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()