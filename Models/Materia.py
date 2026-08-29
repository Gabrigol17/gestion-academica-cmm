class Materia:

    def __init__(self, MAT_ID, MAT_NOMBRE):
        self.MAT_ID     = MAT_ID
        self.MAT_NOMBRE = MAT_NOMBRE


    def to_dict(self):
        return {
            'MAT_ID'    : self.MAT_ID,
            'MAT_NOMBRE': self.MAT_NOMBRE
        }