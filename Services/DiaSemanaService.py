from flask import current_app

class DiaSemanaService:

    def crear(self, dia_sem_nombre):
        # 1. Abrimos el cursor para conectarnos
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos el nombre del día de la semana
        query = "INSERT INTO T_DIA_SEMANA (DIA_SEM_NOMBRE) VALUES (%s)"
        
        # 3. Ejecutamos la consulta con el parámetro
        cursor.execute(query, (dia_sem_nombre,))
        
        # 4. Guardamos los cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DIA_SEMANA"
        cursor.execute(query)
        
        data = cursor.fetchall()
        dias = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return dias

    def obtener_por_id(self, dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos el día específico por DIA_SEM_ID
        query = "SELECT * FROM T_DIA_SEMANA WHERE DIA_SEM_ID = %s"
        cursor.execute(query, (dia_sem_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, dia_sem_id, dia_sem_nombre):
        cursor = current_app.mysql.connection.cursor()
        # Actualizamos el nombre del día
        query = "UPDATE T_DIA_SEMANA SET DIA_SEM_NOMBRE = %s WHERE DIA_SEM_ID = %s"
        cursor.execute(query, (dia_sem_nombre, dia_sem_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, dia_sem_id):
        cursor = current_app.mysql.connection.cursor()
        # Eliminamos el registro del día
        query = "DELETE FROM T_DIA_SEMANA WHERE DIA_SEM_ID = %s"
        cursor.execute(query, (dia_sem_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()
