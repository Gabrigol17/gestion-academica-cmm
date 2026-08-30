from flask import current_app

class DetalleHorarioService:

    def add(self, id_asignacion, id_dia_semana, hora_inicio, hora_fin):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO DetalleHorario (id_asignacion, id_dia_semana, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s)"
        c.execute(query, (id_asignacion, id_dia_semana, hora_inicio, hora_fin))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM DetalleHorario"
        c.execute(query)
        data = c.fetchall()
        horarios = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return horarios

    def update(self, id_detalle_horario, id_asignacion, id_dia_semana, hora_inicio, hora_fin):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE DetalleHorario SET id_asignacion = %s, id_dia_semana = %s, hora_inicio = %s, hora_fin = %s WHERE id_detalle_horario = %s"
        c.execute(query, (id_asignacion, id_dia_semana, hora_inicio, hora_fin, id_detalle_horario))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_detalle_horario):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM DetalleHorario WHERE id_detalle_horario = %s"
        c.execute(query, (id_detalle_horario,))
        current_app.mysql.connection.commit()
        c.close()

