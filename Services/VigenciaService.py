from flask import current_app

class VigenciaService:

    def crear(self, vig_uuid, vig_anio, vig_estado):
        # 1. Abrimos conexión mediante el cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Registramos la año/vigencia lectiva (Ej: 2026, Activo)
        query = (
            "INSERT INTO T_VIGENCIA "
            "(VIG_UUID, VIG_ANIO, VIG_ESTADO) "
            "VALUES (%s, %s, %s)"
        )
        
        # 3. Pasamos los datos en tupla
        cursor.execute(query, (vig_uuid, vig_anio, vig_estado))
        
        # 4. Guardamos los cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_VIGENCIA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        vigencias = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return vigencias

    def obtener_por_id(self, vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos la vigencia por VIG_ID
        query = "SELECT * FROM T_VIGENCIA WHERE VIG_ID = %s"
        cursor.execute(query, (vig_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, vig_id, vig_uuid, vig_anio, vig_estado):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos el año o estado de la vigencia
        query = (
            "UPDATE T_VIGENCIA "
            "SET VIG_UUID = %s, VIG_ANIO = %s, VIG_ESTADO = %s "
            "WHERE VIG_ID = %s"
        )
        cursor.execute(query, (vig_uuid, vig_anio, vig_estado, vig_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el registro de la vigencia
        query = "DELETE FROM T_VIGENCIA WHERE VIG_ID = %s"
        cursor.execute(query, (vig_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()