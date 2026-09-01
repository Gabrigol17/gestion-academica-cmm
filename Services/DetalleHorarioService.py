from flask import current_app

from Models.DetalleHorario import DetalleHorario

class DetalleHorarioService:

    def crear(self, det_hor_asig_aca_id, det_hor_dia_sem_id, det_hor_hora_inicio, det_hor_hora_fin):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_DETALLE_HORARIO "
            "(DET_HOR_UUID, DET_HOR_ASIG_ACA_ID, DET_HOR_DIA_SEM_ID, DET_HOR_HORA_INICIO, DET_HOR_HORA_FIN) "
            "VALUES (UUID(), %s, %s, %s, %s)"
        )

        cursor.execute(query, (det_hor_asig_aca_id, det_hor_dia_sem_id, det_hor_hora_inicio, det_hor_hora_fin))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DETALLE_HORARIO"
        cursor.execute(query)

        data = cursor.fetchall()

        horarios = [DetalleHorario(col[0], col[1], col[2], col[3], col[4], col[5]).to_dict() for col in data]

        cursor.close()
        return horarios

    def obtener_por_id(self, det_hor_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DETALLE_HORARIO WHERE DET_HOR_ID = %s"
        cursor.execute(query, (det_hor_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            horario = DetalleHorario(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()
            return horario
        else:
            return None

    def actualizar(self, det_hor_asig_aca_id, det_hor_dia_sem_id, det_hor_hora_inicio, det_hor_hora_fin, det_hor_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_DETALLE_HORARIO "
            "SET DET_HOR_ASIG_ACA_ID = %s, DET_HOR_DIA_SEM_ID = %s, "
            "DET_HOR_HORA_INICIO = %s, DET_HOR_HORA_FIN = %s "
            "WHERE DET_HOR_ID = %s"
        )
        cursor.execute(query, (det_hor_asig_aca_id, det_hor_dia_sem_id, det_hor_hora_inicio, det_hor_hora_fin, det_hor_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, det_hor_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_DETALLE_HORARIO WHERE DET_HOR_ID = %s"
        cursor.execute(query, (det_hor_id,))

        current_app.mysql.connection.commit()
        cursor.close()
