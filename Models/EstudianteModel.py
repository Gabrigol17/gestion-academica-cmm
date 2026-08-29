from flask import current_app

class EstudianteModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Estudiante (id_persona, codigo_estudiante) VALUES (%s, %s)"
        params = (data.get('id_persona'), data.get('codigo_estudiante'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_estudiante, data):
        db = current_app.db
        query = "UPDATE Estudiante SET id_persona = %s, codigo_estudiante = %s WHERE id_estudiante = %s"
        params = (data.get('id_persona'), data.get('codigo_estudiante'), id_estudiante)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_estudiante):
        db = current_app.db
        query = "DELETE FROM Estudiante WHERE id_estudiante = %s"
        return db.execute_query(query, (id_estudiante,), commit=True)

    def read(self, id_estudiante=None):
        db = current_app.db
        if id_estudiante:
            query = "SELECT * FROM Estudiante WHERE id_estudiante = %s"
            return db.fetch_one(query, (id_estudiante,))
        else:
            query = "SELECT * FROM Estudiante"
            return db.fetch_all(query)