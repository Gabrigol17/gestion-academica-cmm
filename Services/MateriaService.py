from flask import current_app

class MateriaService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Materia (nombre_materia, descripcion) VALUES (%s, %s)"
        params = (data.get('nombre_materia'), data.get('descripcion'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_materia, data):
        db = current_app.db
        query = "UPDATE Materia SET nombre_materia = %s, descripcion = %s WHERE id_materia = %s"
        params = (data.get('nombre_materia'), data.get('descripcion'), id_materia)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_materia):
        db = current_app.db
        query = "DELETE FROM Materia WHERE id_materia = %s"
        return db.execute_query(query, (id_materia,), commit=True)

    def read(self, id_materia=None):
        db = current_app.db
        if id_materia:
            query = "SELECT * FROM Materia WHERE id_materia = %s"
            return db.fetch_one(query, (id_materia,))
        else:
            query = "SELECT * FROM Materia"
            return db.fetch_all(query)