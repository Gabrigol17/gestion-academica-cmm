from flask import current_app

class MateriaService:

    def add(self, nombre_materia):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Materia (nombre_materia) VALUES (%s)"
        c.execute(query, (nombre_materia,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Materia"
        c.execute(query)
        data = c.fetchall()
        materias = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return materias

    def update(self, id_materia, nombre_materia):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Materia SET nombre_materia = %s WHERE id_materia = %s"
        c.execute(query, (nombre_materia, id_materia))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_materia):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Materia WHERE id_materia = %s"
        c.execute(query, (id_materia,))
        current_app.mysql.connection.commit()
        c.close()