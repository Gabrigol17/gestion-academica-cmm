from flask import current_app

class PeriodoAcademicoService:

    def crear(self, per_aca_uuid, per_aca_nombre, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id):
        # 1. Abrimos conexión mediante cursor
        cursor = current_app.mysql.connection.cursor()
        
        # 2. Insertamos el periodo académico (Ej: Periodo 1, Trimestre 2)
        query = (
            "INSERT INTO T_PERIODO_ACADEMICO "
            "(PER_ACA_UUID, PER_ACA_NOMBRE, PER_ACA_FECHA_INICIO, PER_ACA_FECHA_FIN, PER_ACA_VIG_ID) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        
        # 3. Pasamos los datos en tupla
        cursor.execute(query, (per_aca_uuid, per_aca_nombre, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id))
        
        # 4. Confirmamos los datos
        current_app.mysql.connection.commit()
        
        # 5. Cerramos cursor
        cursor.close()

    def obtener_todos(self):
        cursor = current_app.mysql.connection.cursor()
        query = "SELECT * FROM T_PERIODO_ACADEMICO"
        cursor.execute(query)
        
        data = cursor.fetchall()
        periodos = [dict(zip([col[0] for col in cursor.description], row)) for row in data]
        cursor.close()
        return periodos

    def obtener_por_id(self, per_aca_id):
        cursor = current_app.mysql.connection.cursor()
        # Buscamos el periodo por PER_ACA_ID
        query = "SELECT * FROM T_PERIODO_ACADEMICO WHERE PER_ACA_ID = %s"
        cursor.execute(query, (per_aca_id,))
        
        data = cursor.fetchone()
        cursor.close()
        return dict(zip([col[0] for col in cursor.description], data)) if data else None

    def actualizar(self, per_aca_id, per_aca_uuid, per_aca_nombre, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id):
        cursor = current_app.mysql.connection.cursor()
        # Modificamos las fechas o nombre del periodo
        query = (
            "UPDATE T_PERIODO_ACADEMICO "
            "SET PER_ACA_UUID = %s, PER_ACA_NOMBRE = %s, PER_ACA_FECHA_INICIO = %s, "
            "PER_ACA_FECHA_FIN = %s, PER_ACA_VIG_ID = %s "
            "WHERE PER_ACA_ID = %s"
        )
        cursor.execute(query, (per_aca_uuid, per_aca_nombre, per_aca_fecha_inicio, per_aca_fecha_fin, per_aca_vig_id, per_aca_id))
        
        current_app.mysql.connection.commit()
        cursor.close()

    def eliminar(self, per_aca_id):
        cursor = current_app.mysql.connection.cursor()
        # Borramos el periodo académico
        query = "DELETE FROM T_PERIODO_ACADEMICO WHERE PER_ACA_ID = %s"
        cursor.execute(query, (per_aca_id,))
        
        current_app.mysql.connection.commit()
        cursor.close()