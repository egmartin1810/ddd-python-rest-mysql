class BasicConfig:
    ##### ARCHIVO #####
    # RUTA DE ARCHIVO
    ARCHIVO_NOMBRE = "archivo-a-cargar/technical_challenge_data"
    ARCHIVO_FORMATO = "csv"
    ARCHIVO_SEPARADOR = ","
    ARCHIVO_ENCODING = "utf-8"

    ##### ENDPOINTS API MELI #####
    SRVBE_ITEMS = {'idServicio': "SRVBE_ITEMS", 'url': "https://api.mercadolibre.com/items/", 'nivel': 1}
    SRVBE_CATEGORIAS = {'idServicio': "SRVBE_CATEGORIAS", 'url': "https://api.mercadolibre.com/categories/", 'nivel': 2}
    SRVBE_MONEDAS = {'idServicio': "SRVBE_MONEDAS", 'url': "https://api.mercadolibre.com/currencies/", 'nivel': 2}
    SRVBE_USUARIOS = {'idServicio': "SRVBE_USUARIOS", 'url': "https://api.mercadolibre.com/users/", 'nivel': 2}

    ##### THREADPOOLEXECUTOR #####
    # Número de hilos para procesar concurrentemente
    THREADPOOLEXECUTOR_NUM_WORKERS = 50

    ##### Database #####
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://challengeml:1challengeml@db:3306/meli"
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 50, 'max_overflow': 5}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### Otras Funcionalidades #####
    BORRAR_TODOS_REGISTROS_ITEMSBD = True
