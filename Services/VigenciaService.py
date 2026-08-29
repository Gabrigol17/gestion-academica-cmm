from flask import current_app

class VigenciaService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Vigencia (anio, estado) VALUES (%s, %s)"
        params = (data.get('anio'), data.get('estado'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_vigencia, data):
        db = current_app.db
        query = "UPDATE Vigencia SET anio = %s, estado = %s WHERE id_vigencia = %s"
        params = (data.get('anio'), data.get('estado'), id_vigencia)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_vigencia):
        db = current_app.db
        query = "DELETE FROM Vigencia WHERE id_vigencia = %s"
        return db.execute_query(query, (id_vigencia,), commit=True)

    def read(self, id_vigencia=None):
        db = current_app.db
        if id_vigencia:
            query = "SELECT * FROM Vigencia WHERE id_vigencia = %s"
            return db.fetch_one(query, (id_vigencia,))
        else:
            query = "SELECT * FROM Vigencia"
            return db.fetch_all(query)