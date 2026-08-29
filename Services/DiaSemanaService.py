from flask import current_app

class DiaSemanaService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO DiaSemana (nombre_dia) VALUES (%s)"
        params = (data.get('nombre_dia'),)
        return db.execute_query(query, params, commit=True)

    def update(self, id_dia, data):
        db = current_app.db
        query = "UPDATE DiaSemana SET nombre_dia = %s WHERE id_dia = %s"
        params = (data.get('nombre_dia'), id_dia)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_dia):
        db = current_app.db
        query = "DELETE FROM DiaSemana WHERE id_dia = %s"
        return db.execute_query(query, (id_dia,), commit=True)

    def read(self, id_dia=None):
        db = current_app.db
        if id_dia:
            query = "SELECT * FROM DiaSemana WHERE id_dia = %s"
            return db.fetch_one(query, (id_dia,))
        else:
            query = "SELECT * FROM DiaSemana"
            return db.fetch_all(query)