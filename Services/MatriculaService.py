from flask import current_app

from Models.Matricula import Matricula

class MatriculaService:

    def crear(self, matr_est_id, matr_cur_vig_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_MATRICULA "
            "(MATR_UUID, MATR_EST_ID, MATR_CUR_VIG_ID) "
            "VALUES (UUID(), %s, %s)"
        )

        cursor.execute(query, (matr_est_id, matr_cur_vig_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_MATRICULA"
        cursor.execute(query)

        data = cursor.fetchall()

        matriculas = [Matricula(col[0], col[1], col[2], col[3]).to_dict() for col in data]

        cursor.close()
        return matriculas

    def obtener_por_id(self, matr_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_MATRICULA WHERE MATR_ID = %s"
        cursor.execute(query, (matr_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            matricula = Matricula(data[0], data[1], data[2], data[3]).to_dict()
            return matricula
        else:
            return None

    def actualizar(self, matr_est_id, matr_cur_vig_id, matr_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_MATRICULA "
            "SET MATR_EST_ID = %s, MATR_CUR_VIG_ID = %s "
            "WHERE MATR_ID = %s"
        )
        cursor.execute(query, (matr_est_id, matr_cur_vig_id, matr_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, matr_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_MATRICULA WHERE MATR_ID = %s"
        cursor.execute(query, (matr_id,))

        current_app.mysql.connection.commit()
        cursor.close()
