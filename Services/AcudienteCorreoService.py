from flask import current_app

class AcudienteCorreoService:

    def crear(self, acu_corr_uuid, acu_corr_acu_id, acu_corr_correo):
        # 1. Abrimos el cursor para conectarnos a MySQL desde Flask
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Definimos la consulta INSERT limpia sin sangría interna
        query = (
            "INSERT INTO T_ACUDIENTE_CORREO "
            "(ACU_CORR_UUID, ACU_CORR_ACU_ID, ACU_CORR_CORREO) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Ejecutamos enviando los valores en una tupla
        cursor.execute(query, (acu_corr_uuid, acu_corr_acu_id, acu_corr_correo))
        
        # 4. Guardamos los cambios permanentemente en la base de datos
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_CORREO"
        cursor.execute(query)
        
        # fetchall() obtiene todas las filas devueltas
        data = cursor.fetchall()
        
        # Mapeamos las tuplas a diccionarios usando los nombres de las columnas
        correos = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        
        cursor.close()
        return correos

    def obtener_por_id(self, acu_corr_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos filtrando por la clave primaria ACU_CORR_ID
        query = "SELECT * FROM T_ACUDIENTE_CORREO WHERE ACU_CORR_ID = %s"
        cursor.execute(query, (acu_corr_id,))
        
        # fetchone() recupera una sola coincidencia
        data = cursor.fetchone()
        cursor.close()
        
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, acu_corr_id, acu_corr_uuid, acu_corr_acu_id, acu_corr_correo):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia UPDATE para actualizar la fila
        query = (
            "UPDATE T_ACUDIENTE_CORREO "
            "SET ACU_CORR_UUID = %s, ACU_CORR_ACU_ID = %s, ACU_CORR_CORREO = %s "
            "WHERE ACU_CORR_ID = %s"
        )
        cursor.execute(query, (acu_corr_uuid, acu_corr_acu_id, acu_corr_correo, acu_corr_id))
        
        # Confirmamos los cambios
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_corr_id):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia DELETE para remover por ID
        query = "DELETE FROM T_ACUDIENTE_CORREO WHERE ACU_CORR_ID = %s"
        cursor.execute(query, (acu_corr_id,))
        
        # Confirmamos la eliminación
        current_app.mysql.connection.commit()
        cursor.close()

