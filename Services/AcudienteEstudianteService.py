from flask import current_app

class AcudienteEstudianteService:

    def crear(self, acu_est_uuid, acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal):
        # 1. Abrimos conexión
        cursor = current_app.mysql.connection.cursor()
        # 2. Query estructurada en múltiples líneas sin romper la indentación
        query = (
            "INSERT INTO T_ACUDIENTE_ESTUDIANTE "
            "(ACU_EST_UUID, ACU_EST_PARENTESCO, ACU_EST_ACU_ID, ACU_EST_EST_ID, ACU_EST_ESPRINCIPAL) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        # 3. Ejecutamos pasando la tupla de datos
        cursor.execute(query, (acu_est_uuid, acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal))
        # 4. Guardamos cambios
        current_app.mysql.connection.commit()
        # 5. Cerramos cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_ESTUDIANTE"
        cursor.execute(query)
        # fetchall() obtiene todos los registros y los mapeamos a diccionario
        data = cursor.fetchall()
        resultados = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return resultados

    def obtener_por_id(self, acu_est_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ACUDIENTE_ESTUDIANTE WHERE ACU_EST_ID = %s"
        cursor.execute(query, (acu_est_id,))
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, acu_est_id, acu_est_uuid, acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_ACUDIENTE_ESTUDIANTE "
            "SET ACU_EST_UUID = %s, ACU_EST_PARENTESCO = %s, ACU_EST_ACU_ID = %s, "
            "ACU_EST_EST_ID = %s, ACU_EST_ESPRINCIPAL = %s "
            "WHERE ACU_EST_ID = %s"
        )
        cursor.execute(query, (acu_est_uuid, acu_est_parentesco, acu_est_acu_id, acu_est_est_id, acu_est_esprincipal, acu_est_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, acu_est_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_ACUDIENTE_ESTUDIANTE WHERE ACU_EST_ID = %s"
        cursor.execute(query, (acu_est_id,))
        current_app.mysql.connection.commit()
        cursor.close()