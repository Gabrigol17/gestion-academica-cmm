from flask import current_app

class AcudienteService:

    def add(self, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Acudiente (id_persona) VALUES (%s)"
        c.execute(query, (id_persona,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Acudiente"
        c.execute(query)
        data = c.fetchall()
        acudientes = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return acudientes

    def update(self, id_acudiente, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Acudiente SET id_persona = %s WHERE id_acudiente = %s"
        c.execute(query, (id_persona, id_acudiente))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_acudiente):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Acudiente WHERE id_acudiente = %s"
        c.execute(query, (id_acudiente,))
        current_app.mysql.connection.commit()
        c.close()

