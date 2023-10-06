class Usuario:
    __id:int = 0
    __nombre:str = ''
    __clave:str = ''

    def __init__(self, id, nombre, clave):
        self.__id = id
        self.__nombre = nombre
        self.__clave = clave
    
    def get_nombre(self):
        return self.__nombre
    
    def get_id(self):
        return self.__id
    
