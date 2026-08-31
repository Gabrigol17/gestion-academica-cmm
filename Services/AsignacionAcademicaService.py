from flask import current_app

class AsignacionAcademicaService:

    def crear(self, asig_aca_uuid, asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id):
        # 1. Abrimos el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Sentencia para asociar docente, materia y curso
        query = (
            "INSERT INTO T_ASIGNACION_ACADEMICA "
            "(ASIG_ACA_UUID, ASIG_ACA_ESTADO, ASIG_ACA_DOC_ID, ASIG_ACA_MAT_ID, ASIG_ACA_CUR_VIG_ID) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos enviando los parámetros
        cursor.execute(query, (asig_aca_uuid, asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id))
        
        # 4. Guardamos la asignación
        current_app.mysql.connection.commit()
        
        # 5. Cerramos cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_ASIGNACION_ACADEMICA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        asignaciones = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return asignaciones

    def obtener_por_id(self, asig_aca_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos por ASIG_ACA_ID
        query = "SELECT * FROM T_ASIGNACION_ACADEMICA WHERE ASIG_ACA_ID = %s"
        cursor.execute(query, (asig_aca_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, asig_aca_id, asig_aca_uuid, asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos la asignación existente
        query = (
            "UPDATE T_ASIGNACION_ACADEMICA "
            "SET ASIG_ACA_UUID = %s, ASIG_ACA_ESTADO = %s, ASIG_ACA_DOC_ID = %s, "
            "ASIG_ACA_MAT_ID = %s, ASIG_ACA_CUR_VIG_ID = %s "
            "WHERE ASIG_ACA_ID = %s"
        )
        cursor.execute(query, (asig_aca_uuid, asig_aca_estado, asig_aca_doc_id, asig_aca_mat_id, asig_aca_cur_vig_id, asig_aca_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, asig_aca_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos la asignación académica
        query = "DELETE FROM T_ASIGNACION_ACADEMICA WHERE ASIG_ACA_ID = %s"
        cursor.execute(query, (asig_aca_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()

