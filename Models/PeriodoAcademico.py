class PeriodoAcademico:

    def __init__(
        self,
        PER_ACA_ID,
        PER_ACA_UUID,
        PER_ACA_NUMERO,
        PER_ACA_FECHA_INICIO,
        PER_ACA_FECHA_FIN,
        PER_ACA_VIG_ID
    ):
        self.PER_ACA_ID          = PER_ACA_ID
        self.PER_ACA_UUID        = PER_ACA_UUID
        self.PER_ACA_NUMERO      = PER_ACA_NUMERO
        self.PER_ACA_FECHA_INICIO = PER_ACA_FECHA_INICIO
        self.PER_ACA_FECHA_FIN   = PER_ACA_FECHA_FIN
        self.PER_ACA_VIG_ID      = PER_ACA_VIG_ID


    def to_dict(self):
        return {
            'PER_ACA_ID'          : self.PER_ACA_ID,
            'PER_ACA_UUID'        : self.PER_ACA_UUID,
            'PER_ACA_NUMERO'      : self.PER_ACA_NUMERO,
            'PER_ACA_FECHA_INICIO': self.PER_ACA_FECHA_INICIO,
            'PER_ACA_FECHA_FIN'   : self.PER_ACA_FECHA_FIN,
            'PER_ACA_VIG_ID'      : self.PER_ACA_VIG_ID
        }