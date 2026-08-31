from flask import current_app

class TipoComponenteService:

    def crear(self, tipo_comp_nombre, tipo_comp_descripcion):
        # 1. Conexión mediante cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Registramos el tipo de componente (Ej: Examen, Tarea, Proyecto)
        query = (
            "INSERT INTO T_TIPO_COMPONENTE "
            "(TIPO_COMP_NOMBRE, TIPO_COMP_DESCRIPCION) "
            "VALUES (%s, %s)"
        )
        
        # 3. Pasamos los parámetros
        cursor.execute(query, (tipo_comp_nombre, tipo_comp_descripcion))
        
        # 4. Guardamos cambios
        current_app.mysql.connection.commit()
        
        # 5. Cerramos el cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_TIPO_COMPONENTE"
        cursor.execute(query)
        
        data = cursor.fetchall()
        tipos = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return tipos

    def obtener_por_id(self, tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos por TIPO_COMP_ID
        query = "SELECT * FROM T_TIPO_COMPONENTE WHERE TIPO_COMP_ID = %s"
        cursor.execute(query, (tipo_comp_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, tipo_comp_id, tipo_comp_nombre, tipo_comp_descripcion):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos el nombre o descripción del tipo de componente
        query = (
            "UPDATE T_TIPO_COMPONENTE "
            "SET TIPO_COMP_NOMBRE = %s, TIPO_COMP_DESCRIPCION = %s "
            "WHERE TIPO_COMP_ID = %s"
        )
        cursor.execute(query, (tipo_comp_nombre, tipo_comp_descripcion, tipo_comp_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos el tipo de componente
        query = "DELETE FROM T_TIPO_COMPONENTE WHERE TIPO_COMP_ID = %s"
        cursor.execute(query, (tipo_comp_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()