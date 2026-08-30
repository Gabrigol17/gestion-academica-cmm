from flask import current_app

class GradoService:

    def add(self, nombre_grado, id_nivel_educativo):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Grado (nombre_grado, id_nivel_educativo) VALUES (%s, %s)"
        c.execute(query, (nombre_grado, id_nivel_educativo))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Grado"
        c.execute(query)
        data = c.fetchall()
        grados = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return grados

    def update(self, id_grado, nombre_grado, id_nivel_educativo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Grado SET nombre_grado = %s, id_nivel_educativo = %s WHERE id_grado = %s"
        c.execute(query, (nombre_grado, id_nivel_educativo, id_grado))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_grado):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Grado WHERE id_grado = %s"
        c.execute(query, (id_grado,))
        current_app.mysql.connection.commit()
        c.close()
