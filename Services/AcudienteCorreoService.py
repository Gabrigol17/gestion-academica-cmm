from flask import current_app

class AcudienteCorreoService:

    def add(self, id_acudiente, correo):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO AcudienteCorreo (id_acudiente, correo) VALUES (%s, %s)"
        c.execute(query, (id_acudiente, correo))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM AcudienteCorreo"
        c.execute(query)
        data = c.fetchall()
        correos = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return correos

    def update(self, id_acudiente_correo, id_acudiente, correo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE AcudienteCorreo SET id_acudiente = %s, correo = %s WHERE id_acudiente_correo = %s"
        c.execute(query, (id_acudiente, correo, id_acudiente_correo))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_acudiente_correo):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM AcudienteCorreo WHERE id_acudiente_correo = %s"
        c.execute(query, (id_acudiente_correo,))
        current_app.mysql.connection.commit()
        c.close()

