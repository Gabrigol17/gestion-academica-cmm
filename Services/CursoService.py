from flask import current_app

class CursoService:

    def add(self, nombre_curso, id_grado):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Curso (nombre_curso, id_grado) VALUES (%s, %s)"
        c.execute(query, (nombre_curso, id_grado))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Curso"
        c.execute(query)
        data = c.fetchall()
        cursos = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return cursos

    def update(self, id_curso, nombre_curso, id_grado):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Curso SET nombre_curso = %s, id_grado = %s WHERE id_curso = %s"
        c.execute(query, (nombre_curso, id_grado, id_curso))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_curso):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Curso WHERE id_curso = %s"
        c.execute(query, (id_curso,))
        current_app.mysql.connection.commit()
        c.close()

