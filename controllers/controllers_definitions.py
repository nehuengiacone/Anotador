# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, ".")

# IMPORTACIONES
from models import repositories_definitions
from controllers.apps import Nota


# DEFINICION DE CLASES CONTROLADORAS   

class ConexionController:
    __conn = None

    def __init__(self):
        self.__conn = repositories_definitions.DataWire.DataWire()
    

    def iniciarConexion(self):
        return self.__conn.connection_start(True)

    def cerrarConexion(self):
        return self.__conn.close_connection()

    def get_conexion(self):
        return self.__conn.get_connection()



# print(conexion.iniciarConexion())
# print(conexion.cerrarConexion())

class UsuarioController:
    __nombre:str = ''
    __clave:str = ''
    __usuario_repositorio = None

    def __init__(self):
        self.__usuario_repositorio = repositories_definitions.UsuarioRepositorio()

    def set_usuario(self, nombre:str, clave:str):
        self.__nombre = nombre
        self.__clave = clave
        self.__usuario_repositorio.guardar_usuario(self.__nombre, self.__clave)
    

    def get_usuario(self, nombre, clave):
        respuesta = self.__usuario_repositorio.buscar_usuario(nombre, clave)

        if((respuesta != []) and (respuesta[0][1] == nombre) and (respuesta[0][2] == clave)):
            return (respuesta, True)
        
        return (respuesta, False)
    

class NotaController:
    __titulo:str = ''
    __cuerpo:str = ''
    __fecha_crea:str = ''
    __nota_repositorio = None

    def __init__(self):
        self.__nota_repositorio = repositories_definitions.notaRepositorio()

    def set_nota_nueva(self, titulo:str, cuerpo:str, idusuario:int):
        return self.__nota_repositorio.guardar_nota(titulo, cuerpo, idusuario)

    def get_notas_por_titulo(self, titulo:str, idusuario:int):
        return self.__nota_repositorio.get_notas_por_titulo(titulo, idusuario)
        

# nc = NotaController()

# print(nc.get_notas_por_titulo("prue", 1))