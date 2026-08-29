class TipoComponente:

    def __init__(self, TIPO_COMP_ID, TIPO_COMP_NOMBRE):
        self.TIPO_COMP_ID     = TIPO_COMP_ID
        self.TIPO_COMP_NOMBRE = TIPO_COMP_NOMBRE


    def to_dict(self):
        return {
            'TIPO_COMP_ID'    : self.TIPO_COMP_ID,
            'TIPO_COMP_NOMBRE': self.TIPO_COMP_NOMBRE
        }