from flask import current_app

class EstudianteService:

    def add(self, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Estudiante (id_persona) VALUES (%s)"
        c.execute(query, (id_persona,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Estudiante"
        c.execute(query)
        data = c.fetchall()
        estudiantes = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return estudiantes

    def update(self, id_estudiante, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Estudiante SET id_persona = %s WHERE id_estudiante = %s"
        c.execute(query, (id_persona, id_estudiante))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_estudiante):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Estudiante WHERE id_estudiante = %s"
        c.execute(query, (id_estudiante,))
        current_app.mysql.connection.commit()
        c.close()
