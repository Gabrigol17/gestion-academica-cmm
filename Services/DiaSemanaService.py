from flask import current_app

from Models.DiaSemana import DiaSemana

class DiaSemanaService:

    def crear(self, dia_sem_dia):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_DIA_SEMANA "
            "(DIA_SEM_DIA) "
            "VALUES (%s)"
        )

        cursor.execute(query, (dia_sem_dia,))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DIA_SEMANA"
        cursor.execute(query)

        data = cursor.fetchall()

        dias = [DiaSemana(col[0], col[1]).to_dict() for col in data]

        cursor.close()
        return dias

    def obtener_por_id(self, dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DIA_SEMANA WHERE DIA_SEM_ID = %s"
        cursor.execute(query, (dia_sem_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            dia = DiaSemana(data[0], data[1]).to_dict()
            return dia
        else:
            return None

    def actualizar(self, dia_sem_dia, dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_DIA_SEMANA "
            "SET DIA_SEM_DIA = %s "
            "WHERE DIA_SEM_ID = %s"
        )
        cursor.execute(query, (dia_sem_dia, dia_sem_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_DIA_SEMANA WHERE DIA_SEM_ID = %s"
        cursor.execute(query, (dia_sem_id,))

        current_app.mysql.connection.commit()
        cursor.close()
