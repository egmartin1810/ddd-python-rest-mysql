import abc
# Interface de FabricaItems
class IFabricaItems(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def crearItem(self, idSitio, idItem, fechaInicio, precio, categoria, moneda, vendedor):
        """
        Fabrica de objetos Items
        :param idSitio: idSitio
        :param idItem: idItem
        :param fechaInicio: fechaInicio
        :param precio: precio
        :param idCategoria: idCategoria
        :param nombreCategoria: nombreCategoria
        :param idMoneda: idMoneda
        :param descripcionMoneda: descripcionMoneda
        :param idVendedor: idVendedor
        :param apodoVendedor: apodoVendedor
        :return: objeto de tipo etidades.item
        """

    def crearCategoria(self, idCategoria, nombreCategoria):
        """
        Fabrica de objetos de dominio Categoria
        :param idCategoria: idCategoria
        :param nombreCategoria: nombreCategoria
        :return: objeto de tipo etidades.Categoria
        """

    def crearMoneda(self, idMoneda, descripcionMoneda):
        """
        Fabrica de objetos de dominio Moneda
        :param idMoneda: idMoneda
        :param descripcionMoneda: descripcionMoneda
        :return: objeto de tipo etidades.Moneda
        """

    def crearVendedor(self, idVendedor, apodoVendedor):
        """
        Fabrica de objetos de dominio Vendedor
        :param idVendedor: idVendedor
        :param apodoVendedor: apodoVendedor
        :return: objeto de tipo etidades.Vendedor
        """