from flask import current_app

class ResultadoEvaluativoService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO ResultadoEvaluativo (id_actividad, id_matricula, calificacion, observacion) VALUES (%s, %s, %s, %s)"
        params = (data.get('id_actividad'), data.get('id_matricula'), data.get('calificacion'), data.get('observacion'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_resultado, data):
        db = current_app.db
        query = "UPDATE ResultadoEvaluativo SET id_actividad = %s, id_matricula = %s, calificacion = %s, observacion = %s WHERE id_resultado = %s"
        params = (data.get('id_actividad'), data.get('id_matricula'), data.get('calificacion'), data.get('observacion'), id_resultado)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_resultado):
        db = current_app.db
        query = "DELETE FROM ResultadoEvaluativo WHERE id_resultado = %s"
        return db.execute_query(query, (id_resultado,), commit=True)

    def read(self, id_resultado=None):
        db = current_app.db
        if id_resultado:
            query = "SELECT * FROM ResultadoEvaluativo WHERE id_resultado = %s"
            return db.fetch_one(query, (id_resultado,))
        else:
            query = "SELECT * FROM ResultadoEvaluativo"
            return db.fetch_all(query)