# Por: Giovanni Martinez
# Fecha: 2021/03/29
# Descripción: Categoría que agrupa items
class Categoria:

    #Atributos
    __idCategoria = 0
    __nombreCategoria = ""

    # Constructor
    def __init__(self, idCategoria, nombreCategoria):
        self.__idCategoria = idCategoria
        self.__nombreCategoria = nombreCategoria

    # Getters y Setters
    def getIdCategoria(self):
        return self.__idCategoria

    def getNombreCategoria(self):
        return self.__nombreCategoria

    def setIdCategoria(self, idCategoria):
        self.__idCategoria = idCategoria

    def setNombreCategoria(self, nombreCategoria):
        self.__nombreCategoria = nombreCategoria

    def __str__(self):
        return "idCategoria: " + self.__idCategoria + ", nombreCategoria: " +self.__nombreCategoria
