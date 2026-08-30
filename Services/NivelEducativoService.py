from flask import current_app

class NivelEducativoService:

    def add(self, nombre_nivel):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO NivelEducativo (nombre_nivel) VALUES (%s)"
        c.execute(query, (nombre_nivel,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM NivelEducativo"
        c.execute(query)
        data = c.fetchall()
        niveles = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return niveles

    def update(self, id_nivel_educativo, nombre_nivel):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE NivelEducativo SET nombre_nivel = %s WHERE id_nivel_educativo = %s"
        c.execute(query, (nombre_nivel, id_nivel_educativo))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_nivel_educativo):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM NivelEducativo WHERE id_nivel_educativo = %s"
        c.execute(query, (id_nivel_educativo,))
        current_app.mysql.connection.commit()
        c.close()