from flask import current_app

from Models.ComponenteEvaluativo import ComponenteEvaluativo

class ComponenteEvaluativoService:

    def crear(self, com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_COMPONENTE_EVALUATIVO "
            "(COM_EVA_PORCENTAJE, COM_EVA_PER_ACA_ID, COM_EVA_TIPO_COMP_ID) "
            "VALUES (%s, %s, %s)"
        )

        cursor.execute(query, (com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_COMPONENTE_EVALUATIVO"
        cursor.execute(query)

        data = cursor.fetchall()

        componentes = [ComponenteEvaluativo(col[0], col[1], col[2], col[3]).to_dict() for col in data]

        cursor.close()
        return componentes

    def obtener_por_id(self, com_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_COMPONENTE_EVALUATIVO WHERE COM_EVA_ID = %s"
        cursor.execute(query, (com_eva_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            componente = ComponenteEvaluativo(data[0], data[1], data[2], data[3]).to_dict()
            return componente
        else:
            return None

    def actualizar(self, com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id, com_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_COMPONENTE_EVALUATIVO "
            "SET COM_EVA_PORCENTAJE = %s, COM_EVA_PER_ACA_ID = %s, COM_EVA_TIPO_COMP_ID = %s "
            "WHERE COM_EVA_ID = %s"
        )
        cursor.execute(query, (com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id, com_eva_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, com_eva_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_COMPONENTE_EVALUATIVO WHERE COM_EVA_ID = %s"
        cursor.execute(query, (com_eva_id,))

        current_app.mysql.connection.commit()
        cursor.close()
