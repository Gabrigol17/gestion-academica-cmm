from flask import current_app

class DocenteModel:

    def add(self, data):
        db = current_app.db
        query = "INSERT INTO Docente (id_persona, titulo_academico) VALUES (%s, %s)"
        params = (data.get('id_persona'), data.get('titulo_academico'))
        return db.execute_query(query, params, commit=True)

    def update(self, id_docente, data):
        db = current_app.db
        query = "UPDATE Docente SET id_persona = %s, titulo_academico = %s WHERE id_docente = %s"
        params = (data.get('id_persona'), data.get('titulo_academico'), id_docente)
        return db.execute_query(query, params, commit=True)

    def delete(self, id_docente):
        db = current_app.db
        query = "DELETE FROM Docente WHERE id_docente = %s"
        return db.execute_query(query, (id_docente,), commit=True)

    def read(self, id_docente=None):
        db = current_app.db
        if id_docente:
            query = "SELECT * FROM Docente WHERE id_docente = %s"
            return db.fetch_one(query, (id_docente,))
        else:
            query = "SELECT * FROM Docente"
            return db.fetch_all(query)