import procesadoritemsimpl as procesadoritemsimpl

def main():
    print('Iniciado prueba')
    nombreArchivo= "C:/Users/Edwin_Martinez/Documents/mis-meli-src/technical_challenge_data1"
    formato = "csv"
    separador = ","
    encoding = "utf-8"
    #proc_ = procesadorarchivoimpl.ProcesadorArchivoImpl()
    #proc_.cargarArchivoStreameable(nombreArchivo, formato, separador, encoding)

    procitem_ = procesadoritemsimpl.ProcesadorItemsImpl()
    #procitem_.procesarItems("MLA","782750723")
    procitem_.procesarItems("MLA","693105237")
    #procitem_.procesarItems("MLA", "750925229")

if __name__ == '__main__':
    main()