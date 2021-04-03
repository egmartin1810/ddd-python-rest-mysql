# Por: Giovanni Martinez
# Fecha: 2021/03/31
# Descripción: Clase que implementa la inteface de IFabricaArchivos.
from ml.challenge.dominio.entidades.archivolecturastrmable import ArchivoLecturaStrmable
from ml.challenge.dominio.interf.ifabricaarchivos import IFabricaArchivos

class FabricaArchivos(IFabricaArchivos):

    # Crear instancias de la clase de dominio ArchivoLectura
    def crearArchivoLecturaStreameable(self, nombreArchivo, formatoArchivo, separadorColumnasArc, encodingArchivo):
        return ArchivoLecturaStrmable(nombreArchivo, formatoArchivo, separadorColumnasArc, encodingArchivo)