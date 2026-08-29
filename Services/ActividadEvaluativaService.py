from flask import current_app

class ActividadEvaluativaService:

    def add(self, data):
        db = current_app.db
        query = """
            INSERT INTO ActividadEvaluativa (id_componente, id_periodo, titulo, descripcion, fecha_entrega)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            data.get('id_componente'),
            data.get('id_periodo'),
            data.get('titulo'),
            data.get('descripcion'),
            data.get('fecha_entrega')
        )
        return db.execute_query(query, params, commit=True)

    def update(self, id_actividad, data):
        db = current_app.db
        query = """
            UPDATE ActividadEvaluativa 
            SET id_componente = %s, id_periodo = %s, titulo = %s, descripcion = %s, fecha_entrega = %s
            WHERE id_actividad = %s
        """
        params = (
            data.get('id_componente'),
            data.get('id_periodo'),
            data.get('titulo'),
            data.get('descripcion'),
            data.get('fecha_entrega'),
            id_actividad
        )
        return db.execute_query(query, params, commit=True)

    def delete(self, id_actividad):
        db = current_app.db
        query = "DELETE FROM ActividadEvaluativa WHERE id_actividad = %s"
        return db.execute_query(query, (id_actividad,), commit=True)

    def read(self, id_actividad=None):
        db = current_app.db
        if id_actividad:
            query = "SELECT * FROM ActividadEvaluativa WHERE id_actividad = %s"
            return db.fetch_one(query, (id_actividad,))
        else:
            query = "SELECT * FROM ActividadEvaluativa"
            return db.fetch_all(query)