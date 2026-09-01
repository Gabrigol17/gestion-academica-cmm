from flask import current_app

from Models.CursoVigencia import CursoVigencia

class CursoVigenciaService:

    def crear(self, cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_CURSO_VIGENCIA "
            "(CUR_VIG_UUID, CUR_VIG_LETRA, CUR_VIG_VIG_ID, CUR_VIG_GRAD_ID) "
            "VALUES (UUID(), %s, %s, %s)"
        )

        cursor.execute(query, (cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_CURSO_VIGENCIA"
        cursor.execute(query)

        data = cursor.fetchall()

        cursos = [CursoVigencia(col[0], col[1], col[2], col[3], col[4]).to_dict() for col in data]

        cursor.close()
        return cursos

    def obtener_por_id(self, cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_CURSO_VIGENCIA WHERE CUR_VIG_ID = %s"
        cursor.execute(query, (cur_vig_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            curso = CursoVigencia(data[0], data[1], data[2], data[3], data[4]).to_dict()
            return curso
        else:
            return None

    def actualizar(self, cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id, cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_CURSO_VIGENCIA "
            "SET CUR_VIG_LETRA = %s, CUR_VIG_VIG_ID = %s, CUR_VIG_GRAD_ID = %s "
            "WHERE CUR_VIG_ID = %s"
        )
        cursor.execute(query, (cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id, cur_vig_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_CURSO_VIGENCIA WHERE CUR_VIG_ID = %s"
        cursor.execute(query, (cur_vig_id,))

        current_app.mysql.connection.commit()
        cursor.close()
