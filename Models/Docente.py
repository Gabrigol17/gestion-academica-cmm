class Docente:

    def __init__(self, DOC_ID, DOC_UUID, DOC_ESTADO, DOC_PER_ID):
        self.DOC_ID     = DOC_ID
        self.DOC_UUID   = DOC_UUID
        self.DOC_ESTADO = DOC_ESTADO
        self.DOC_PER_ID = DOC_PER_ID


    def to_dict(self):
        return {
            'DOC_ID'    : self.DOC_ID,
            'DOC_UUID'  : self.DOC_UUID,
            'DOC_ESTADO': self.DOC_ESTADO,
            'DOC_PER_ID': self.DOC_PER_ID
        }
