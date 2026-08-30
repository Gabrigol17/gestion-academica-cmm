from flask import current_app

class AcudienteEstudianteService:

    def add(self, id_acudiente, id_estudiante, parentesco):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO AcudienteEstudiante (id_acudiente, id_estudiante, parentesco) VALUES (%s, %s, %s)"
        c.execute(query, (id_acudiente, id_estudiante, parentesco))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM AcudienteEstudiante"
        c.execute(query)
        data = c.fetchall()
        relaciones = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return relaciones

    def update(self, id_acudiente_estudiante, id_acudiente, id_estudiante, parentesco):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE AcudienteEstudiante SET id_acudiente = %s, id_estudiante = %s, parentesco = %s WHERE id_acudiente_estudiante = %s"
        c.execute(query, (id_acudiente, id_estudiante, parentesco, id_acudiente_estudiante))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_acudiente_estudiante):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM AcudienteEstudiante WHERE id_acudiente_estudiante = %s"
        c.execute(query, (id_acudiente_estudiante,))
        current_app.mysql.connection.commit()
        c.close()
