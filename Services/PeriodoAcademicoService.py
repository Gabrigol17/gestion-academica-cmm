from flask import current_app

class PeriodoAcademicoService:

    def add(self, nombre_periodo, id_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO PeriodoAcademico (nombre_periodo, id_vigencia) VALUES (%s, %s)"
        c.execute(query, (nombre_periodo, id_vigencia))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM PeriodoAcademico"
        c.execute(query)
        data = c.fetchall()
        periodos = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return periodos

    def update(self, id_periodo, nombre_periodo, id_vigencia):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE PeriodoAcademico SET nombre_periodo = %s, id_vigencia = %s WHERE id_periodo = %s"
        c.execute(query, (nombre_periodo, id_vigencia, id_periodo))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_periodo):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM PeriodoAcademico WHERE id_periodo = %s"
        c.execute(query, (id_periodo,))
        current_app.mysql.connection.commit()
        c.close()
