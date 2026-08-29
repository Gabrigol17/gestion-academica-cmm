from flask import current_app

class CursoModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Curso (id_grado, nombre_curso) VALUES (%s, %s)"
        params = (data.get('id_grado'), data.get('nombre_curso'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_curso, data):
        db = current_app.db
        query = "UPDATE Curso SET id_grado = %s, nombre_curso = %s WHERE id_curso = %s"
        params = (data.get('id_grado'), data.get('nombre_curso'), id_curso)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_curso):
        db = current_app.db
        query = "DELETE FROM Curso WHERE id_curso = %s"
        return db.execute_query(query, (id_curso,), commit=True)

    def read(self, id_curso=None):
        db = current_app.db
        if id_curso:
            query = "SELECT * FROM Curso WHERE id_curso = %s"
            return db.fetch_one(query, (id_curso,))
        else:
            query = "SELECT * FROM Curso"
            return db.fetch_all(query)