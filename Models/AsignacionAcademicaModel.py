from flask import current_app

class AsignacionAcademicaModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO AsignacionAcademica (id_docente, id_materia, id_curso_vigencia) VALUES (%s, %s, %s)"
        params = (data.get('id_docente'), data.get('id_materia'), data.get('id_curso_vigencia'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_asignacion, data):
        db = current_app.db
        query = "UPDATE AsignacionAcademica SET id_docente = %s, id_materia = %s, id_curso_vigencia = %s WHERE id_asignacion = %s"
        params = (data.get('id_docente'), data.get('id_materia'), data.get('id_curso_vigencia'), id_asignacion)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_asignacion):
        db = current_app.db
        query = "DELETE FROM AsignacionAcademica WHERE id_asignacion = %s"
        return db.execute_query(query, (id_asignacion,), commit=True)

    def read(self, id_asignacion=None):
        db = current_app.db
        if id_asignacion:
            query = "SELECT * FROM AsignacionAcademica WHERE id_asignacion = %s"
            return db.fetch_one(query, (id_asignacion,))
        else:
            query = "SELECT * FROM AsignacionAcademica"
            return db.fetch_all(query)