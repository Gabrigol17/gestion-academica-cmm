from flask import current_app

class DiaSemanaService:

    def add(self, nombre_dia):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO DiaSemana (nombre_dia) VALUES (%s)"
        c.execute(query, (nombre_dia,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM DiaSemana"
        c.execute(query)
        data = c.fetchall()
        dias = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return dias

    def update(self, id_dia_semana, nombre_dia):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE DiaSemana SET nombre_dia = %s WHERE id_dia_semana = %s"
        c.execute(query, (nombre_dia, id_dia_semana))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_dia_semana):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM DiaSemana WHERE id_dia_semana = %s"
        c.execute(query, (id_dia_semana,))
        current_app.mysql.connection.commit()
        c.close()
