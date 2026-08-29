from flask import current_app

class ComponenteEvaluativoModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO ComponenteEvaluativo (id_asignacion, id_tipo_componente, porcentaje) VALUES (%s, %s, %s)"
        params = (data.get('id_asignacion'), data.get('id_tipo_componente'), data.get('porcentaje'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_componente, data):
        db = current_app.db
        query = "UPDATE ComponenteEvaluativo SET id_asignacion = %s, id_tipo_componente = %s, porcentaje = %s WHERE id_componente = %s"
        params = (data.get('id_asignacion'), data.get('id_tipo_componente'), data.get('porcentaje'), id_componente)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_componente):
        db = current_app.db
        query = "DELETE FROM ComponenteEvaluativo WHERE id_componente = %s"
        return db.execute_query(query, (id_componente,), commit=True)

    def read(self, id_componente=None):
        db = current_app.db
        if id_componente:
            query = "SELECT * FROM ComponenteEvaluativo WHERE id_componente = %s"
            return db.fetch_one(query, (id_componente,))
        else:
            query = "SELECT * FROM ComponenteEvaluativo"
            return db.fetch_all(query)