from flask import current_app

class AsignacionAcademicaService:

    def add(self, id_docente, id_materia, id_curso_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO AsignacionAcademica (id_docente, id_materia, id_curso_vigencia) VALUES (%s, %s, %s)"
        c.execute(query, (id_docente, id_materia, id_curso_vigencia))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM AsignacionAcademica"
        c.execute(query)
        data = c.fetchall()
        asignaciones = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return asignaciones

    def update(self, id_asignacion, id_docente, id_materia, id_curso_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE AsignacionAcademica SET id_docente = %s, id_materia = %s, id_curso_vigencia = %s WHERE id_asignacion = %s"
        c.execute(query, (id_docente, id_materia, id_curso_vigencia, id_asignacion))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_asignacion):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM AsignacionAcademica WHERE id_asignacion = %s"
        c.execute(query, (id_asignacion,))
        current_app.mysql.connection.commit()
        c.close()

