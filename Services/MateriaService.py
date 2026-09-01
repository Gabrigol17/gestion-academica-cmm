from flask import current_app

from Models.Materia import Materia

class MateriaService:

    def crear(self, mat_nombre):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_MATERIA "
            "(MAT_NOMBRE) "
            "VALUES (%s)"
        )

        cursor.execute(query, (mat_nombre,))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_MATERIA"
        cursor.execute(query)

        data = cursor.fetchall()

        materias = [Materia(col[0], col[1]).to_dict() for col in data]

        cursor.close()
        return materias

    def obtener_por_id(self, mat_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_MATERIA WHERE MAT_ID = %s"
        cursor.execute(query, (mat_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            materia = Materia(data[0], data[1]).to_dict()
            return materia
        else:
            return None

    def actualizar(self, mat_nombre, mat_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_MATERIA "
            "SET MAT_NOMBRE = %s "
            "WHERE MAT_ID = %s"
        )
        cursor.execute(query, (mat_nombre, mat_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, mat_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_MATERIA WHERE MAT_ID = %s"
        cursor.execute(query, (mat_id,))

        current_app.mysql.connection.commit()
        cursor.close()
