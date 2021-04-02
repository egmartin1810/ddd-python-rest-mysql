import abc

class IProcesadorItems(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def procesarItem(self, idSitio, idItem):
        """
        Inteface del componente de dominio GestorItems para procesar los items.
        :param item: item a procesar
        :return: no retorna nada
        """