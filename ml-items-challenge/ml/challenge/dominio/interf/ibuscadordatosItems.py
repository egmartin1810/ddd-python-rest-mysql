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
    def recuperarDatosEntidades2Nivel(self, dictServAllamar):
        """
        Recupera los datos de un Usuario
        :param dictServAllamar: Dicionario con el identificador del servicio a llamar y los parámetros.
        :return: Objeto con información Recuperada del servicio.
        """