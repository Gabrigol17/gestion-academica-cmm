class ActividadEvaluativa:

    def __init__(
        self,
        ACT_EVA_ID,
        ACT_EVA_UUID,
        ACT_EVA_NOMBRE,
        ACT_EVA_DESCRIPCION,
        ACT_EVA_ASIG_ACA_ID,
        ACT_EVA_COM_EVA_ID
    ):
        self.ACT_EVA_ID          = ACT_EVA_ID
        self.ACT_EVA_UUID        = ACT_EVA_UUID
        self.ACT_EVA_NOMBRE      = ACT_EVA_NOMBRE
        self.ACT_EVA_DESCRIPCION = ACT_EVA_DESCRIPCION
        self.ACT_EVA_ASIG_ACA_ID = ACT_EVA_ASIG_ACA_ID
        self.ACT_EVA_COM_EVA_ID  = ACT_EVA_COM_EVA_ID


    def to_dict(self):
        return {
            'ACT_EVA_ID'         : self.ACT_EVA_ID,
            'ACT_EVA_UUID'       : self.ACT_EVA_UUID,
            'ACT_EVA_NOMBRE'     : self.ACT_EVA_NOMBRE,
            'ACT_EVA_DESCRIPCION': self.ACT_EVA_DESCRIPCION,
            'ACT_EVA_ASIG_ACA_ID': self.ACT_EVA_ASIG_ACA_ID,
            'ACT_EVA_COM_EVA_ID' : self.ACT_EVA_COM_EVA_ID
        }