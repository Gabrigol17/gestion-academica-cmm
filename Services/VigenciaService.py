from flask import current_app

from Models.Vigencia import Vigencia

class VigenciaService:

    def crear(self, vig_anio):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_VIGENCIA "
            "(VIG_UUID, VIG_ANIO) "
            "VALUES (UUID(), %s)"
        )

        cursor.execute(query, (vig_anio,))

        nuevo_id = cursor.lastrowid

        current_app.mysql.connection.commit()
        cursor.close()

        return self.obtener_por_id(nuevo_id)

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_VIGENCIA"
        cursor.execute(query)

        data = cursor.fetchall()

        vigencias = [Vigencia(col[0], col[1], col[2]).to_dict() for col in data]

        cursor.close()
        return vigencias

    def obtener_por_id(self, vig_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_VIGENCIA WHERE VIG_ID = %s"
        cursor.execute(query, (vig_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            vigencia = Vigencia(data[0], data[1], data[2]).to_dict()
            return vigencia
        else:
            return None

    def actualizar(self, vig_anio, vig_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_VIGENCIA "
            "SET VIG_ANIO = %s "
            "WHERE VIG_UUID = %s"
        )
        cursor.execute(query, (vig_anio, vig_uuid))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0

    def eliminar(self, vig_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_VIGENCIA WHERE VIG_UUID = %s"
        cursor.execute(query, (vig_uuid,))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0
