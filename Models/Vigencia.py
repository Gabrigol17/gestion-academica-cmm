class Vigencia:

    def __init__(self, VIG_ID, VIG_UUID, VIG_AÑO):
        self.VIG_ID   = VIG_ID
        self.VIG_UUID = VIG_UUID
        self.VIG_AÑO  = VIG_AÑO


    def to_dict(self):
        return {
            'VIG_ID'   : self.VIG_ID,
            'VIG_UUID' : self.VIG_UUID,
            'VIG_AÑO'  : self.VIG_AÑO
        }
