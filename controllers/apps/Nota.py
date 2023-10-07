class Nota:
    __titulo:str = ''
    __cuerpo:str = ''

    def __init__(self, titulo:str, cuerpo:str):
        self.__titulo = titulo
        self.__cuerpo = cuerpo

    def get_titulo(self):
        return self.__titulo
    
    def get_cuerpo(self):
        return self.__cuerpo