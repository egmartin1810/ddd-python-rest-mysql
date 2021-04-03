import abc

class IProcesadorItems(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def realizarTransformacionesItem(self, idSitio, idItem):
        """
        Inteface del componente de dominio GestorItems para procesar los items.
        :param item: item a procesar
        :return: no retorna nada
        """
    @abc.abstractmethod
    def guardarItem(self):
        """
        Inteface del componente de dominio para guardar items.
        :return: no objeto de dominio de la entidad item
        """

    @abc.abstractmethod
    def eliminarTodosLosItemsPersistidos(self):
        """
        Inteface del componente de dominio para eliminar todos los items persistidos.
        :return: número de items eliminados.
        """