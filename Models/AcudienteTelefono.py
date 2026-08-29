class AcudienteTelefono:

    def __init__(self, ACU_TEL_ID, ACU_TEL_UUID, ACU_TEL_ACU_ID, ACU_TEL_NUMERO):
        self.ACU_TEL_ID     = ACU_TEL_ID
        self.ACU_TEL_UUID   = ACU_TEL_UUID
        self.ACU_TEL_ACU_ID = ACU_TEL_ACU_ID
        self.ACU_TEL_NUMERO = ACU_TEL_NUMERO


    def to_dict(self):
        return {
            'ACU_TEL_ID'    : self.ACU_TEL_ID,
            'ACU_TEL_UUID'  : self.ACU_TEL_UUID,
            'ACU_TEL_ACU_ID': self.ACU_TEL_ACU_ID,
            'ACU_TEL_NUMERO': self.ACU_TEL_NUMERO
        }
