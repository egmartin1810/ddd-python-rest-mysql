# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase Moneda de paises
class Moneda:

    #Atributos
    __idMoneda = ""
    __descripcionMoneda = ""

    #Constructor
    def __init__(self, idMoneda, descripcionMoneda):
        self.__idMoneda = idMoneda
        self.__descripcionMoneda = descripcionMoneda

    # Getters y Setters

    def getIdMoneda(self):
        return self.__idMoneda

    def getDescripcionMoneda(self):
        return self.__descripcionMoneda

    def setIdMoneda(self, idMoneda):
        self.__idMoneda = idMoneda

    def setDescripcionMoneda(self, descripcionMoneda):
        self.__descripcionMoneda
