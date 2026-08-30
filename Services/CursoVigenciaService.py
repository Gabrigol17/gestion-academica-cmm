from flask import current_app

class CursoVigenciaService:

    def add(self, id_curso, id_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO CursoVigencia (id_curso, id_vigencia) VALUES (%s, %s)"
        c.execute(query, (id_curso, id_vigencia))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM CursoVigencia"
        c.execute(query)
        data = c.fetchall()
        cursos_vigencia = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return cursos_vigencia

    def update(self, id_curso_vigencia, id_curso, id_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE CursoVigencia SET id_curso = %s, id_vigencia = %s WHERE id_curso_vigencia = %s"
        c.execute(query, (id_curso, id_vigencia, id_curso_vigencia))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_curso_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM CursoVigencia WHERE id_curso_vigencia = %s"
        c.execute(query, (id_curso_vigencia,))
        current_app.mysql.connection.commit()
        c.close()
