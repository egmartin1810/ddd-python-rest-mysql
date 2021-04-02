# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Exepcion que se lanza cuando .
class RespuestaHTTPException(Exception):

    def __init__(self, statusCode, message):
        self.statusCode = statusCode
        self.message = message
        super().__init__(message)

class RecursoNoEncontradoException(RespuestaHTTPException):

    def __init__(self, statusCode, message):
        super().__init__(statusCode, message)