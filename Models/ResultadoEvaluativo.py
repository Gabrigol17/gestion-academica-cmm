class ResultadoEvaluativo:

    def __init__(
        self,
        RES_EVA_ID,
        RES_EVA_UUID,
        RES_EVA_NOTA,
        RES_EVA_AJUSTE,
        RES_EVA_OBSERVACION,
        RES_EVA_MAT_ID,
        RES_EVA_ACT_EVA_ID
    ):
        self.RES_EVA_ID          = RES_EVA_ID
        self.RES_EVA_UUID        = RES_EVA_UUID
        self.RES_EVA_NOTA        = RES_EVA_NOTA
        self.RES_EVA_AJUSTE      = RES_EVA_AJUSTE
        self.RES_EVA_OBSERVACION = RES_EVA_OBSERVACION
        self.RES_EVA_MAT_ID      = RES_EVA_MAT_ID
        self.RES_EVA_ACT_EVA_ID  = RES_EVA_ACT_EVA_ID


    def to_dict(self):
        return {
            'RES_EVA_ID'         : self.RES_EVA_ID,
            'RES_EVA_UUID'       : self.RES_EVA_UUID,
            'RES_EVA_NOTA'       : self.RES_EVA_NOTA,
            'RES_EVA_AJUSTE'     : self.RES_EVA_AJUSTE,
            'RES_EVA_OBSERVACION': self.RES_EVA_OBSERVACION,
            'RES_EVA_MAT_ID'     : self.RES_EVA_MAT_ID,
            'RES_EVA_ACT_EVA_ID' : self.RES_EVA_ACT_EVA_ID
        }