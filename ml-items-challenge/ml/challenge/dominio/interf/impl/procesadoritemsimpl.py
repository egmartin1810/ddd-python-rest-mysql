import sys
import abc
import concurrent.futures
from ml.challenge.dominio.interf.iprocesadoritems import IProcesadorItems
import ml.challenge.dominio.interf.impl.fabricaitems as fabricaitems
import ml.challenge.dominio.interf.impl.buscadordatositems as busdatosItems
import ml.challenge.repositorio.adaptador.servicios.meli.excepciones.respuestahttpexception as respuestahttpexception
import ml.challenge.repositorio.persistencia.modelo.itemorm as itemorm


# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que implementa la inteface para el procesesamiento de items.
class ProcesadorItemsImpl(IProcesadorItems):


    # Atributos
    item = {}
    categoria = {}
    moneda = {}
    vendedor = {}
    buscadorDatositems = busdatosItems.BuscadorDatosItems()
    # Generar objeto fábrica para construir objetos de las entidades de dominio
    fabricaItems = fabricaitems.FabricaItems()

    #Métodos
    # Metodo para construir el item con base a la información de los sistemas terceros.
    def realizarTransformacionesItem(self, idSitio, idItem):
        print("Entrando al método de ProcesadorItemsImpl.procesarItems....")
        # recuperar los datos básicos del item.
        # llamar el cliente del servicio la claveItem (concatenando idSitio y idItem)
        objRespuestaClienteItem = {}
        dictRqServicios = {'srv': 'SRVBE_ITEMS', 'parametro': idSitio+idItem}
        try:
            objRespuestaClienteItem = self.buscadorDatositems.recuperarDatosBasicosItem(dictRqServicios)
        except respuestahttpexception.RecursoNoEncontradoException as err:
            print(f'No se encontraron datos para el item: {idSitio + idItem}  de MELI: {err.message}')

        # Datos recuperados del servicio de Item
        resFechaInicial = objRespuestaClienteItem.get('start_time')
        resPrecio = objRespuestaClienteItem.get('price')
        resCategoriaId = objRespuestaClienteItem.get('category_id')
        resMonedaId = objRespuestaClienteItem.get('currency_id')
        resVendedorId = str(objRespuestaClienteItem.get('seller_id'))
        # Procesar los otros llamados a la API de forma concurrente.
        self.realizarTransDatosItemNivel2Concurrente(resCategoriaId, resMonedaId, resVendedorId)
        # crear objeto de entidad de dominio item
        self.item = self.fabricaItems.crearItem(idSitio, idItem, resFechaInicial, resPrecio, self.categoria
                                                , self.moneda, self.vendedor)
        print("Saliendo del método de ProcesadorItemsImpl.procesarItems....")
        return self.item

    # Metodo para guardar el item en el sistema.
    def guardarItem(self):
        print("Entrando del método de ProcesadorItemsImpl.guardarItem....")
        print("Objeto Item a guardar: ", self.item)
        self.item.persistir()
        print("Saliendo del método de ProcesadorItemsImpl.guardarItem. Item: ",
              self.item.getIdSitio() + self.item.getIdItem())

    # Metodo para eliminar todos los items persistidos.
    def eliminarTodosLosItemsPersistidos(self):
        print("Entrando del método de ProcesadorItemsImpl.eliminarTodosLosItemsPersistidos....")
        # Eliminar TODOS datos de items en BD, para ejecuciones repetitivas
        itemper = itemorm.ItemORM()
        numRegEliminados = itemper.deleteAll()
        print("Saliendo del método de ProcesadorItemsImpl.eliminarTodosLosItemsPersistidos....")
        return numRegEliminados

    # recuperar los datos básicos del item.
    # llamar el cliente del servicio de los datos de nivel dos del item.
    # los llamados a estos servicios se van a hacer de forma concurrente
    def realizarTransDatosItemNivel2Concurrente(self, resCategoriaId, resMonedaId, resVendedorId):

        listaSrvsAllamar = []
        # recuperar Nombre Categoria si existe el valor
        if not resCategoriaId is None:
            listaSrvsAllamar.append({'srv': 'SRVBE_CATEGORIAS', 'parametro': resCategoriaId})
        # recuperar Descripción Moneda si existe el valor
        if not resMonedaId is None:
            listaSrvsAllamar.append({'srv': 'SRVBE_MONEDAS', 'parametro': resMonedaId})
        # recuperar Apodo Vendedor si existe el valor
        if not resVendedorId == "None":
            listaSrvsAllamar.append({'srv': 'SRVBE_USUARIOS', 'parametro': resVendedorId})
        tamanoListaSrv = len(listaSrvsAllamar)

        # Validar si el tamaño de la lista es mayor a 0 para crear por lo menos un hilo.
        if tamanoListaSrv > 0:
            # Ejecutar a través de varios hilos gestionados por ThreadPoolExecutor
            with concurrent.futures.ThreadPoolExecutor(max_workers=tamanoListaSrv) as executor:
                futures = []
                for srvAllamar in listaSrvsAllamar:
                    futures.append(executor.submit(self.buscadorDatositems.recuperarDatosEntidades2Nivel,
                                                   dictServAllamar=srvAllamar))
                    # Recibir las respuestas y procesarlas.
                    for future in concurrent.futures.as_completed(futures):
                        if (future.result()['srv'] == 'SRVBE_CATEGORIAS'):
                            # crear objeto entidad Categoria
                            self.categoria = self.fabricaItems.crearCategoria(resCategoriaId, future.result()['name'])
                        if (future.result()['srv'] == 'SRVBE_MONEDAS'):
                            # crear objeto entidad Categoria
                            self.moneda = self.fabricaItems.crearMoneda(resMonedaId, future.result()['description'])
                        if (future.result()['srv'] == 'SRVBE_USUARIOS'):
                            # crear objeto entidad Categoria
                            self.vendedor = self.fabricaItems.crearVendedor(resVendedorId, future.result()['nickname'])

    def __sizeof__(self):
        return object.__sizeof__(self) + \
               sum(sys.getsizeof(v) for v in self.__dict__.values())
