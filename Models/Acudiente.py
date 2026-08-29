class Acudiente:

    def __init__(self, ACU_ID, ACU_UUID, ACU_NOMBRES, ACU_APELLIDOS, ACU_ESTADO):
        self.ACU_ID        = ACU_ID
        self.ACU_UUID      = ACU_UUID
        self.ACU_NOMBRES   = ACU_NOMBRES
        self.ACU_APELLIDOS = ACU_APELLIDOS
        self.ACU_ESTADO    = ACU_ESTADO


    def to_dict(self):
        return {
            'ACU_ID'       : self.ACU_ID,
            'ACU_UUID'     : self.ACU_UUID,
            'ACU_NOMBRES'  : self.ACU_NOMBRES,
            'ACU_APELLIDOS': self.ACU_APELLIDOS,
            'ACU_ESTADO'   : self.ACU_ESTADO
        }
