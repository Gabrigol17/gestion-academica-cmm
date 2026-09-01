from flask import current_app

from Models.ActividadEvaluativa import ActividadEvaluativa

class ActividadEvaluativaService:

    def crear(self, act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id):
        cursor = current_app.mysql.connection.cursor()
        
        query = (
            "INSERT INTO T_ACTIVIDAD_EVALUATIVA "
            "(ACT_EVA_UUID, ACT_EVA_NOMBRE, ACT_EVA_DESCRIPCION, ACT_EVA_ASIG_ACA_ID, ACT_EVA_COM_EVA_ID) "
            "VALUES (UUID(), %s, %s, %s, %s)"
        )

        cursor.execute(query, (act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id))
        current_app.mysql.connection.commit()
        cursor.close()


    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACTIVIDAD_EVALUATIVA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        
        actividades = [ActividadEvaluativa(col[0], col[1], col[2], col[3], col[4], col[5]).to_dict() for col in data]
        
        cursor.close()
        return actividades

    def obtener_por_id(self, act_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos la actividad filtrando por su llave primaria ACT_EVA_ID
        query = "SELECT * FROM T_ACTIVIDAD_EVALUATIVA WHERE ACT_EVA_ID = %s"
        cursor.execute(query, (act_eva_id,))
        
        data = cursor.fetchone()
        cursor.close()
        if data:
            actividad = ActividadEvaluativa(data[0], data[1], data[2], data[3], data[4], data[5]).to_dict()
            return actividad
        else:
            return None

    def actualizar(self, act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id, act_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
        "UPDATE T_ACTIVIDAD_EVALUATIVA "
        "SET ACT_EVA_NOMBRE = %s, "
        "ACT_EVA_DESCRIPCION = %s, "
        "ACT_EVA_ASIG_ACA_ID = %s, "
        "ACT_EVA_COM_EVA_ID = %s "
        "WHERE ACT_EVA_ID = %s"
    )
        cursor.execute(query, (act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id, act_eva_id))
        
        # Confirmamos la actualización en MySQL
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, act_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia DELETE para borrar la fila por su ID
        query = "DELETE FROM T_ACTIVIDAD_EVALUATIVA WHERE ACT_EVA_ID = %s"
        cursor.execute(query, (act_eva_id,))
        
        # Confirmamos la eliminación en la base de datos
        current_app.mysql.connection.commit()
        cursor.close()