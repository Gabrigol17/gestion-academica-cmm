from flask import current_app

class GradoService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Grado (id_nivel, nombre_grado) VALUES (%s, %s)"
        params = (data.get('id_nivel'), data.get('nombre_grado'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_grado, data):
        db = current_app.db
        query = "UPDATE Grado SET id_nivel = %s, nombre_grado = %s WHERE id_grado = %s"
        params = (data.get('id_nivel'), data.get('nombre_grado'), id_grado)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_grado):
        db = current_app.db
        query = "DELETE FROM Grado WHERE id_grado = %s"
        return db.execute_query(query, (id_grado,), commit=True)

    def read(self, id_grado=None):
        db = current_app.db
        if id_grado:
            query = "SELECT * FROM Grado WHERE id_grado = %s"
            return db.fetch_one(query, (id_grado,))
        else:
            query = "SELECT * FROM Grado"
            return db.fetch_all(query)