class Nota:
    __id_nota = int = 0
    __titulo:str = ''
    __cuerpo:str = ''

    def __init__(self, id:int, titulo:str, cuerpo:str):
        self.__id_nota = id
        self.__titulo = titulo
        self.__cuerpo = cuerpo

    def get_id(self):
        return self.__id_nota

    def get_titulo(self):
        return self.__titulo
    
    def get_cuerpo(self):
        return self.__cuerpo