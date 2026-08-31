from flask import current_app

class ActividadEvaluativaService:

    def crear(self, act_eva_uuid, act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id):
        # 1. Abrimos el cursor para interactuar con la base de datos desde Flask
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Sentencia SQL estructurada sin sangría dentro del string para evitar marcas rojas
        query = (
            "INSERT INTO T_ACTIVIDAD_EVALUATIVA "
            "(ACT_EVA_UUID, ACT_EVA_NOMBRE, ACT_EVA_DESCRIPCION, ACT_EVA_ASIG_ACA_ID, ACT_EVA_COM_EVA_ID) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        # 3. Pasamos los parámetros en una tupla para evitar inyección SQL
        cursor.execute(query, (act_eva_uuid, act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id))
        
        # 4. Confirmamos y aplicamos los cambios en la base de datos
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor para liberar recursos de la conexión
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACTIVIDAD_EVALUATIVA"
        cursor.execute(query)
        
        # fetchall() extrae todas las filas devueltas por la consulta SQL
        data = cursor.fetchall()
        
        # Mapeamos cada tupla a un diccionario usando las llaves de cursor.description
        actividades = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        
        cursor.close()
        return actividades

    def obtener_por_id(self, act_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos la actividad filtrando por su llave primaria ACT_EVA_ID
        query = "SELECT * FROM T_ACTIVIDAD_EVALUATIVA WHERE ACT_EVA_ID = %s"
        cursor.execute(query, (act_eva_id,))
        
        # fetchone() devuelve únicamente el primer registro encontrado
        data = cursor.fetchone()
        cursor.close()
        
        # Retorna el diccionario si se encontró el registro, o None si no existe
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, act_eva_id, act_eva_uuid, act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia UPDATE formateada sin saltos de línea con espacios vacíos
        query = (
            "UPDATE T_ACTIVIDAD_EVALUATIVA "
            "SET ACT_EVA_UUID = %s, ACT_EVA_NOMBRE = %s, ACT_EVA_DESCRIPCION = %s, "
            "ACT_EVA_ASIG_ACA_ID = %s, ACT_EVA_COM_EVA_ID = %s "
            "WHERE ACT_EVA_ID = %s"
        )
        cursor.execute(query, (act_eva_uuid, act_eva_nombre, act_eva_descripcion, act_eva_asig_aca_id, act_eva_com_eva_id, act_eva_id))
        
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