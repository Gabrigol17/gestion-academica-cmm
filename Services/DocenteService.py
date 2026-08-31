from flask import current_app

class DocenteService:

    def crear(self, doc_uuid, doc_estado, doc_per_id):
        # 1. Abrimos conexión MySQL
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos la información del docente vinculada a T_PERSONA
        query = (
            "INSERT INTO T_DOCENTE "
            "(DOC_UUID, DOC_ESTADO, DOC_PER_ID) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Ejecutamos la inserción en tupla
        cursor.execute(query, (doc_uuid, doc_estado, doc_per_id))
        
        # 4. Guardamos los cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos conexión
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DOCENTE"
        cursor.execute(query)
        
        data = cursor.fetchall()
        docentes = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return docentes

    def obtener_por_id(self, doc_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos al docente por DOC_ID
        query = "SELECT * FROM T_DOCENTE WHERE DOC_ID = %s"
        cursor.execute(query, (doc_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, doc_id, doc_uuid, doc_estado, doc_per_id):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos el estado o referencia del docente
        query = (
            "UPDATE T_DOCENTE "
            "SET DOC_UUID = %s, DOC_ESTADO = %s, DOC_PER_ID = %s "
            "WHERE DOC_ID = %s"
        )
        cursor.execute(query, (doc_uuid, doc_estado, doc_per_id, doc_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, doc_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos al docente
        query = "DELETE FROM T_DOCENTE WHERE DOC_ID = %s"
        cursor.execute(query, (doc_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()