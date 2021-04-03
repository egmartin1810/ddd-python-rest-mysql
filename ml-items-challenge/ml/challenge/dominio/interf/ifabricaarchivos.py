import abc
# Interface de FabricaArchivos
class IFabricaArchivos(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def crearArchivoLecturaStreameable(self, nombreArchivo, formatoArchivo, separadorColumnasArc, encodingArchivo):
        """
        Fabrica de objetos Archivo Streameable
        :param nombreArchivo: nombreArchivo
        :param formatoArchivo: formatoArchivo
        :param separadorColumnasArc: separadorColumnasArc
        :param encodingArchivo: encodingArchivo
        """

