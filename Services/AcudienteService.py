from flask import current_app

class AcudienteService:

    def crear(self, acu_uuid, acu_nombres, acu_apellidos, acu_estado):
        # 1. Abrimos conexión con el cursor de MySQL
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Sentencia INSERT para la tabla T_ACUDIENTE
        query = (
            "INSERT INTO T_ACUDIENTE "
            "(ACU_UUID, ACU_NOMBRES, ACU_APELLIDOS, ACU_ESTADO) "
            "VALUES (%s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos enviando los datos del acudiente
        cursor.execute(query, (acu_uuid, acu_nombres, acu_apellidos, acu_estado))
        
        # 4. Guardamos los cambios permanentemente
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE"
        cursor.execute(query)
        
        # Extraemos todas las filas devueltas por la base de datos
        data = cursor.fetchall()
        
        # Convertimos las tuplas recibidas en diccionarios llave: valor
        acudientes = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        
        cursor.close()
        return acudientes

    def obtener_por_id(self, acu_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos un acudiente por su clave primaria ACU_ID
        query = "SELECT * FROM T_ACUDIENTE WHERE ACU_ID = %s"
        cursor.execute(query, (acu_id,))
        
        # fetchone() obtiene únicamente el registro encontrado
        data = cursor.fetchone()
        cursor.close()
        
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, acu_id, acu_uuid, acu_nombres, acu_apellidos, acu_estado):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos los datos del acudiente
        query = (
            "UPDATE T_ACUDIENTE "
            "SET ACU_UUID = %s, ACU_NOMBRES = %s, ACU_APELLIDOS = %s, ACU_ESTADO = %s "
            "WHERE ACU_ID = %s"
        )
        cursor.execute(query, (acu_uuid, acu_nombres, acu_apellidos, acu_estado, acu_id))
        
        # Confirmamos la actualización
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos el registro del acudiente
        query = "DELETE FROM T_ACUDIENTE WHERE ACU_ID = %s"
        cursor.execute(query, (acu_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()