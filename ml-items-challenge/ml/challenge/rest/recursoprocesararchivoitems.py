import multiprocessing
import threading
import os
import time
import csv
import concurrent.futures
import sqlalchemy
from main import app
from ml.challenge.rest.excepciones.internalservererror import InternalServerError
import ml.challenge.dominio.interf.impl.procesadoritemsimpl as procesadoritemsimpl
import ml.challenge.dominio.interf.impl.fabricaarchivos as fabricaarchivo



# Por: Giovanni Martinez
# Fecha: 2021/03/31
# Descripción: REcurso que representa el método post procesarArchivoItems, representan articulos o productos a la venta
class RecursoProcesarArchivoItems():

    # Generar objeto fábrica para construir objetos de las entidades de dominio
    fabricaArchivos = fabricaarchivo.FabricaArchivos()

    # Metodo que representa le método POST almacenardatositems con la lógica para leer un archivo, llamar
    # algunas APIs (Servicios Proveedores) y persistirlos.
    # Parámetros no requiere
    # return: Objeto de respuesta de la ejecución el metodo POST.
    def procesarArchivoItemsStreameable(self):
        # Crear objeto de dominio para procesar el archivo.
        print("Entrando al método RecursoProcesarArchivoItems.procesarArchivoItemsStreameable....")
        try:
            # Validar propiedad configurable app.config['BORRAR_TODOS_REGISTROS_ITEMSBD']
            if app.config['BORRAR_TODOS_REGISTROS_ITEMSBD']:
                # Eliminar todos los registros de Items que están persisitidos.
                domProcItem = procesadoritemsimpl.ProcesadorItemsImpl()
                domProcItem.eliminarTodosLosItemsPersistidos()

            # Crear objeto de entidad archivo a traves de la fábrica fabricaarchivo.
            domArchivoStr = self.fabricaArchivos.crearArchivoLecturaStreameable(app.config['ARCHIVO_NOMBRE'],
                                                                          app.config['ARCHIVO_FORMATO'],
                                                                          app.config['ARCHIVO_SEPARADOR'],
                                                                          app.config['ARCHIVO_ENCODING'])
            # procesar el archivo con los identificadores de los items
            respuesta = self.__procesarArchivosItems(domArchivoStr,
                                                             app.config['THREADPOOLEXECUTOR_NUM_WORKERS'])
        except Exception as err:
            print(f'(Exception) Error En la Ejecución del servicio: {err}')
            raise InternalServerError('Error Interno en el Sistema.', status_code=500)
        print("Saliendo del método RecursoProcesarArchivoItems.procesarArchivoItemsStreameable....")
        return respuesta

    # Método que procesa un archivo de tipo streameable con los siguientes parametros para su lectura.
    # Parámetros: objeto de dominio arvhivo y numWorkers para procesamiento concurrente de hilos.
    # Rerturn: Objeto con los valores de procesamiento del archivo.
    def __procesarArchivosItems(self, domArchivoStr, numWorkers):
        print("Entrando al método de RecursoProcesarArchivoItems.procesarArchivoItemsStreameable....")
        nombreCompletoArchivo = domArchivoStr.getNombreArchivo() + "." + domArchivoStr.getFormatoArchivo()
        print(f'Archivo ha leer:  {nombreCompletoArchivo}, '
              f'Tamaño del archivo es {os.stat(nombreCompletoArchivo).st_size / (1024 * 1024)} MB')

        # Empezar a contar el tiempo del procesamiento del archivo.
        start_time = time.time()
        # Abrir el archivo que está en la configuración
        with open(nombreCompletoArchivo, encoding=domArchivoStr.getEncodingArchivo()) as archivo:
            datareader = csv.reader(archivo, delimiter=domArchivoStr.getSeparadorColumnasArc())
            # Se lee el header del arvhivo
            header = next(datareader)
            count = 0
            # Ejecutar a través de varios hilos gestionados por ThreadPoolExecutor
            with concurrent.futures.ThreadPoolExecutor(max_workers=numWorkers) as executor:
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
        objRespuesta = {'tiempo': respuesta, 'registrosProcesados': count, 'numWorkersHilos': numWorkers}
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
        # Realizamos las consultas necesarias a los servicios proveedores para completar la entidad de dominio.
        procitem_.realizarTransformacionesItem(idSitio, idItem)
        # Guarda el item procesado.
        procitem_.guardarItem()
