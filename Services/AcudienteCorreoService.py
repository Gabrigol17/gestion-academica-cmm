from flask import current_app

from Models.AcudienteCorreo import AcudienteCorreo

class AcudienteCorreoService:

    def crear(self, acu_corr_acu_id, acu_corr_correo):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ACUDIENTE_CORREO "
            "(ACU_CORR_UUID, ACU_CORR_ACU_ID, ACU_CORR_CORREO) "
            "VALUES (UUID(), %s, %s)"
        )

        cursor.execute(query, (acu_corr_acu_id, acu_corr_correo))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_CORREO"
        cursor.execute(query)

        data = cursor.fetchall()

        correos = [AcudienteCorreo(col[0], col[1], col[2], col[3]).to_dict() for col in data]

        cursor.close()
        return correos

    def obtener_por_id(self, acu_corr_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_CORREO WHERE ACU_CORR_ID = %s"
        cursor.execute(query, (acu_corr_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            correo = AcudienteCorreo(data[0], data[1], data[2], data[3]).to_dict()
            return correo
        else:
            return None

    def actualizar(self, acu_corr_acu_id, acu_corr_correo, acu_corr_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ACUDIENTE_CORREO "
            "SET ACU_CORR_ACU_ID = %s, ACU_CORR_CORREO = %s "
            "WHERE ACU_CORR_ID = %s"
        )
        cursor.execute(query, (acu_corr_acu_id, acu_corr_correo, acu_corr_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_corr_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ACUDIENTE_CORREO WHERE ACU_CORR_ID = %s"
        cursor.execute(query, (acu_corr_id,))

        current_app.mysql.connection.commit()
        cursor.close()
