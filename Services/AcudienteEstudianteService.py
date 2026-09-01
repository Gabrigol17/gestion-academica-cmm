from flask import current_app

from Models.AcudienteEstudiante import AcudienteEstudiante

class AcudienteEstudianteService:

    def crear(self, acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ACUDIENTE_ESTUDIANTE "
            "(ACU_EST_UUID, ACU_EST_PARENTESCO, ACU_EST_ACU_ID, ACU_EST_EST_ID, ACU_EST_ESPRINCIPAL) "
            "VALUES (UUID(), %s, %s, %s, %s)"
        )

        cursor.execute(query, (acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_ESTUDIANTE"
        cursor.execute(query)

        data = cursor.fetchall()

        resultados = [AcudienteEstudiante(col[0], col[1], col[2], col[3], col[4], col[5]).to_dict() for col in data]

        cursor.close()
        return resultados

    def obtener_por_id(self, acu_est_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_ESTUDIANTE WHERE ACU_EST_ID = %s"
        cursor.execute(query, (acu_est_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            resultado = AcudienteEstudiante(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()
            return resultado
        else:
            return None

    def actualizar(self, acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal, acu_est_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ACUDIENTE_ESTUDIANTE "
            "SET ACU_EST_PARENTESCO = %s, ACU_EST_ACU_ID = %s, "
            "ACU_EST_EST_ID = %s, ACU_EST_ESPRINCIPAL = %s "
            "WHERE ACU_EST_ID = %s"
        )
        cursor.execute(query, (acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal, acu_est_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_est_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ACUDIENTE_ESTUDIANTE WHERE ACU_EST_ID = %s"
        cursor.execute(query, (acu_est_id,))

        current_app.mysql.connection.commit()
        cursor.close()
