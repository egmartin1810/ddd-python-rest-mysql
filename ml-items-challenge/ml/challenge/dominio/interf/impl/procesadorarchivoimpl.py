import abc
import multiprocessing
import threading
import os
import time
import csv
import concurrent.futures
import sqlalchemy
import ml.challenge.dominio.interf.impl.procesadoritemsimpl as procesadoritemsimpl
from ml.challenge.dominio.interf.iprocesadorarchivo import IProcesadorArchivo
# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que implementa la inteface para el procesesamiento o lectura de un archivo.
class ProcesadorArchivoImpl(IProcesadorArchivo):

    # Atributos
    __nombreArchivo = ""
    __formatoArchivo = ""
    __separadorColumnasArc = ""
    __encodingArchivo = ""
    __numWorkers = 5

    # Constructor
    def __init__(self, nombreArchivo, formatoArchivo, separadorColumnasArc, encodingArchivo, numWorkers):
        self.__nombreArchivo = nombreArchivo
        self.__formatoArchivo = formatoArchivo
        self.__separadorColumnasArc = separadorColumnasArc
        self.__encodingArchivo = encodingArchivo
        self.__numWorkers = numWorkers

    # Getters y Setters

    def getNombreArchivo(self):
        return self.__nombreArchivo

    def getFormatoArchivo(self):
        return self.__formatoArchivo

    def getSeparadorColumnasArc(self):
        return self.__separadorColumnasArc

    def getEncodingArchivo(self):
        return self.__encodingArchivo

    def getNumWorkers(self):
        return  self.__numWorkers

    def setNombreArchivo(self, nombreArchivo):
        self.__nombreArchivo = nombreArchivo

    def setFormatoArchivo(self, formatoArchivo):
        self.__formatoArchivo = formatoArchivo

    def setSeparadorColumnasArc(self, separadorColumnasArc):
        self.__separadorColumnasArc = separadorColumnasArc

    def setEncodingArchivo(self, encodingArchivo):
        self.__encodingArchivo = encodingArchivo

    def setEncodingArchivo(self, numWorkers):
        self.__numWorkers = numWorkers

    # Método que procesa un archivo de tipo streameable con los siguientes parametros para su lectura.
    def procesarArchivoStreameable(self):
        print("Entrando al método de ProcesadorArchivoImpl.leerArchivoStreameable....")

        nombreCompletoArchivo = self.__nombreArchivo+"."+self.__formatoArchivo
        print(f'Archivo ha leer:  {nombreCompletoArchivo}, Tamaño del archivo es {os.stat(nombreCompletoArchivo).st_size / (1024 * 1024)} MB')

        # Empezar a contar el tiempo del procesamiento del archivo.
        start_time = time.time()
        # Abrir el archivo que está en la configuración
        with open(nombreCompletoArchivo, encoding=self.__encodingArchivo) as archivo:
            datareader = csv.reader(archivo, delimiter=self.__separadorColumnasArc)
            header = next(datareader)
            print(f'Header {header}')
            count = 0
            # Ejecutar a través de varios hilos gestionados por ThreadPoolExecutor
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.__numWorkers) as executor:
                futures = []
                for registro in datareader:
                    futures.append(executor.submit(self.__procesarRegistro, registro=registro))
                # Validar si la respuesta de la ejecución fue error para loguearlo en el sistema.
                for future in concurrent.futures.as_completed(futures):
                    count += 1
                    try:
                        print(future.result())
                    except sqlalchemy.exc.IntegrityError as err:
                        print(f'Error al persistir el registro : {err}')
                    except Exception as err:
                        print(f'(Exception) Error al persistir el registro : {err}')

        respuesta = ("Tiempo de procesamiento %s seconds" % (time.time() - start_time))
        print(f'Número de lineas procesadas del archivo es: {count}')
        print(respuesta)
        print("Saliendo del método de ProcesadorArchivoImpl.leerArchivoStreameable....")
        objRespuesta = {'tiempo': respuesta, 'registrosProcesados': count}
        return objRespuesta

    # Método que procesa un registro que representa un item,de un archivo, para ejecutarlo con hilos concurrentes.
    def __procesarRegistro(self, registro):
        print("PID: %s, Process Name: %s, Thread Name: %s" % (
            os.getpid(),
            multiprocessing.current_process().name,
            threading.current_thread().name)
              )
        idSitio = registro[0]
        idItem = registro[1]
        # Instanciamos el objeto de dominio ProcesadorItemsImpl para cada registro
        procitem_ = procesadoritemsimpl.ProcesadorItemsImpl()
        procitem_.realizarTransformacionesItem(idSitio, idItem)
        # Guarda el item procesado.
        procitem_.guardarItem()