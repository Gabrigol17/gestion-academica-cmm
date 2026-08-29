class Grado:

    def __init__(self, GRAD_ID, GRAD_NOMBRE, GRAD_NIV_EDUC_ID):
        self.GRAD_ID          = GRAD_ID
        self.GRAD_NOMBRE      = GRAD_NOMBRE
        self.GRAD_NIV_EDUC_ID = GRAD_NIV_EDUC_ID


    def to_dict(self):
        return {
            'GRAD_ID'         : self.GRAD_ID,
            'GRAD_NOMBRE'     : self.GRAD_NOMBRE,
            'GRAD_NIV_EDUC_ID': self.GRAD_NIV_EDUC_ID
        }