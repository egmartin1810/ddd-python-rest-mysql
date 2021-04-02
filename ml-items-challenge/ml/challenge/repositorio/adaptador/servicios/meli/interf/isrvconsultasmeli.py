import abc
# Interface de ISrvConsultasMELI
class ISrvConsultasMELI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def recuperarDatosAPIMELI(self, url, pathParam):
        """
        Recupera los datos del Item de un servicio Proveedor
        :param url: endpoint del servicio provedor
        :param pathParam: identificador único que hace parte de la url para el llamado al servicio
        :return: objeto respuesta de servicio proveedor
        """