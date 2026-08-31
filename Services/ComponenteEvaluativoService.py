from flask import current_app

class ComponenteEvaluativoService:

    def crear(self, com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id):
        # 1. Iniciamos conexión mediante cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos el componente evaluativo con su porcentaje correspondiente
        query = (
            "INSERT INTO T_COMPONENTE_EVALUATIVO "
            "(COM_EVA_PORCENTAJE, COM_EVA_PER_ACA_ID, COM_EVA_TIPO_COMP_ID) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Pasamos los parámetros
        cursor.execute(query, (com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id))
        
        # 4. Confirmamos la inserción
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_COMPONENTE_EVALUATIVO"
        cursor.execute(query)
        
        data = cursor.fetchall()
        componentes = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return componentes

    def obtener_por_id(self, com_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos componente por COM_EVA_ID
        query = "SELECT * FROM T_COMPONENTE_EVALUATIVO WHERE COM_EVA_ID = %s"
        cursor.execute(query, (com_eva_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, com_eva_id, com_eva_porcentaje, com_eva_per_aca_id, com_eva_tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos los valores del componente evaluativo
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
        # Borramos el componente por ID
        query = "DELETE FROM T_COMPONENTE_EVALUATIVO WHERE COM_EVA_ID = %s"
        cursor.execute(query, (com_eva_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()

