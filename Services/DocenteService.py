from flask import current_app

from Models.Docente import Docente

class DocenteService:

    def crear(self, doc_estado, doc_per_id):
        cursor = current_app.mysql.connection.cursor()

        query = (
            "INSERT INTO T_DOCENTE "
            "(DOC_UUID, DOC_ESTADO, DOC_PER_ID) "
            "VALUES (UUID(), %s, %s)"
        )

        cursor.execute(query, (doc_estado, doc_per_id))
        current_app.mysql.connection.commit()
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DOCENTE"
        cursor.execute(query)

        data = cursor.fetchall()

        docentes = [Docente(col[0], col[1], col[2], col[3]).to_dict() for col in data]

        cursor.close()
        return docentes

    def obtener_por_id(self, doc_id):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_DOCENTE WHERE DOC_ID = %s"
        cursor.execute(query, (doc_id,))

        data = cursor.fetchone()
        cursor.close()
        if data:
            docente = Docente(data[0], data[1], data[2], data[3]).to_dict()
            return docente
        else:
            return None

    def actualizar(self, doc_estado, doc_per_id, doc_id):
        cursor = current_app.mysql.connection.cursor()
        query = (
            "UPDATE T_DOCENTE "
            "SET DOC_ESTADO = %s, DOC_PER_ID = %s "
            "WHERE DOC_ID = %s"
        )
        cursor.execute(query, (doc_estado, doc_per_id, doc_id))

        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, doc_id):
        cursor = current_app.mysql.connection.cursor()
        query = "DELETE FROM T_DOCENTE WHERE DOC_ID = %s"
        cursor.execute(query, (doc_id,))

        current_app.mysql.connection.commit()
        cursor.close()
