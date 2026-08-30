from flask import current_app

class AcudienteTelefonoService:

    def add(self, id_acudiente, telefono):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO AcudienteTelefono (id_acudiente, telefono) VALUES (%s, %s)"
        c.execute(query, (id_acudiente, telefono))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM AcudienteTelefono"
        c.execute(query)
        data = c.fetchall()
        telefonos = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return telefonos

    def update(self, id_acudiente_telefono, id_acudiente, telefono):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE AcudienteTelefono SET id_acudiente = %s, telefono = %s WHERE id_acudiente_telefono = %s"
        c.execute(query, (id_acudiente, telefono, id_acudiente_telefono))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_acudiente_telefono):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM AcudienteTelefono WHERE id_acudiente_telefono = %s"
        c.execute(query, (id_acudiente_telefono,))
        current_app.mysql.connection.commit()
        c.close()

