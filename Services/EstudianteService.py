from flask import current_app

class EstudianteService:

    def crear(self, est_uuid, est_codigo_estudiantil, est_estado, est_per_id):
        # 1. Abrimos conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos la información propia del estudiante
        query = (
            "INSERT INTO T_ESTUDIANTE "
            "(EST_UUID, EST_CODIGO_ESTUDIANTIL, EST_ESTADO, EST_PER_ID) "
            "VALUES (%s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos la consulta pasándole la tupla de datos
        cursor.execute(query, (est_uuid, est_codigo_estudiantil, est_estado, est_per_id))
        
        # 4. Confirmamos la inserción en la base de datos
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ESTUDIANTE"
        cursor.execute(query)
        
        data = cursor.fetchall()
        estudiantes = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return estudiantes

    def obtener_por_id(self, est_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos estudiante por EST_ID
        query = "SELECT * FROM T_ESTUDIANTE WHERE EST_ID = %s"
        cursor.execute(query, (est_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, est_id, est_uuid, est_codigo_estudiantil, est_estado, est_per_id):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos código estudiantil o datos del estudiante
        query = (
            "UPDATE T_ESTUDIANTE "
            "SET EST_UUID = %s, EST_CODIGO_ESTUDIANTIL = %s, EST_ESTADO = %s, EST_PER_ID = %s "
            "WHERE EST_ID = %s"
        )
        cursor.execute(query, (est_uuid, est_codigo_estudiantil, est_estado, est_per_id, est_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, est_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos la ficha del estudiante
        query = "DELETE FROM T_ESTUDIANTE WHERE EST_ID = %s"
        cursor.execute(query, (est_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()