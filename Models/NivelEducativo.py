class NivelEducativo:

    def __init__(self, NIV_EDUC_ID, NIV_EDUC_NOMBRE):
        self.NIV_EDUC_ID     = NIV_EDUC_ID
        self.NIV_EDUC_NOMBRE = NIV_EDUC_NOMBRE


    def to_dict(self):
        return {
            'NIV_EDUC_ID'    : self.NIV_EDUC_ID,
            'NIV_EDUC_NOMBRE': self.NIV_EDUC_NOMBRE
        }