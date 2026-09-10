from flask import current_app

from Models.Rol import Rol

class RolService:

    def crear(self, rol_nombre):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ROL "
            "(ROL_UUID, ROL_NOMBRE) "
            "VALUES (UUID(), %s)"
        )

        cursor.execute(query, (rol_nombre,))

        nuevo_id = cursor.lastrowid

        current_app.mysql.connection.commit()
        cursor.close()

        return self.obtener_por_id(nuevo_id)

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ROL"
        cursor.execute(query)

        data = cursor.fetchall()

        roles = [Rol(col[0], col[1], col[2]).to_dict() for col in data]

        cursor.close()
        return roles

    def obtener_por_id(self, rol_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ROL WHERE ROL_ID = %s"
        cursor.execute(query, (rol_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            rol = Rol(data[0], data[1], data[2]).to_dict()
            return rol
        else:
            return None

    def actualizar(self, rol_nombre, rol_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ROL "
            "SET ROL_NOMBRE = %s "
            "WHERE ROL_UUID = %s"
        )
        cursor.execute(query, (rol_nombre, rol_uuid))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0

    def eliminar(self, rol_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ROL WHERE ROL_UUID = %s"
        cursor.execute(query, (rol_uuid,))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0
