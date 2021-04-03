import abc
from ml.challenge.dominio.interf.ibuscadordatosItems import IBuscadorDatosItems
import ml.challenge.repositorio.adaptador.servicios.meli.srvconsultasmeli as srvconsultasmeli

# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que implementa la inteface de Buscador Items.
class BuscadorDatosItems(IBuscadorDatosItems):

    #Atributos
    srvCliente = {}

    def __init__(self):
        self.srvCliente = srvconsultasmeli.SrvConsultasMELI()

    # Métodos
    # Recupera los datos básicos de item, de un servicio tercero: fechaInicio, precio,
    # idCategoria, idMoneda, idVendedor
    # reporta respuesta exitosa del cliente Rest.
    def recuperarDatosBasicosItem(self, dictServAllamar):
        print("Entrando al método de BuscadorDatosItems.recuperarDatosBasicosItem....")
        objRespuestaClienteItem = {}
        # llamar el cliente del servicio la claveItem (concatenando idSitio y idItem)
        objRespuestaClienteItem = self.srvCliente.recuperarDatosAPIMELI(dictServAllamar)
        print("Saliendo al método de BuscadorDatosItems.recuperarDatosBasicosItem....")
        return objRespuestaClienteItem

    def recuperarDatosEntidades2Nivel(self, dictServAllamar):
        print("Entrando al método de BuscadorDatosItems.recuperarDatosGenerico....")
        objRespCliente = self.srvCliente.recuperarDatosAPIMELI(dictServAllamar)
        print("Saliendo del método de BuscadorDatosItems.recuperarDatosGenerico....")
        # Adicionamos el identificador de la petición para correlacionar.
        objRespCliente['srv'] = dictServAllamar['srv']
        return objRespCliente


