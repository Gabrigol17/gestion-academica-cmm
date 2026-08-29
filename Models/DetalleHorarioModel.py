from flask import current_app

class DetalleHorarioModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO DetalleHorario (id_asignacion, id_dia, hora_inicio, hora_fin) VALUES (%s, %s, %s, %s)"
        params = (data.get('id_asignacion'), data.get('id_dia'), data.get('hora_inicio'), data.get('hora_fin'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_detalle_horario, data):
        db = current_app.db
        query = "UPDATE DetalleHorario SET id_asignacion = %s, id_dia = %s, hora_inicio = %s, hora_fin = %s WHERE id_detalle_horario = %s"
        params = (data.get('id_asignacion'), data.get('id_dia'), data.get('hora_inicio'), data.get('hora_fin'), id_detalle_horario)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_detalle_horario):
        db = current_app.db
        query = "DELETE FROM DetalleHorario WHERE id_detalle_horario = %s"
        return db.execute_query(query, (id_detalle_horario,), commit=True)

    def read(self, id_detalle_horario=None):
        db = current_app.db
        if id_detalle_horario:
            query = "SELECT * FROM DetalleHorario WHERE id_detalle_horario = %s"
            return db.fetch_one(query, (id_detalle_horario,))
        else:
            query = "SELECT * FROM DetalleHorario"
            return db.fetch_all(query)