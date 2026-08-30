from flask import current_app

class MatriculaService:

    def add(self, id_estudiante, id_curso_vigencia, fecha_matricula):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Matricula (id_estudiante, id_curso_vigencia, fecha_matricula) VALUES (%s, %s, %s)"
        c.execute(query, (id_estudiante, id_curso_vigencia, fecha_matricula))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Matricula"
        c.execute(query)
        data = c.fetchall()
        matriculas = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return matriculas

    def update(self, id_matricula, id_estudiante, id_curso_vigencia, fecha_matricula):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Matricula SET id_estudiante = %s, id_curso_vigencia = %s, fecha_matricula = %s WHERE id_matricula = %s"
        c.execute(query, (id_estudiante, id_curso_vigencia, fecha_matricula, id_matricula))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_matricula):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Matricula WHERE id_matricula = %s"
        c.execute(query, (id_matricula,))
        current_app.mysql.connection.commit()
        c.close()
