# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, ".")

# IMPORTACIONES
from connections import DataWire
from controllers.apps import Usuario
import datetime

# CLASES REPOSITORIOS
class UsuarioRepositorio:
    # __nombre:str = ''
    # __clave:str = ''
    __connex:DataWire.DataWire = None

    def __init__(self):
        self.__connex = DataWire.DataWire()
        self.__connex.connection_start(True)
        
    def guardar_usuario(self, nombre, clave):

        cursor = self.__connex.get_connection().cursor()
        query = f"insert into usuarios(nombre, clave) values(%s, %s)"
        query_data = (nombre, clave)
        cursor.execute(query, query_data)
        self.__connex.get_connection().commit()
        cursor.close()
        self.__connex.close_connection()
    
    def buscar_usuario(self, nombre, clave):
        cursor = self.__connex.get_connection().cursor()
        query = "select * from usuarios where nombre=%s and clave=%s"
        query_data = (nombre, clave)
        cursor.execute(query, query_data)
        resultado = cursor.fetchall()
        cursor.close()
        self.__connex.close_connection()

        return resultado


class notaRepositorio:
    __connex:DataWire.DataWire = None

    def __init__(self):
        self.__connex = DataWire.DataWire()
        self.__connex.connection_start(True)

    def guardar_nota(self, titulo:str, cuerpo:str, idusuario:int):
        cursor = self.__connex.get_connection().cursor()
        query = "insert into nota(titulo, cuerpo, fecha_audit, idusuario, habilitado) values(%s, %s, %s, %s, %s)"
        query_data = (titulo, cuerpo, datetime.date.today(), idusuario, 1)
        try:
            cursor.execute(query, query_data)
            self.__connex.get_connection().commit()
            cursor.close()
            self.__connex.close_connection()

            return True
        except:
            return False


# nr = notaRepositorio()

# usuario = Usuario.Usuario(1, "NEHUEN", "1234")

# nr.guardar_nota("Prueba", "Soy una bendita nota de prueba. ¡LA PRIMERA!", usuario)
