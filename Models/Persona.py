class Persona:

    def __init__(
        self,
        PER_ID,
        PER_UUID,
        PER_TIPO_DOCUMENTO,
        PER_NUMERO_DOCUMENTO,
        PER_PRIMER_NOMBRE,
        PER_SEGUNDO_NOMBRE,
        PER_PRIMER_APELLIDO,
        PER_SEGUNDO_APELLIDO,
        PER_CORREO_INSTITUCIONAL,
        PER_FECHA_NACIMIENTO,
        PER_ROL_ID
    ):
        self.PER_ID                   = PER_ID
        self.PER_UUID                 = PER_UUID
        self.PER_TIPO_DOCUMENTO       = PER_TIPO_DOCUMENTO
        self.PER_NUMERO_DOCUMENTO     = PER_NUMERO_DOCUMENTO
        self.PER_PRIMER_NOMBRE        = PER_PRIMER_NOMBRE
        self.PER_SEGUNDO_NOMBRE       = PER_SEGUNDO_NOMBRE
        self.PER_PRIMER_APELLIDO      = PER_PRIMER_APELLIDO
        self.PER_SEGUNDO_APELLIDO     = PER_SEGUNDO_APELLIDO
        self.PER_CORREO_INSTITUCIONAL = PER_CORREO_INSTITUCIONAL
        self.PER_FECHA_NACIMIENTO     = PER_FECHA_NACIMIENTO
        self.PER_ROL_ID               = PER_ROL_ID


    def to_dict(self):
        return {
            'PER_ID'                  : self.PER_ID,
            'PER_UUID'                : self.PER_UUID,
            'PER_TIPO_DOCUMENTO'      : self.PER_TIPO_DOCUMENTO,
            'PER_NUMERO_DOCUMENTO'    : self.PER_NUMERO_DOCUMENTO,
            'PER_PRIMER_NOMBRE'       : self.PER_PRIMER_NOMBRE,
            'PER_SEGUNDO_NOMBRE'      : self.PER_SEGUNDO_NOMBRE,
            'PER_PRIMER_APELLIDO'     : self.PER_PRIMER_APELLIDO,
            'PER_SEGUNDO_APELLIDO'    : self.PER_SEGUNDO_APELLIDO,
            'PER_CORREO_INSTITUCIONAL': self.PER_CORREO_INSTITUCIONAL,
            'PER_FECHA_NACIMIENTO'    : self.PER_FECHA_NACIMIENTO.isoformat(),
            'PER_ROL_ID'              : self.PER_ROL_ID
        }
