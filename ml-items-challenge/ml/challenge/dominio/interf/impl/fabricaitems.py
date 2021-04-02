import abc
from ml.challenge.dominio.interf.ifabricaitems import IFabricaItems
from ml.challenge.dominio.entidades.item import Item
from ml.challenge.dominio.entidades.categoria import Categoria
from ml.challenge.dominio.entidades.moneda import Moneda
from ml.challenge.dominio.entidades.vendedor import Vendedor

# Por: Giovanni Martinez
# Fecha: 2021/03/31
# Descripción: Clase que implementa la inteface de IFabricaItems.
class FabricaItems(IFabricaItems):

    # Crear instancias de la clase de dominio Item
    def crearItem(self, idSitio, idItem, fechaInicio, precio, categoria, moneda, vendedor):
        return  Item(idSitio, idItem, fechaInicio, precio, categoria, moneda, vendedor)

    # Crear instancias de la clase de dominio Categoria
    def crearCategoria(self, idCategoria, nombreCategoria):
        return Categoria(idCategoria, nombreCategoria)

    # Crear instancias de la clase de dominio Moneda
    def crearMoneda(self, idMoneda, descripcionMoneda):
        return Moneda(idMoneda, descripcionMoneda)

    # Crear instancias de la clase de dominio Vendedor
    def crearVendedor(self, idVendedor, apodoVendedor):
        return Vendedor(idVendedor, apodoVendedor)

