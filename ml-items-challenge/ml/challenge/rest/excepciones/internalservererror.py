# Por: Giovanni Martinez
# Fecha: 2021/03/31
# Descripción: Excepion HTTP para responder a los errores internos del servicio REST.
class InternalServerError(Exception):
    status_code = 500
    message = "InternalServerError"

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv