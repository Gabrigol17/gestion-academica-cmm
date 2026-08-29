from flask import current_app

class PersonaService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Persona (id_rol, documento, nombre, apellido, correo, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
        params = (data.get('id_rol'), data.get('documento'), data.get('nombre'), data.get('apellido'), data.get('correo'), data.get('telefono'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_persona, data):
        db = current_app.db
        query = "UPDATE Persona SET id_rol = %s, documento = %s, nombre = %s, apellido = %s, correo = %s, telefono = %s WHERE id_persona = %s"
        params = (data.get('id_rol'), data.get('documento'), data.get('nombre'), data.get('apellido'), data.get('correo'), data.get('telefono'), id_persona)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_persona):
        db = current_app.db
        query = "DELETE FROM Persona WHERE id_persona = %s"
        return db.execute_query(query, (id_persona,), commit=True)

    def read(self, id_persona=None):
        db = current_app.db
        if id_persona:
            query = "SELECT * FROM Persona WHERE id_persona = %s"
            return db.fetch_one(query, (id_persona,))
        else:
            query = "SELECT * FROM Persona"
            return db.fetch_all(query)