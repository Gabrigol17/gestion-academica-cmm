from flask import current_app

class TipoComponenteService:

    def add(self, nombre_tipo):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO TipoComponente (nombre_tipo) VALUES (%s)"
        c.execute(query, (nombre_tipo,))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM TipoComponente"
        c.execute(query)
        data = c.fetchall()
        tipos = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return tipos

    def update(self, id_tipo_componente, nombre_tipo):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE TipoComponente SET nombre_tipo = %s WHERE id_tipo_componente = %s"
        c.execute(query, (nombre_tipo, id_tipo_componente))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_tipo_componente):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM TipoComponente WHERE id_tipo_componente = %s"
        c.execute(query, (id_tipo_componente,))
        current_app.mysql.connection.commit()
        c.close()