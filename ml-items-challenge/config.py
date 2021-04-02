class BasicConfig:

    ##### ARCHIVO #####
    # RUTA DE ARCHIVO
    ARCHIVO_NOMBRE= "archivo-a-cargar/technical_challenge_data"
    ARCHIVO_FORMATO = "csv"
    ARCHIVO_SEPARADOR = ","
    ARCHIVO_ENCODING = "utf-8"

    ##### ENDPOINTS API MELI #####
    MELI_URL_ITEMS = "https://api.mercadolibre.com/items/"
    MELI_URL_CATEGORIAS = "https://api.mercadolibre.com/categories/"
    MELI_URL_MONEDAS = "https://api.mercadolibre.com/currencies/"
    MELI_URL_USUARIOS = "https://api.mercadolibre.com/users/"

    ##### THREADPOOLEXECUTOR #####
    #Número de hilos para procesar concurrentemente
    THREADPOOLEXECUTOR_NUM_WORKERS = 60

    ##### Database #####
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://challengeml:1challengeml@db:3306/meli"
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 60,'max_overflow': 5}
    SQLALCHEMY_TRACK_MODIFICATIONS = False