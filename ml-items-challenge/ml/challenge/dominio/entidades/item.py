# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Items que representan articulos o productos a la venta
import ml.challenge.repositorio.persistencia.modelo.itemorm as itemorm
class Item:
    # Atributos
    __idSitio = ""
    __idItem = ""
    __fechaInicio = ""
    __precio = 0.0
    __categoria = {}
    __moneda = {}
    __vendedor = {}

    # Constructor
    def __init__(self, idSitio, idItem, fechaInicio, precio, categoria, moneda, vendedor):
        self.__idSitio = idSitio
        self.__idItem = idItem
        self.__fechaInicio = fechaInicio
        self.__precio = precio
        self.__categoria = categoria
        self.__moneda = moneda
        self.__vendedor = vendedor

    # Getters y Setters

    def getIdSitio(self):
        return self.__idSitio

    def getIdItem(self):
        return self.__idItem

    def getFechaInicio(self):
        return self.__fechaInicio

    def getPrecio(self):
        return self.__precio

    def getCategoria(self):
        return self.__categoria

    def getMoneda(self):
        return self.__moneda

    def getVendedor(self):
        return self.__vendedor

    def setIdSitio(self, idSitio):
        self.__idSitio = idSitio

    def setIdItem(self, idItem):
        self.__idItem = idItem

    def setFechaInicio(self, fechaInicio):
        self.__fechaInicio = fechaInicio

    def setPrecio(self, precio):
        self.__precio = precio

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def setMoneda(self, moneda):
        self.__moneda = moneda

    def setVendedor(self, vendedor):
        self.__vendedor = vendedor

    def __str__(self):
        valores = "idSitio: " + self.__idSitio + ", idItem: " + self.__idItem + ", fechaInicio: " \
                  + ( "" if not self.__fechaInicio else self.__fechaInicio) \
                  + ", precio: " + str(self.__precio) + ", categoria: " \
                  + ("" if not self.__categoria else self.__categoria.getNombreCategoria()) \
                  + ", moneda: " + ("" if not self.__moneda else self.__moneda.getDescripcionMoneda()) + ", vendedor: " \
                  + ( "" if not self.__vendedor else self.__vendedor.getApodoVendedor())
        return valores


    # Metodo para persistir el item
    def persistir(self):
        print("Entrando al método de Item.persistir....")

        itemper = itemorm.ItemORM(site=self.__idSitio, id=self.__idItem, price=self.__precio,start_time=self.__fechaInicio,
                                  name=(None if not self.__categoria else self.__categoria.getNombreCategoria()),
                                  description=(None if not self.__moneda else self.__moneda.getDescripcionMoneda()),
                                  nickname=( None if not self.__vendedor else self.__vendedor.getApodoVendedor()))
        itemper.save()
        print("Saliendo al método de Item.persistir....")