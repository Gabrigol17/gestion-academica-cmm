class AsignacionAcademica:

    def __init__(
        self,
        ASIG_ACA_ID,
        ASIG_ACA_UUID,
        ASIG_ACA_ESTADO,
        ASIG_ACA_DOC_ID,
        ASIG_ACA_MAT_ID,
        ASIG_ACA_CUR_VIG_ID
    ):
        self.ASIG_ACA_ID         = ASIG_ACA_ID
        self.ASIG_ACA_UUID       = ASIG_ACA_UUID
        self.ASIG_ACA_ESTADO     = ASIG_ACA_ESTADO
        self.ASIG_ACA_DOC_ID     = ASIG_ACA_DOC_ID
        self.ASIG_ACA_MAT_ID     = ASIG_ACA_MAT_ID
        self.ASIG_ACA_CUR_VIG_ID = ASIG_ACA_CUR_VIG_ID


    def to_dict(self):
        return {
            'ASIG_ACA_ID'        : self.ASIG_ACA_ID,
            'ASIG_ACA_UUID'      : self.ASIG_ACA_UUID,
            'ASIG_ACA_ESTADO'    : self.ASIG_ACA_ESTADO,
            'ASIG_ACA_DOC_ID'    : self.ASIG_ACA_DOC_ID,
            'ASIG_ACA_MAT_ID'    : self.ASIG_ACA_MAT_ID,
            'ASIG_ACA_CUR_VIG_ID': self.ASIG_ACA_CUR_VIG_ID
        }