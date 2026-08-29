class AcudienteCorreo:

    def __init__(self, ACU_CORR_ID, ACU_CORR_UUID, ACU_CORR_ACU_ID, ACU_CORR_CORREO):
        self.ACU_CORR_ID     = ACU_CORR_ID
        self.ACU_CORR_UUID   = ACU_CORR_UUID
        self.ACU_CORR_ACU_ID = ACU_CORR_ACU_ID
        self.ACU_CORR_CORREO = ACU_CORR_CORREO


    def to_dict(self):
        return {
            'ACU_CORR_ID'    : self.ACU_CORR_ID,
            'ACU_CORR_UUID'  : self.ACU_CORR_UUID,
            'ACU_CORR_ACU_ID': self.ACU_CORR_ACU_ID,
            'ACU_CORR_CORREO': self.ACU_CORR_CORREO
        }
