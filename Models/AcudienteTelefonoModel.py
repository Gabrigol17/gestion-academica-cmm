from flask import current_app

class AcudienteTelefonoModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO AcudienteTelefono (id_acudiente, telefono) VALUES (%s, %s)"
        params = (data.get('id_acudiente'), data.get('telefono'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_acudiente_telefono, data):
        db = current_app.db
        query = "UPDATE AcudienteTelefono SET id_acudiente = %s, telefono = %s WHERE id_acudiente_telefono = %s"
        params = (data.get('id_acudiente'), data.get('telefono'), id_acudiente_telefono)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_acudiente_telefono):
        db = current_app.db
        query = "DELETE FROM AcudienteTelefono WHERE id_acudiente_telefono = %s"
        return db.execute_query(query, (id_acudiente_telefono,), commit=True)

    def read(self, id_acudiente_telefono=None):
        db = current_app.db
        if id_acudiente_telefono:
            query = "SELECT * FROM AcudienteTelefono WHERE id_acudiente_telefono = %s"
            return db.fetch_one(query, (id_acudiente_telefono,))
        else:
            query = "SELECT * FROM AcudienteTelefono"
            return db.fetch_all(query)