from flask import current_app

class VigenciaService:

    def add(self, anio):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Vigencia (anio) VALUES (%s)"
        c.execute(query, (anio,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Vigencia"
        c.execute(query)
        data = c.fetchall()
        vigencias = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return vigencias

    def update(self, id_vigencia, anio):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Vigencia SET anio = %s WHERE id_vigencia = %s"
        c.execute(query, (anio, id_vigencia))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Vigencia WHERE id_vigencia = %s"
        c.execute(query, (id_vigencia,))
        current_app.mysql.connection.commit()
        c.close()