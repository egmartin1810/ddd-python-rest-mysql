import abc
from ml.challenge.dominio.interf.ibuscadordatosItems import IBuscadorDatosItems
import ml.challenge.dominio.entidades.item as entidadItem
import ml.challenge.dominio.entidades.categoria as entidadCategoria
import ml.challenge.dominio.entidades.moneda as emoneda
import ml.challenge.dominio.entidades.vendedor as evendedor
import ml.challenge.repositorio.adaptador.servicios.meli.srvconsultasmeli as srvconsultasmeli

# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que implementa la inteface de Buscador Items.
class BuscadorDatosItems(IBuscadorDatosItems):

    #Atributos
    srvCliente = {}
    propiedades = {}

    def __init__(self, propiedades):
        self.srvCliente = srvconsultasmeli.SrvConsultasMELI()
        self.propiedades = propiedades

    # Métodos
    # Recupera los datos básicos de item, de un servicio tercero: fechaInicio, precio,
    # idCategoria, idMoneda, idVendedor
    # reporta respuesta exitosa del cliente Rest.
    def recuperarDatosBasicosItem(self, idSitio, idItem):
        print("Entrando al método de BuscadorDatosItems.recuperarDatosBasicosItem....")
        objRespuestaClienteItem = {}
        urlItems = "https://api.mercadolibre.com/items/"

        # llamar el cliente del servicio la claveItem (concatenando idSitio y idItem)
        objRespuestaClienteItem = self.srvCliente.recuperarDatosAPIMELI(urlItems, idSitio+idItem)
        print("Saliendo al método de BuscadorDatosItems.recuperarDatosBasicosItem....")
        return objRespuestaClienteItem


    def recuperarDatosCategoria(self, idCategoria):
        objRespClienteCatgria = {}
        print("Entrando al método de BuscadorDatosItems.recuperarDatosCategoria....")
        urlCategorias = "https://api.mercadolibre.com/categories/"
        # llamar el cliente del servicio por medio del idCategoria
        objRespClienteCatgria = self.srvCliente.recuperarDatosAPIMELI(urlCategorias, idCategoria)
        print("Saliendo al método de BuscadorDatosItems.recuperarDatosCategoria....")
        return objRespClienteCatgria

    def recuperarDatosMoneda(self, idMoneda):
        print("Entrando al método de BuscadorDatosItems.recuperarDatosMoneda....")
        objRespClienteMoneda = {}
        urlMonedas = "https://api.mercadolibre.com/currencies/"
        # llamar el cliente del servicio por medio del idMoneda
        objRespClienteMoneda = self.srvCliente.recuperarDatosAPIMELI(urlMonedas, idMoneda)
        print("Saliendo al método de BuscadorDatosItems.recuperarDatosMoneda....")
        return objRespClienteMoneda

    def recuperarDatosUsuario(self, idUsuario):
        print("Entrando al método de BuscadorDatosItems.recuperarDatosUsuario....")
        objRespClienteUsuario = {}
        urlUsuarios = "https://api.mercadolibre.com/users/"
        # llamar el cliente del servicio por medio del idUsario
        objRespClienteUsuario = self.srvCliente.recuperarDatosAPIMELI(urlUsuarios, idUsuario)
        print("Saliendo al método de BuscadorDatosItems.recuperarDatosUsuario....")
        return objRespClienteUsuario

