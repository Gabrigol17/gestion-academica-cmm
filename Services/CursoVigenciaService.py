from flask import current_app

class CursoVigenciaService:

    def crear(self, cur_vig_uuid, cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id):
        # 1. Abrimos cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos la relación entre grado, letra y vigencia del curso
        query = (
            "INSERT INTO T_CURSO_VIGENCIA "
            "(CUR_VIG_UUID, CUR_VIG_LETRA, CUR_VIG_VIG_ID, CUR_VIG_GRAD_ID) "
            "VALUES (%s, %s, %s, %s)"
        )
        
        # 3. Ejecutamos con tupla segura
        cursor.execute(query, (cur_vig_uuid, cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id))
        
        # 4. Guardamos los cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_CURSO_VIGENCIA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        cursos = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return cursos

    def obtener_por_id(self, cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos por CUR_VIG_ID
        query = "SELECT * FROM T_CURSO_VIGENCIA WHERE CUR_VIG_ID = %s"
        cursor.execute(query, (cur_vig_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, cur_vig_id, cur_vig_uuid, cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos los parámetros del curso en la vigencia
        query = (
            "UPDATE T_CURSO_VIGENCIA "
            "SET CUR_VIG_UUID = %s, CUR_VIG_LETRA = %s, CUR_VIG_VIG_ID = %s, CUR_VIG_GRAD_ID = %s "
            "WHERE CUR_VIG_ID = %s"
        )
        cursor.execute(query, (cur_vig_uuid, cur_vig_letra, cur_vig_vig_id, cur_vig_grad_id, cur_vig_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, cur_vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el registro del curso
        query = "DELETE FROM T_CURSO_VIGENCIA WHERE CUR_VIG_ID = %s"
        cursor.execute(query, (cur_vig_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()
