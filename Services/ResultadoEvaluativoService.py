from flask import current_app

class ResultadoEvaluativoService:

    def add(self, id_actividad, id_matricula, nota):
        c = current_app.mysql.connection.cursor()
        query = "INSERT INTO ResultadoEvaluativo (id_actividad, id_matricula, nota) VALUES (%s, %s, %s)"
        c.execute(query, (id_actividad, id_matricula, nota))
        current_app.mysql.connection.commit()
        c.close()

    def read(self):
        c = current_app.mysql.connection.cursor()
        query = "SELECT * FROM ResultadoEvaluativo"
        c.execute(query)
        data = c.fetchall()
        resultados = [dict(zip([column[0] for column in c.description], row)) for row in data]
        c.close()
        return resultados

    def update(self, id_resultado, id_actividad, id_matricula, nota):
        c = current_app.mysql.connection.cursor()
        query = "UPDATE ResultadoEvaluativo SET id_actividad = %s, id_matricula = %s, nota = %s WHERE id_resultado = %s"
        c.execute(query, (id_actividad, id_matricula, nota, id_resultado))
        current_app.mysql.connection.commit()
        c.close()

    def delete(self, id_resultado):
        c = current_app.mysql.connection.cursor()
        query = "DELETE FROM ResultadoEvaluativo WHERE id_resultado = %s"
        c.execute(query, (id_resultado,))
        current_app.mysql.connection.commit()
        c.close()