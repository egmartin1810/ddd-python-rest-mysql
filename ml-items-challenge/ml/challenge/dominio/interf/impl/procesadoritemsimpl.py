import sys
import abc
from ml.challenge.dominio.interf.iprocesadoritems import IProcesadorItems
import ml.challenge.dominio.interf.impl.fabricaitems as fabricaitems
import ml.challenge.dominio.interf.impl.buscadordatositems as busdatosItems
import ml.challenge.repositorio.adaptador.servicios.meli.excepciones.respuestahttpexception as respuestahttpexception

# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que implementa la inteface para el procesesamiento de items.
class ProcesadorItemsImpl(IProcesadorItems):

    #Atributos
    item = {}
    buscadorDatositems = busdatosItems.BuscadorDatosItems("propiedades")

    def procesarItem(self, idSitio, idItem):
        print("Entrando al método de ProcesadorItemsImpl.procesarItems....")
        # recuperar los datos básicos del item.
        # llamar el cliente del servicio la claveItem (concatenando idSitio y idItem)
        objRespuestaClienteItem = {}
        try:
            objRespuestaClienteItem = self.buscadorDatositems.recuperarDatosBasicosItem(idSitio, idItem)
        except respuestahttpexception.RecursoNoEncontradoException as err:
            print(f'No se encontraron datos para el item: {idSitio+idItem}  de MELI: {err.message}')

        # Datos recuperados del servicio de Item
        resFechaInicial = objRespuestaClienteItem.get('start_time')
        resPrecio = objRespuestaClienteItem.get('price')
        resCategoriaId = objRespuestaClienteItem.get('category_id')
        resMonedaId = objRespuestaClienteItem.get('currency_id')
        resVendedorId = str(objRespuestaClienteItem.get('seller_id'))

        # Generar objetos de dominio a traves de la fabricaItem
        fabricaItems = fabricaitems.FabricaItems()
        # recuperar Nombre Categoria si existe el valor
        if not resCategoriaId is None:
            objRespClienteCatgria = self.buscadorDatositems.recuperarDatosCategoria(resCategoriaId)
            # crear objeto entidad Categoria
            objCategoria = fabricaItems.crearCategoria(resCategoriaId, objRespClienteCatgria['name'])
        else:
            objCategoria = {}
        # recuperar Descripción Moneda si existe el valor
        if not resMonedaId is None:
            objRespClienteMoneda = self.buscadorDatositems.recuperarDatosMoneda(resMonedaId)
            # crear objeto entidad Moneda
            objMoneda = fabricaItems.crearMoneda(resMonedaId, objRespClienteMoneda['description'])
        else:
            objMoneda = {}

        # recuperar Apodo Vendedor si existe el valor
        if not resVendedorId == "None":
            objRespClienteUsuario = self.buscadorDatositems.recuperarDatosUsuario(resVendedorId)
            # crear objeto entidad Vendedor
            objVendedor = fabricaItems.crearVendedor(resVendedorId, objRespClienteUsuario['nickname'])
        else:
            objVendedor = {}

        # crear objeto de entidad de dominio item
        self.item = fabricaItems.crearItem(idSitio, idItem, resFechaInicial, resPrecio, objCategoria
                                     , objMoneda, objVendedor)

        print("Objeto Item: ", self.item)
        # persistir el objeto de entidad item
        self.item.persistir()
        print("Saliendo del método de ProcesadorItemsImpl.procesarItems....")

        def __sizeof__(self):
            return object.__sizeof__(self) + \
                   sum(sys.getsizeof(v) for v in self.__dict__.values())