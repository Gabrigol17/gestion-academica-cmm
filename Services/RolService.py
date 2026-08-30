from flask import current_app

class RolService:

    def add(self, nombre_rol):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO Rol (nombre_rol) VALUES (%s)"
        c.execute(query, (nombre_rol,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM Rol"
        c.execute(query)
        data = c.fetchall()
        roles = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return roles

    def update(self, id_rol, nombre_rol):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE Rol SET nombre_rol = %s WHERE id_rol = %s"
        c.execute(query, (nombre_rol, id_rol))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_rol):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM Rol WHERE id_rol = %s"
        c.execute(query, (id_rol,))
        current_app.mysql.connection.commit()
        c.close()
