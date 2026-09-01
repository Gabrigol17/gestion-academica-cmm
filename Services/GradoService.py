from flask import current_app

from Models.Grado import Grado

class GradoService:

    def crear(self, grad_nombre, grad_niv_edu_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_GRADO "
            "(GRAD_NOMBRE, GRAD_NIV_EDU_ID) "
            "VALUES (%s, %s)"
        )

        cursor.execute(query, (grad_nombre, grad_niv_edu_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_GRADO"
        cursor.execute(query)

        data = cursor.fetchall()

        grados = [Grado(col[0], col[1], col[2]).to_dict() for col in data]

        cursor.close()
        return grados

    def obtener_por_id(self, grad_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_GRADO WHERE GRAD_ID = %s"
        cursor.execute(query, (grad_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            grado = Grado(data[0], data[1], data[2]).to_dict()
            return grado
        else:
            return None

    def actualizar(self, grad_nombre, grad_niv_edu_id, grad_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_GRADO "
            "SET GRAD_NOMBRE = %s, GRAD_NIV_EDU_ID = %s "
            "WHERE GRAD_ID = %s"
        )
        cursor.execute(query, (grad_nombre, grad_niv_edu_id, grad_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, grad_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_GRADO WHERE GRAD_ID = %s"
        cursor.execute(query, (grad_id,))

        current_app.mysql.connection.commit()
        cursor.close()
