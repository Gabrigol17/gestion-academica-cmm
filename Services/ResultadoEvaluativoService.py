from flask import current_app

class ResultadoEvaluativoService:

    def crear(self, res_eva_nota, res_eva_observacion, res_eva_est_id, res_eva_act_eva_id):
        # 1. Conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Registramos la nota obtenida por el estudiante en la actividad
        query = (
            "INSERT INTO T_RESULTADO_EVALUATIVO "
            "(RES_EVA_NOTA, RES_EVA_OBSERVACION, RES_EVA_EST_ID, RES_EVA_ACT_EVA_ID) "
            "VALUES (%s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos pasándole la tupla de datos
        cursor.execute(query, (res_eva_nota, res_eva_observacion, res_eva_est_id, res_eva_act_eva_id))
        
        # 4. Guardamos la transacción en MySQL
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_RESULTADO_EVALUATIVO"
        cursor.execute(query)
        
        data = cursor.fetchall()
        resultados = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return resultados

    def obtener_por_id(self, res_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos la nota registrada por RES_EVA_ID
        query = "SELECT * FROM T_RESULTADO_EVALUATIVO WHERE RES_EVA_ID = %s"
        cursor.execute(query, (res_eva_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, res_eva_id, res_eva_nota, res_eva_observacion, res_eva_est_id, res_eva_act_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos la nota u observación
        query = (
            "UPDATE T_RESULTADO_EVALUATIVO "
            "SET RES_EVA_NOTA = %s, RES_EVA_OBSERVACION = %s, "
            "RES_EVA_EST_ID = %s, RES_EVA_ACT_EVA_ID = %s "
            "WHERE RES_EVA_ID = %s"
        )
        cursor.execute(query, (res_eva_nota, res_eva_observacion, res_eva_est_id, res_eva_act_eva_id, res_eva_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, res_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos la nota registrada
        query = "DELETE FROM T_RESULTADO_EVALUATIVO WHERE RES_EVA_ID = %s"
        cursor.execute(query, (res_eva_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()