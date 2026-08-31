from flask import current_app

class AcudienteTelefonoService:

    def crear(self, acu_tel_uuid, acu_tel_acu_id, acu_tel_numero):
        # 1. Creamos el cursor de conexión
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Sentencia SQL de inserción
        query = (
            "INSERT INTO T_ACUDIENTE_TELEFONO "
            "(ACU_TEL_UUID, ACU_TEL_ACU_ID, ACU_TEL_NUMERO) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Pasamos los parámetros
        cursor.execute(query, (acu_tel_uuid, acu_tel_acu_id, acu_tel_numero))
        
        # 4. Confirmamos la transacción
        current_app.mysql.connection.commit()
        
        # 5. Cerramos conexión
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_TELEFONO"
        cursor.execute(query)
        
        # Mapeamos los teléfonos registrados
        data = cursor.fetchall()
        telefonos = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return telefonos

    def obtener_por_id(self, acu_tel_id):
        cursor = current_app.mysql.connection.cursor()
        # Obtenemos el teléfono por su ID
        query = "SELECT * FROM T_ACUDIENTE_TELEFONO WHERE ACU_TEL_ID = %s"
        cursor.execute(query, (acu_tel_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, acu_tel_id, acu_tel_uuid, acu_tel_acu_id, acu_tel_numero):
        cursor = current_app.mysql.connection.cursor()
        # Sentencia UPDATE para actualizar el número telefónico
        query = (
            "UPDATE T_ACUDIENTE_TELEFONO "
            "SET ACU_TEL_UUID = %s, ACU_TEL_ACU_ID = %s, ACU_TEL_NUMERO = %s "
            "WHERE ACU_TEL_ID = %s"
        )
        cursor.execute(query, (acu_tel_uuid, acu_tel_acu_id, acu_tel_numero, acu_tel_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_tel_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos el número telefónico por ID
        query = "DELETE FROM T_ACUDIENTE_TELEFONO WHERE ACU_TEL_ID = %s"
        cursor.execute(query, (acu_tel_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()