from flask import current_app

class AcudienteCorreoService:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO AcudienteCorreo (id_acudiente, correo) VALUES (%s, %s)"
        params = (data.get('id_acudiente'), data.get('correo'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_acudiente_correo, data):
        db = current_app.db
        query = "UPDATE AcudienteCorreo SET id_acudiente = %s, correo = %s WHERE id_acudiente_correo = %s"
        params = (data.get('id_acudiente'), data.get('correo'), id_acudiente_correo)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_acudiente_correo):
        db = current_app.db
        query = "DELETE FROM AcudienteCorreo WHERE id_acudiente_correo = %s"
        return db.execute_query(query, (id_acudiente_correo,), commit=True)

    def read(self, id_acudiente_correo=None):
        db = current_app.db
        if id_acudiente_correo:
            query = "SELECT * FROM AcudienteCorreo WHERE id_acudiente_correo = %s"
            return db.fetch_one(query, (id_acudiente_correo,))
        else:
            query = "SELECT * FROM AcudienteCorreo"
            return db.fetch_all(query)