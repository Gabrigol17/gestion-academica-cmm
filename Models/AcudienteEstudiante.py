class AcudienteEstudiante:

    def __init__(
        self,
        ACU_EST_ID,
        ACU_EST_UUID,
        ACU_EST_PARENTESCO,
        ACU_EST_ACU_ID,
        ACU_EST_EST_ID,
        ACU_EST_ESPRINCIPAL
    ):
        self.ACU_EST_ID          = ACU_EST_ID
        self.ACU_EST_UUID        = ACU_EST_UUID
        self.ACU_EST_PARENTESCO  = ACU_EST_PARENTESCO
        self.ACU_EST_ACU_ID      = ACU_EST_ACU_ID
        self.ACU_EST_EST_ID      = ACU_EST_EST_ID
        self.ACU_EST_ESPRINCIPAL = ACU_EST_ESPRINCIPAL


    def to_dict(self):
        return {
            'ACU_EST_ID'         : self.ACU_EST_ID,
            'ACU_EST_UUID'       : self.ACU_EST_UUID,
            'ACU_EST_PARENTESCO' : self.ACU_EST_PARENTESCO,
            'ACU_EST_ACU_ID'     : self.ACU_EST_ACU_ID,
            'ACU_EST_EST_ID'     : self.ACU_EST_EST_ID,
            'ACU_EST_ESPRINCIPAL': self.ACU_EST_ESPRINCIPAL
        }
