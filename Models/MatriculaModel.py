from flask import current_app

class MatriculaModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Matricula (id_estudiante, id_curso_vigencia, fecha_matricula) VALUES (%s, %s, %s)"
        params = (data.get('id_estudiante'), data.get('id_curso_vigencia'), data.get('fecha_matricula'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_matricula, data):
        db = current_app.db
        query = "UPDATE Matricula SET id_estudiante = %s, id_curso_vigencia = %s, fecha_matricula = %s WHERE id_matricula = %s"
        params = (data.get('id_estudiante'), data.get('id_curso_vigencia'), data.get('fecha_matricula'), id_matricula)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_matricula):
        db = current_app.db
        query = "DELETE FROM Matricula WHERE id_matricula = %s"
        return db.execute_query(query, (id_matricula,), commit=True)

    def read(self, id_matricula=None):
        db = current_app.db
        if id_matricula:
            query = "SELECT * FROM Matricula WHERE id_matricula = %s"
            return db.fetch_one(query, (id_matricula,))
        else:
            query = "SELECT * FROM Matricula"
            return db.fetch_all(query)