from flask import current_app

from Models.Estudiante import Estudiante

class EstudianteService:

    def crear(self, est_estado_institucional, est_per_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ESTUDIANTE "
            "(EST_UUID, EST_ESTADO_INSTITUCIONAL, EST_PER_ID) "
            "VALUES (UUID(), %s, %s)"
        )

        cursor.execute(query, (est_estado_institucional, est_per_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ESTUDIANTE"
        cursor.execute(query)

        data = cursor.fetchall()

        estudiantes = [Estudiante(col[0], col[1], col[2], col[3]).to_dict() for col in data]

        cursor.close()
        return estudiantes

    def obtener_por_id(self, est_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ESTUDIANTE WHERE EST_ID = %s"
        cursor.execute(query, (est_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            estudiante = Estudiante(data[0], data[1], data[2], data[3]).to_dict()
            return estudiante
        else:
            return None

    def actualizar(self, est_estado_institucional, est_per_id, est_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ESTUDIANTE "
            "SET EST_ESTADO_INSTITUCIONAL = %s, EST_PER_ID = %s "
            "WHERE EST_ID = %s"
        )
        cursor.execute(query, (est_estado_institucional, est_per_id, est_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, est_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ESTUDIANTE WHERE EST_ID = %s"
        cursor.execute(query, (est_id,))

        current_app.mysql.connection.commit()
        cursor.close()
