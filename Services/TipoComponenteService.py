from flask import current_app

class TipoComponenteService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO TipoComponente (nombre_tipo) VALUES (%s)"
        params = (data.get('nombre_tipo'),)
        return db.execute_query(query, params, commit=True)

    def update(self, id_tipo_componente, data):
        db = current_app.db
        query = "UPDATE TipoComponente SET nombre_tipo = %s WHERE id_tipo_componente = %s"
        params = (data.get('nombre_tipo'), id_tipo_componente)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_tipo_componente):
        db = current_app.db
        query = "DELETE FROM TipoComponente WHERE id_tipo_componente = %s"
        return db.execute_query(query, (id_tipo_componente,), commit=True)

    def read(self, id_tipo_componente=None):
        db = current_app.db
        if id_tipo_componente:
            query = "SELECT * FROM TipoComponente WHERE id_tipo_componente = %s"
            return db.fetch_one(query, (id_tipo_componente,))
        else:
            query = "SELECT * FROM TipoComponente"
            return db.fetch_all(query)