import srvconsultasmeli as srv

def main():
    print('Iniciado prueba llamado servicios REST')
    url= "https://api.mercadolibre.com/items/"
    urlCat = "https://api.mercadolibre.com/categories/"
    id = "MLA782750723"
    idCat = "MLA4283"

    urlCurrency = "https://api.mercadolibre.com/currencies/"
    idMoneda = "ARS"

    urlUsr = "https://api.mercadolibre.com/users/"
    idUsuario = "63443205"

    req = srv.SrvConsultasMELI()
    res = req.recuperarDatosAPIMELI(urlCurrency, idMoneda)
    print("Respuesta: ", res)
    print('Finalizando prueba llamado servicios REST', res['id'])

if __name__ == '__main__':
    main()