from flask import current_app

class RolModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Rol (nombre_rol) VALUES (%s)"
        params = (data.get('nombre_rol'),)
        return db.execute_query(query, params, commit=True)

    def update(self, id_rol, data):
        db = current_app.db
        query = "UPDATE Rol SET nombre_rol = %s WHERE id_rol = %s"
        params = (data.get('nombre_rol'), id_rol)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_rol):
        db = current_app.db
        query = "DELETE FROM Rol WHERE id_rol = %s"
        return db.execute_query(query, (id_rol,), commit=True)

    def read(self, id_rol=None):
        db = current_app.db
        if id_rol:
            query = "SELECT * FROM Rol WHERE id_rol = %s"
            return db.fetch_one(query, (id_rol,))
        else:
            query = "SELECT * FROM Rol"
            return db.fetch_all(query)