from flask import current_app

class PersonaService:

    def add(self, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento, id_rol):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Persona (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento, id_rol) VALUES (%s, %s, %s, %s, %s, %s)"
        c.execute(query, (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento, id_rol))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Persona"
        c.execute(query)
        data = c.fetchall()
        personas = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return personas

    def update(self, id_persona, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento, id_rol):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Persona SET primer_nombre = %s, segundo_nombre = %s, primer_apellido = %s, segundo_apellido = %s, documento = %s, id_rol = %s WHERE id_persona = %s"
        c.execute(query, (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, documento, id_rol, id_persona))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_persona):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Persona WHERE id_persona = %s"
        c.execute(query, (id_persona,))
        current_app.mysql.connection.commit()
        c.close()
