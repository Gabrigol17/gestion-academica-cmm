from flask import current_app

from Models.CursoVigencia import CursoVigencia

class CursoService:

    def crear(self, cur_nombre, cur_descripcion):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_CURSO "
            "(CUR_UUID, CUR_NOMBRE, CUR_DESCRIPCION) "
            "VALUES (UUID(), %s, %s)"
        )

        cursor.execute(query, (cur_nombre, cur_descripcion))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_CURSO"
        cursor.execute(query)

        data = cursor.fetchall()

        cursos = [CursoVigencia(col[0], col[1], col[2], col[3], col[4]).to_dict() for col in data]

        cursor.close()
        return cursos

    def obtener_por_id(self, cur_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_CURSO WHERE CUR_ID = %s"
        cursor.execute(query, (cur_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            curso = CursoVigencia(data[0], data[1], data[2], data[3], data[4]).to_dict()
            return curso
        else:
            return None

    def actualizar(self, cur_nombre, cur_descripcion, cur_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_CURSO "
            "SET CUR_NOMBRE = %s, CUR_DESCRIPCION = %s "
            "WHERE CUR_ID = %s"
        )
        cursor.execute(query, (cur_nombre, cur_descripcion, cur_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, cur_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_CURSO WHERE CUR_ID = %s"
        cursor.execute(query, (cur_id,))

        current_app.mysql.connection.commit()
        cursor.close()
