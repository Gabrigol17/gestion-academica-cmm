from flask import current_app

from Models.PeriodoAcademico import PeriodoAcademico

class PeriodoAcademicoService:

    def crear(self, per_aca_numero, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_PERIODO_ACADEMICO "
            "(PER_ACA_UUID, PER_ACA_NUMERO, PER_ACA_FECHA_INICIO, PER_ACA_FECHA_FIN, PER_ACA_VIG_ID) "
            "VALUES (UUID(), %s, %s, %s, %s)"
        )

        cursor.execute(query, (per_aca_numero, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_PERIODO_ACADEMICO"
        cursor.execute(query)

        data = cursor.fetchall()

        periodos = [PeriodoAcademico(col[0], col[1], col[2], col[3], col[4], col[5]).to_dict() for col in data]

        cursor.close()
        return periodos

    def obtener_por_id(self, per_aca_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_PERIODO_ACADEMICO WHERE PER_ACA_ID = %s"
        cursor.execute(query, (per_aca_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            periodo = PeriodoAcademico(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()
            return periodo
        else:
            return None

    def actualizar(self, per_aca_numero, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id, per_aca_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_PERIODO_ACADEMICO "
            "SET PER_ACA_NUMERO = %s, PER_ACA_FECHA_INICIO = %s, "
            "PER_ACA_FECHA_FIN = %s, PER_ACA_VIG_ID = %s "
            "WHERE PER_ACA_ID = %s"
        )
        cursor.execute(query, (per_aca_numero, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id, per_aca_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, per_aca_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_PERIODO_ACADEMICO WHERE PER_ACA_ID = %s"
        cursor.execute(query, (per_aca_id,))

        current_app.mysql.connection.commit()
        cursor.close()
