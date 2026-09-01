from flask import current_app

from Models.AsignacionAcademica import AsignacionAcademica

class AsignacionAcademicaService:

    def crear(self, asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_ASIGNACION_ACADEMICA "
            "(ASIG_ACA_UUID, ASIG_ACA_ESTADO, ASIG_ACA_DOC_ID, ASIG_ACA_MAT_ID, ASIG_ACA_CUR_VIG_ID) "
            "VALUES (UUID(), %s, %s, %s, %s)"
        )

        cursor.execute(query, (asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ASIGNACION_ACADEMICA"
        cursor.execute(query)

        data = cursor.fetchall()

        asignaciones = [AsignacionAcademica(col[0], col[1], col[2], col[3], col[4], col[5]).to_dict() for col in data]

        cursor.close()
        return asignaciones

    def obtener_por_id(self, asig_aca_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ASIGNACION_ACADEMICA WHERE ASIG_ACA_ID = %s"
        cursor.execute(query, (asig_aca_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            asignacion = AsignacionAcademica(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()
            return asignacion
        else:
            return None

    def actualizar(self, asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id, asig_aca_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ASIGNACION_ACADEMICA "
            "SET ASIG_ACA_ESTADO = %s, ASIG_ACA_DOC_ID = %s, "
            "ASIG_ACA_MAT_ID = %s, ASIG_ACA_CUR_VIG_ID = %s "
            "WHERE ASIG_ACA_ID = %s"
        )
        cursor.execute(query, (asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id, asig_aca_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, asig_aca_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ASIGNACION_ACADEMICA WHERE ASIG_ACA_ID = %s"
        cursor.execute(query, (asig_aca_id,))

        current_app.mysql.connection.commit()
        cursor.close()
