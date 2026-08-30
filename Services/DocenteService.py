from flask import current_app

class DocenteService:

    def add(self, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Docente (id_persona) VALUES (%s)"
        c.execute(query, (id_persona,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Docente"
        c.execute(query)
        data = c.fetchall()
        docentes = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return docentes

    def update(self, id_docente, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Docente SET id_persona = %s WHERE id_docente = %s"
        c.execute(query, (id_persona, id_docente))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_docente):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Docente WHERE id_docente = %s"
        c.execute(query, (id_docente,))
        current_app.mysql.connection.commit()
        c.close()
