# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que representa la firma del request para consumir los serivios o API  de MELI.

class ServiciosMELIRq():
    # atributos
    __srv = {}
    __parametro = {}

    # Constructor
    def __init__(self, srvValor, parametroValor):
        self.__srv = {'srv': srvValor}
        self.__parametro = {'parametro': parametroValor}

    # Getters y Setters

    def getSrv(self):
        return self.__srv

    def getParametro(self):
        return self.__parametro

    def setSrv(self, srv):
        self.__srv = srv

    def setParametro(self, parametro):
        self.__parametro = parametro
