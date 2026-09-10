from flask import current_app

from Models.Acudiente import Acudiente

class AcudienteService:

    def crear(self, acu_nombres, acu_apellidos, acu_estado):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ACUDIENTE "
            "(ACU_UUID, ACU_NOMBRES, ACU_APELLIDOS, ACU_ESTADO) "
            "VALUES (UUID(), %s, %s, %s)"
        )

        cursor.execute(query, (acu_nombres, acu_apellidos, acu_estado))

        nuevo_id = cursor.lastrowid

        current_app.mysql.connection.commit()
        cursor.close()

        return self.obtener_por_id(nuevo_id)

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE"
        cursor.execute(query)

        data = cursor.fetchall()

        acudientes = [Acudiente(col[0], col[1], col[2], col[3], col[4]).to_dict() for col in data]

        cursor.close()
        return acudientes

    def obtener_por_id(self, acu_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE WHERE ACU_ID = %s"
        cursor.execute(query, (acu_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            acudiente = Acudiente(data[0], data[1], data[2], data[3], data[4]).to_dict()
            return acudiente
        else:
            return None

    def actualizar(self, acu_nombres, acu_apellidos, acu_estado, acu_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ACUDIENTE "
            "SET ACU_NOMBRES = %s, ACU_APELLIDOS = %s, ACU_ESTADO = %s "
            "WHERE ACU_UUID = %s"
        )
        cursor.execute(query, (acu_nombres, acu_apellidos, acu_estado, acu_uuid))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0

    def eliminar(self, acu_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ACUDIENTE WHERE ACU_UUID = %s"
        cursor.execute(query, (acu_uuid,))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0
