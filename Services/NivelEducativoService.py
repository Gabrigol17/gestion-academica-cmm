from flask import current_app

from Models.NivelEducativo import NivelEducativo

class NivelEducativoService:

    def crear(self, niv_educ_nombre):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_NIVEL_EDUCATIVO "
            "(NIV_EDUC_NOMBRE) "
            "VALUES (%s)"
        )

        cursor.execute(query, (niv_educ_nombre,))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_NIVEL_EDUCATIVO"
        cursor.execute(query)

        data = cursor.fetchall()

        niveles = [NivelEducativo(col[0], col[1]).to_dict() for col in data]

        cursor.close()
        return niveles

    def obtener_por_id(self, niv_educ_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_NIVEL_EDUCATIVO WHERE NIV_EDUC_ID = %s"
        cursor.execute(query, (niv_educ_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            nivel = NivelEducativo(data[0], data[1]).to_dict()
            return nivel
        else:
            return None

    def actualizar(self, niv_educ_nombre, niv_educ_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_NIVEL_EDUCATIVO "
            "SET NIV_EDUC_NOMBRE = %s "
            "WHERE NIV_EDUC_ID = %s"
        )
        cursor.execute(query, (niv_educ_nombre, niv_educ_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, niv_educ_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_NIVEL_EDUCATIVO WHERE NIV_EDUC_ID = %s"
        cursor.execute(query, (niv_educ_id,))

        current_app.mysql.connection.commit()
        cursor.close()
