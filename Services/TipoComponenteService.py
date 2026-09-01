from flask import current_app

from Models.TipoComponente import TipoComponente

class TipoComponenteService:

    def crear(self, tipo_comp_nombre):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_TIPO_COMPONENTE "
            "(TIPO_COMP_NOMBRE) "
            "VALUES (%s)"
        )

        cursor.execute(query, (tipo_comp_nombre,))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_TIPO_COMPONENTE"
        cursor.execute(query)

        data = cursor.fetchall()

        tipos = [TipoComponente(col[0], col[1]).to_dict() for col in data]

        cursor.close()
        return tipos

    def obtener_por_id(self, tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_TIPO_COMPONENTE WHERE TIPO_COMP_ID = %s"
        cursor.execute(query, (tipo_comp_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            tipo = TipoComponente(data[0], data[1]).to_dict()
            return tipo
        else:
            return None

    def actualizar(self, tipo_comp_nombre, tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_TIPO_COMPONENTE "
            "SET TIPO_COMP_NOMBRE = %s "
            "WHERE TIPO_COMP_ID = %s"
        )
        cursor.execute(query, (tipo_comp_nombre, tipo_comp_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, tipo_comp_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_TIPO_COMPONENTE WHERE TIPO_COMP_ID = %s"
        cursor.execute(query, (tipo_comp_id,))

        current_app.mysql.connection.commit()
        cursor.close()
