class ComponenteEvaluativo:

    def __init__(
        self,
        COM_EVA_ID,
        COM_EVA_PORCENTAJE,
        COM_EVA_PER_ACA_ID,
        COM_EVA_TIPO_COMP_ID
    ):
        self.COM_EVA_ID           = COM_EVA_ID
        self.COM_EVA_PORCENTAJE   = COM_EVA_PORCENTAJE
        self.COM_EVA_PER_ACA_ID   = COM_EVA_PER_ACA_ID
        self.COM_EVA_TIPO_COMP_ID = COM_EVA_TIPO_COMP_ID


    def to_dict(self):
        return {
            'COM_EVA_ID'          : self.COM_EVA_ID,
            'COM_EVA_PORCENTAJE'  : self.COM_EVA_PORCENTAJE,
            'COM_EVA_PER_ACA_ID'  : self.COM_EVA_PER_ACA_ID,
            'COM_EVA_TIPO_COMP_ID': self.COM_EVA_TIPO_COMP_ID
        }