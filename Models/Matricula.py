class Matricula:

    def __init__(self, MATR_ID, MATR_UUID, MATR_EST_ID, MATR_CUR_VIG_ID):
        self.MATR_ID         = MATR_ID
        self.MATR_UUID       = MATR_UUID
        self.MATR_EST_ID     = MATR_EST_ID
        self.MATR_CUR_VIG_ID = MATR_CUR_VIG_ID


    def to_dict(self):
        return {
            'MATR_ID'        : self.MATR_ID,
            'MATR_UUID'      : self.MATR_UUID,
            'MATR_EST_ID'    : self.MATR_EST_ID,
            'MATR_CUR_VIG_ID': self.MATR_CUR_VIG_ID
        }