# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Clase que implementa la inteface del servicio proveedor de MELI.
import abc
import requests
from ml.challenge.repositorio.adaptador.servicios.meli.interf.isrvconsultasmeli import ISrvConsultasMELI
import ml.challenge.repositorio.adaptador.servicios.meli.excepciones.respuestahttpexception as respuestahttpexception
from main import app
class SrvConsultasMELI(ISrvConsultasMELI):

    # Métodos
    # Llama a servicio Restful de MELI
    def recuperarDatosAPIMELI(self, dictServAllamar):
        objServicioRes = {}
        idServicio = dictServAllamar.getSrv().get('srv')
        print(f'Entrando método SrvConsultasMELI.recuperarDatosItem() - Servicio a llamar: {idServicio} ...')

        # Completar la url con el pathparam enviado por parametro.
        servicio = app.config[idServicio]
        servURL = servicio['url']
        pathParam = dictServAllamar.getParametro().get('parametro')
        print(" SrvConsultasMELI Paerametro: ", pathParam)
        urlCompleta = servURL+str(pathParam)
        # llamar al metodo get de la API.
        ojbServicioRq = requests.get(urlCompleta)
        # Validar el estado de la respuesta
        if ojbServicioRq.status_code == 200:
            objServicioRes = ojbServicioRq.json()
        else:
            print(f'Error llamando Servicio: {ojbServicioRq} ,url={servURL}  ')
            if (ojbServicioRq.status_code == 404):
                raise respuestahttpexception.RecursoNoEncontradoException(ojbServicioRq.status_code,
                                                                "Error al llamar al servicio solicitado: "
                                                                +str(ojbServicioRq.status_code))
            else:
                raise respuestahttpexception.RespuestaHTTPException(ojbServicioRq.status_code,
                                                                "Error al llamar al servicio solicitado: "
                                                                +str(ojbServicioRq.status_code))

        print(f'Saliendo método SrvConsultasMELI.recuperarDatosItem(), url={servURL} ...')
        return objServicioRes