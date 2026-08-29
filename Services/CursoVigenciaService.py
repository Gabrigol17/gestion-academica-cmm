from flask import current_app

class CursoVigenciaService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO CursoVigencia (id_curso, id_vigencia) VALUES (%s, %s)"
        params = (data.get('id_curso'), data.get('id_vigencia'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_curso_vigencia, data):
        db = current_app.db
        query = "UPDATE CursoVigencia SET id_curso = %s, id_vigencia = %s WHERE id_curso_vigencia = %s"
        params = (data.get('id_curso'), data.get('id_vigencia'), id_curso_vigencia)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_curso_vigencia):
        db = current_app.db
        query = "DELETE FROM CursoVigencia WHERE id_curso_vigencia = %s"
        return db.execute_query(query, (id_curso_vigencia,), commit=True)

    def read(self, id_curso_vigencia=None):
        db = current_app.db
        if id_curso_vigencia:
            query = "SELECT * FROM CursoVigencia WHERE id_curso_vigencia = %s"
            return db.fetch_one(query, (id_curso_vigencia,))
        else:
            query = "SELECT * FROM CursoVigencia"
            return db.fetch_all(query)