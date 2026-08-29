from flask import current_app

class NivelEducativoService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO NivelEducativo (nombre_nivel) VALUES (%s)"
        params = (data.get('nombre_nivel'),)
        return db.execute_query(query, params, commit=True)

    def update(self, id_nivel, data):
        db = current_app.db
        query = "UPDATE NivelEducativo SET nombre_nivel = %s WHERE id_nivel = %s"
        params = (data.get('nombre_nivel'), id_nivel)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_nivel):
        db = current_app.db
        query = "DELETE FROM NivelEducativo WHERE id_nivel = %s"
        return db.execute_query(query, (id_nivel,), commit=True)

    def read(self, id_nivel=None):
        db = current_app.db
        if id_nivel:
            query = "SELECT * FROM NivelEducativo WHERE id_nivel = %s"
            return db.fetch_one(query, (id_nivel,))
        else:
            query = "SELECT * FROM NivelEducativo"
            return db.fetch_all(query)