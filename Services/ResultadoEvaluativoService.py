from flask import current_app

from Models.ResultadoEvaluativo import ResultadoEvaluativo

class ResultadoEvaluativoService:

    def crear(self, res_eva_nota, res_eva_ajuste, res_eva_observacion, res_eva_mat_id, res_eva_act_eva_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_RESULTADO_EVALUATIVO "
            "(RES_EVA_UUID, RES_EVA_NOTA, RES_EVA_AJUSTE, RES_EVA_OBSERVACION, RES_EVA_MAT_ID, RES_EVA_ACT_EVA_ID) "
            "VALUES (UUID(), %s, %s, %s, %s, %s)"
        )

        cursor.execute(query, (res_eva_nota, res_eva_ajuste, res_eva_observacion, res_eva_mat_id, res_eva_act_eva_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_RESULTADO_EVALUATIVO"
        cursor.execute(query)

        data = cursor.fetchall()

        resultados = [ResultadoEvaluativo(col[0], col[1], col[2], col[3], col[4], col[5], col[6]).to_dict() for col in data]

        cursor.close()
        return resultados

    def obtener_por_id(self, res_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_RESULTADO_EVALUATIVO WHERE RES_EVA_ID = %s"
        cursor.execute(query, (res_eva_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            resultado = ResultadoEvaluativo(data[0], data[1], data[2], data[3], data[4], data[5], data[6]).to_dict()
            return resultado
        else:
            return None

    def actualizar(self, res_eva_nota, res_eva_ajuste, res_eva_observacion, res_eva_mat_id, res_eva_act_eva_id, res_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_RESULTADO_EVALUATIVO "
            "SET RES_EVA_NOTA = %s, RES_EVA_AJUSTE = %s, RES_EVA_OBSERVACION = %s, "
            "RES_EVA_MAT_ID = %s, RES_EVA_ACT_EVA_ID = %s "
            "WHERE RES_EVA_ID = %s"
        )
        cursor.execute(query, (res_eva_nota, res_eva_ajuste, res_eva_observacion, res_eva_mat_id, res_eva_act_eva_id, res_eva_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, res_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_RESULTADO_EVALUATIVO WHERE RES_EVA_ID = %s"
        cursor.execute(query, (res_eva_id,))

        current_app.mysql.connection.commit()
        cursor.close()
