from flask import current_app

class ActividadEvaluativaModel:

    def __init__(self, id_actividad=None, id_componente=None, id_periodo=None, titulo=None, descripcion=None, fecha_entrega=None):
        self.id_actividad = id_actividad
        self.id_componente = id_componente
        self.id_periodo = id_periodo
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega

    def save(self):
        db = current_app.db
        query = """
            INSERT INTO ActividadEvaluativa (id_componente, id_periodo, titulo, descripcion, fecha_entrega)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (self.id_componente, self.id_periodo, self.titulo, self.descripcion, self.fecha_entrega)
        return db.execute_query(query, params, commit=True)

    @staticmethod
    def get_by_id(id_actividad):
        db = current_app.db
        query = "SELECT * FROM ActividadEvaluativa WHERE id_actividad = %s"
        return db.fetch_one(query, (id_actividad,))

    @staticmethod
    def get_all():
        db = current_app.db
        query = "SELECT * FROM ActividadEvaluativa"
        return db.fetch_all(query)

    def update(self):
        db = current_app.db
        query = """
            UPDATE ActividadEvaluativa 
            SET id_componente = %s, id_periodo = %s, titulo = %s, descripcion = %s, fecha_entrega = %s
            WHERE id_actividad = %s
        """
        params = (self.id_componente, self.id_periodo, self.titulo, self.descripcion, self.fecha_entrega, self.id_actividad)
        return db.execute_query(query, params, commit=True)

    @staticmethod
    def delete_by_id(id_actividad):
        db = current_app.db
        query = "DELETE FROM ActividadEvaluativa WHERE id_actividad = %s"
        return db.execute_query(query, (id_actividad,), commit=True)