import abc
# Interface de BuscadorItems
class IBuscadorDatosItems(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def recuperarDatosBasicosItem(self, idSitio, idItem):
        """
        Recupera los datos de un Item específico en el sistema proveedor
        :param idSitio: Identificador del sitio que pertenece el item
        :param idItem: Identificador único del item.
        :return: Objeto con información básica del Item.
        """

    @abc.abstractmethod
    def recuperarDatosCategoria(self, idCategoria):
        """
        Recupera los datos de una Cateogoría específica de un Item
        :param idCategoria: Identificador de la categoría
        :return: Objeto con información básica de la Categoría.
        """

    @abc.abstractmethod
    def recuperarDatosMoneda(self, idMoneda):
        """
        Recupera los datos de una Moneda específica de un Item
        :param idMoneda: Identificador de la Moneda
        :return: Objeto con información básica de la Moneda.
        """
    @abc.abstractmethod
    def recuperarDatosUsuario(self, idUsuario):
        """
        Recupera los datos de un Usuario
        :param idUsuario: Identificador único del usuario
        :return: Objeto con información básica de un usuario.
        """