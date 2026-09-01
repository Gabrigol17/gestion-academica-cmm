from flask import current_app

from Models.AcudienteTelefono import AcudienteTelefono

class AcudienteTelefonoService:

    def crear(self, acu_tel_acu_id, acu_tel_numero):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ACUDIENTE_TELEFONO "
            "(ACU_TEL_UUID, ACU_TEL_ACU_ID, ACU_TEL_NUMERO) "
            "VALUES (UUID(), %s, %s)"
        )

        cursor.execute(query, (acu_tel_acu_id, acu_tel_numero))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_TELEFONO"
        cursor.execute(query)

        data = cursor.fetchall()

        telefonos = [AcudienteTelefono(col[0], col[1], col[2], col[3]).to_dict() for col in data]

        cursor.close()
        return telefonos

    def obtener_por_id(self, acu_tel_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_TELEFONO WHERE ACU_TEL_ID = %s"
        cursor.execute(query, (acu_tel_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            telefono = AcudienteTelefono(data[0], data[1], data[2], data[3]).to_dict()
            return telefono
        else:
            return None

    def actualizar(self, acu_tel_acu_id, acu_tel_numero, acu_tel_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ACUDIENTE_TELEFONO "
            "SET ACU_TEL_ACU_ID = %s, ACU_TEL_NUMERO = %s "
            "WHERE ACU_TEL_ID = %s"
        )
        cursor.execute(query, (acu_tel_acu_id, acu_tel_numero, acu_tel_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_tel_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ACUDIENTE_TELEFONO WHERE ACU_TEL_ID = %s"
        cursor.execute(query, (acu_tel_id,))

        current_app.mysql.connection.commit()
        cursor.close()
