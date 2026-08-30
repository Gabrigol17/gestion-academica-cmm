from flask import current_app

class ActividadEvaluativaService:

    def add(self, id_componente, id_periodo, titulo, descripcion, fecha_entrega):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO ActividadEvaluativa (id_componente, id_periodo, titulo, descripcion, fecha_entrega) VALUES (%s, %s, %s, %s, %s)"
        c.execute(query, (id_componente, id_periodo, titulo, descripcion, fecha_entrega))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM ActividadEvaluativa"
        c.execute(query)
        data = c.fetchall()
        actividades = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return actividades

    def update(self, id_actividad, id_componente, id_periodo, titulo, descripcion, fecha_entrega):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE ActividadEvaluativa SET id_componente = %s, id_periodo = %s, titulo = %s, descripcion = %s, fecha_entrega = %s WHERE id_actividad = %s"
        c.execute(query, (id_componente, id_periodo, titulo, descripcion, fecha_entrega, id_actividad))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_actividad):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM ActividadEvaluativa WHERE id_actividad = %s"
        c.execute(query, (id_actividad,))
        current_app.mysql.connection.commit()
        c.close()