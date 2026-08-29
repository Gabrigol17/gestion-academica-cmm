class Estudiante:

    def __init__(self, EST_ID, EST_UUID, EST_ESTADO_INSTITUCIONAL, EST_PER_ID):
        self.EST_ID                   = EST_ID
        self.EST_UUID                 = EST_UUID
        self.EST_ESTADO_INSTITUCIONAL = EST_ESTADO_INSTITUCIONAL
        self.EST_PER_ID               = EST_PER_ID


    def to_dict(self):
        return {
            'EST_ID'                  : self.EST_ID,
            'EST_UUID'                : self.EST_UUID,
            'EST_ESTADO_INSTITUCIONAL': self.EST_ESTADO_INSTITUCIONAL,
            'EST_PER_ID'              : self.EST_PER_ID
        }
