class DiaSemana:

    def __init__(self, DIA_SEM_ID, DIA_SEM_DIA):
        self.DIA_SEM_ID  = DIA_SEM_ID
        self.DIA_SEM_DIA = DIA_SEM_DIA


    def to_dict(self):
        return {
            'DIA_SEM_ID' : self.DIA_SEM_ID,
            'DIA_SEM_DIA': self.DIA_SEM_DIA
        }