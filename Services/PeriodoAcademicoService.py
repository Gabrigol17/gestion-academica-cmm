from flask import current_app

class PeriodoAcademicoService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO PeriodoAcademico (id_vigencia, nombre_periodo, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)"
        params = (data.get('id_vigencia'), data.get('nombre_periodo'), data.get('fecha_inicio'), data.get('fecha_fin'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_periodo, data):
        db = current_app.db
        query = "UPDATE PeriodoAcademico SET id_vigencia = %s, nombre_periodo = %s, fecha_inicio = %s, fecha_fin = %s WHERE id_periodo = %s"
        params = (data.get('id_vigencia'), data.get('nombre_periodo'), data.get('fecha_inicio'), data.get('fecha_fin'), id_periodo)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_periodo):
        db = current_app.db
        query = "DELETE FROM PeriodoAcademico WHERE id_periodo = %s"
        return db.execute_query(query, (id_periodo,), commit=True)

    def read(self, id_periodo=None):
        db = current_app.db
        if id_periodo:
            query = "SELECT * FROM PeriodoAcademico WHERE id_periodo = %s"
            return db.fetch_one(query, (id_periodo,))
        else:
            query = "SELECT * FROM PeriodoAcademico"
            return db.fetch_all(query)