from flask import current_app

class DetalleHorarioService:

    def crear(self, det_hor_hora_inicio, det_hor_hora_fin, det_hor_asig_aca_id, det_hor_dia_sem_id):
        # 1. Abrimos conexión con el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos la franja horaria asociada a una asignación y día
        query = (
            "INSERT INTO T_DETALLE_HORARIO "
            "(DET_HOR_HORA_INICIO, DET_HOR_HORA_FIN, DET_HOR_ASIG_ACA_ID, DET_HOR_DIA_SEM_ID) "
            "VALUES (%s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos la consulta con parámetros
        cursor.execute(query, (det_hor_hora_inicio, det_hor_hora_fin, det_hor_asig_aca_id, det_hor_dia_sem_id))
        
        # 4. Confirmamos la inserción
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DETALLE_HORARIO"
        cursor.execute(query)
        
        data = cursor.fetchall()
        horarios = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return horarios

    def obtener_por_id(self, det_hor_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos el detalle del horario por DET_HOR_ID
        query = "SELECT * FROM T_DETALLE_HORARIO WHERE DET_HOR_ID = %s"
        cursor.execute(query, (det_hor_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, det_hor_id, det_hor_hora_inicio, det_hor_hora_fin, det_hor_asig_aca_id, det_hor_dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos las horas o asignación del horario
        query = (
            "UPDATE T_DETALLE_HORARIO "
            "SET DET_HOR_HORA_INICIO = %s, DET_HOR_HORA_FIN = %s, "
            "DET_HOR_ASIG_ACA_ID = %s, DET_HOR_DIA_SEM_ID = %s "
            "WHERE DET_HOR_ID = %s"
        )
        cursor.execute(query, (det_hor_hora_inicio, det_hor_hora_fin, det_hor_asig_aca_id, det_hor_dia_sem_id, det_hor_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, det_hor_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos la franja horaria
        query = "DELETE FROM T_DETALLE_HORARIO WHERE DET_HOR_ID = %s"
        cursor.execute(query, (det_hor_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()

