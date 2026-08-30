from flask import current_app

class ComponenteEvaluativoService:

    def add(self, id_tipo_componente, id_asignacion, porcentaje):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO ComponenteEvaluativo (id_tipo_componente, id_asignacion, porcentaje) VALUES (%s, %s, %s)"
        c.execute(query, (id_tipo_componente, id_asignacion, porcentaje))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM ComponenteEvaluativo"
        c.execute(query)
        data = c.fetchall()
        componentes = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return componentes

    def update(self, id_componente, id_tipo_componente, id_asignacion, porcentaje):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE ComponenteEvaluativo SET id_tipo_componente = %s, id_asignacion = %s, porcentaje = %s WHERE id_componente = %s"
        c.execute(query, (id_tipo_componente, id_asignacion, porcentaje, id_componente))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_componente):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM ComponenteEvaluativo WHERE id_componente = %s"
        c.execute(query, (id_componente,))
        current_app.mysql.connection.commit()
        c.close()

