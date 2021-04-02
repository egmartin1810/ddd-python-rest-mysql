import abc
# Interface de ProcesadorArchivo
class IProcesadorArchivo(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def procesarArchivoStreameable(self):
        """
        Carga un archivo de tipo streameable con los siguientes parametros para su lectura.
        :param nombreArchivo: nombre del Archivo que se va a leer
        :param formato: formato del archivo ("csv, txt, ,jsonfile")
        :param separador: caracter de sepatación del formato del archivo que se va a leer (",",";","|")
        :param encoding: Encoding para abrir el archivo ("utf-8")
        :return: objeto de la lectura del archivo.
        """