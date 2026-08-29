class CursoVigencia:

    def __init__(self, CUR_VIG_ID, CUR_VIG_UUID, CUR_VIG_LETRA, CUR_VIG_VIG_ID, CUR_VIG_GRAD_ID):
        self.CUR_VIG_ID      = CUR_VIG_ID
        self.CUR_VIG_UUID    = CUR_VIG_UUID
        self.CUR_VIG_LETRA   = CUR_VIG_LETRA
        self.CUR_VIG_VIG_ID  = CUR_VIG_VIG_ID
        self.CUR_VIG_GRAD_ID = CUR_VIG_GRAD_ID


    def to_dict(self):
        return {
            'CUR_VIG_ID'     : self.CUR_VIG_ID,
            'CUR_VIG_UUID'   : self.CUR_VIG_UUID,
            'CUR_VIG_LETRA'  : self.CUR_VIG_LETRA,
            'CUR_VIG_VIG_ID' : self.CUR_VIG_VIG_ID,
            'CUR_VIG_GRAD_ID': self.CUR_VIG_GRAD_ID
        }