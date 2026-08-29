from flask import current_app

class AcudienteEstudianteService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO AcudienteEstudiante (id_acudiente, id_estudiante, parentesco) VALUES (%s, %s, %s)"
        params = (data.get('id_acudiente'), data.get('id_estudiante'), data.get('parentesco'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_acudiente, id_estudiante, data):
        db = current_app.db
        query = "UPDATE AcudienteEstudiante SET parentesco = %s WHERE id_acudiente = %s AND id_estudiante = %s"
        params = (data.get('parentesco'), id_acudiente, id_estudiante)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_acudiente, id_estudiante):
        db = current_app.db
        query = "DELETE FROM AcudienteEstudiante WHERE id_acudiente = %s AND id_estudiante = %s"
        return db.execute_query(query, (id_acudiente, id_estudiante), commit=True)

    def read(self, id_acudiente=None, id_estudiante=None):
        db = current_app.db
        if id_acudiente and id_estudiante:
            query = "SELECT * FROM AcudienteEstudiante WHERE id_acudiente = %s AND id_estudiante = %s"
            return db.fetch_one(query, (id_acudiente, id_estudiante))
        else:
            query = "SELECT * FROM AcudienteEstudiante"
            return db.fetch_all(query)