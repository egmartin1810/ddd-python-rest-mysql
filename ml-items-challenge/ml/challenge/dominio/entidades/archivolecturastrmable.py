# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción:Representación de un archivo de registros de items, para su lectura .
class ArchivoLecturaStrmable():

    # Atributos
    __nombreArchivo = ""
    __formatoArchivo = ""
    __separadorColumnasArc = ""
    __encodingArchivo = ""

    # Constructor
    def __init__(self, nombreArchivo, formatoArchivo, separadorColumnasArc, encodingArchivo):
        self.__nombreArchivo = nombreArchivo
        self.__formatoArchivo = formatoArchivo
        self.__separadorColumnasArc = separadorColumnasArc
        self.__encodingArchivo = encodingArchivo

    # Getters y Setters

    def getNombreArchivo(self):
        return self.__nombreArchivo

    def getFormatoArchivo(self):
        return self.__formatoArchivo

    def getSeparadorColumnasArc(self):
        return self.__separadorColumnasArc

    def getEncodingArchivo(self):
        return self.__encodingArchivo

    def setNombreArchivo(self, nombreArchivo):
        self.__nombreArchivo = nombreArchivo

    def setFormatoArchivo(self, formatoArchivo):
        self.__formatoArchivo = formatoArchivo

    def setSeparadorColumnasArc(self, separadorColumnasArc):
        self.__separadorColumnasArc = separadorColumnasArc

    def setEncodingArchivo(self, encodingArchivo):
        self.__encodingArchivo = encodingArchivo


