# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase Vendedores
class Vendedor:

    #Atributos
    __idVendedor = 0
    __apodoVendedor = ""

    #Constructor
    def __init__(self, idVendedor, apodoVendedor):
        self.__idVendedor = idVendedor
        self.__apodoVendedor = apodoVendedor

    # Getters y Setters
    def getIdVendedor(self):
        return self.__idVendedor

    def getApodoVendedor(self):
        return self.__apodoVendedor

    def setIdVendedor(self, idVendedor):
        self.__idVendedor = idVendedor

    def setApodoVendedor(self, apodoVendedor):
        self.__apodoVendedor = apodoVendedor
