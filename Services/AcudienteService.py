from flask import current_app

class AcudienteService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Acudiente (id_persona, ocupacion) VALUES (%s, %s)"
        params = (data.get('id_persona'), data.get('ocupacion'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_acudiente, data):
        db = current_app.db
        query = "UPDATE Acudiente SET id_persona = %s, ocupacion = %s WHERE id_acudiente = %s"
        params = (data.get('id_persona'), data.get('ocupacion'), id_acudiente)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_acudiente):
        db = current_app.db
        query = "DELETE FROM Acudiente WHERE id_acudiente = %s"
        return db.execute_query(query, (id_acudiente,), commit=True)

    def read(self, id_acudiente=None):
        db = current_app.db
        if id_acudiente:
            query = "SELECT * FROM Acudiente WHERE id_acudiente = %s"
            return db.fetch_one(query, (id_acudiente,))
        else:
            query = "SELECT * FROM Acudiente"
            return db.fetch_all(query)