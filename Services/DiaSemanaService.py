from flask import current_app

from Models.DiaSemana import DiaSemana

class DiaSemanaService:

    def crear(self, dia_sem_dia):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_DIA_SEMANA "
            "(DIA_SEM_UUID, DIA_SEM_DIA) "
            "VALUES (REPLACE(UUID(), '-', ''), %s)"
        )

        cursor.execute(query, (dia_sem_dia,))

        nuevo_id = cursor.lastrowid

        current_app.mysql.connection.commit()
        cursor.close()

        return self.obtener_por_id(nuevo_id)

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DIA_SEMANA"
        cursor.execute(query)

        data = cursor.fetchall()

        dias = [DiaSemana(col[0], col[1], col[2]).to_dict() for col in data]

        cursor.close()
        return dias

    def obtener_por_id(self, dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DIA_SEMANA WHERE DIA_SEM_ID = %s"
        cursor.execute(query, (dia_sem_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            dia = DiaSemana(data[0], data[1], data[2]).to_dict()
            return dia
        else:
            return None

    def actualizar(self, dia_sem_dia, dia_sem_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_DIA_SEMANA "
            "SET DIA_SEM_DIA = %s "
            "WHERE DIA_SEM_UUID = %s"
        )
        cursor.execute(query, (dia_sem_dia, dia_sem_uuid))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0

    def eliminar(self, dia_sem_uuid):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_DIA_SEMANA WHERE DIA_SEM_UUID = %s"
        cursor.execute(query, (dia_sem_uuid,))

        current_app.mysql.connection.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0
