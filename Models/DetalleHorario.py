class DetalleHorario:

    def __init__(
        self,
        DET_HOR_ID,
        DET_HOR_UUID,
        DET_HOR_ASIG_ACA_ID,
        DET_HOR_DIA_SEM_ID,
        DET_HOR_HORA_INICIO,
        DET_HOR_HORA_FIN
    ):
        self.DET_HOR_ID          = DET_HOR_ID
        self.DET_HOR_UUID        = DET_HOR_UUID
        self.DET_HOR_ASIG_ACA_ID = DET_HOR_ASIG_ACA_ID
        self.DET_HOR_DIA_SEM_ID  = DET_HOR_DIA_SEM_ID
        self.DET_HOR_HORA_INICIO = DET_HOR_HORA_INICIO
        self.DET_HOR_HORA_FIN    = DET_HOR_HORA_FIN


    def to_dict(self):
        return {
            'DET_HOR_ID'         : self.DET_HOR_ID,
            'DET_HOR_UUID'       : self.DET_HOR_UUID,
            'DET_HOR_ASIG_ACA_ID': self.DET_HOR_ASIG_ACA_ID,
            'DET_HOR_DIA_SEM_ID' : self.DET_HOR_DIA_SEM_ID,
            'DET_HOR_HORA_INICIO': self.DET_HOR_HORA_INICIO,
            'DET_HOR_HORA_FIN'   : self.DET_HOR_HORA_FIN
        }
