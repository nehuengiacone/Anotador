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
        try:
            cursor = self.__connex.get_connection().cursor()
            query = f"insert into usuarios(nombre, clave) values(%s, %s)"
            query_data = (nombre, clave)
            cursor.execute(query, query_data)
            self.__connex.get_connection().commit()
            cursor.close()
            self.__connex.close_connection()

            return True
        except:
            return False
        
    def buscar_usuario(self, nombre, clave):
        cursor = self.__connex.get_connection().cursor()
        query = "select * from usuarios where nombre=%s and clave=%s"
        query_data = (nombre, clave)
        cursor.execute(query, query_data)
        resultado = cursor.fetchall()
        cursor.close()
        self.__connex.close_connection()

        return resultado
    
    def buscar_nombre_usuario(self, nombre):
        cursor = self.__connex.get_connection().cursor()
        query = "select nombre from usuarios where nombre=%s"
        query_data = tuple([nombre])
        cursor.execute(query, query_data)
        resultado = cursor.fetchall()
        cursor.close()

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
        
    def actualizar_nota(self, id_nota:int, titulo:str, cuerpo:str, idusuario:int):
        print(f"{id_nota} {idusuario}")
        cursor = self.__connex.get_connection().cursor()
        query_insert = "insert into nota(titulo, cuerpo, fecha_audit, idusuario, habilitado) values(%s, %s, %s, %s, %s)"
        query_update = "update nota set habilitado=0 where idnota=%s and idusuario=%s"
        query_data_insert = (titulo, cuerpo, datetime.date.today(), idusuario, 1)
        query_data_update = (id_nota, idusuario)

        try:
            cursor.execute(query_insert, query_data_insert)
            self.__connex.get_connection().commit()
            print("confirmo el insert")

            try:
                cursor.execute(query_update, query_data_update)
                self.__connex.get_connection().commit()
                print("confirmo el update")
                cursor.close()
                self.__connex.close_connection()
                return True
            except:
                cursor.close()
                self.__connex.close_connection()
                return False
        except:
            cursor.close()
            self.__connex.close_connection()
            return False
        

    def get_notas_por_titulo(self, titulo:str, idusuario:int):
        titulo = f"%{titulo}%"
        cursor = self.__connex.get_connection().cursor()
        query = "select * from nota where titulo like %s and idusuario=%s and habilitado=1"
        query_data = (titulo, idusuario)
        try:
            cursor.execute(query, query_data)
            resultado = cursor.fetchall()
            cursor.close()
            self.__connex.close_connection()

            return (resultado, True)
        except:
            return (resultado, False)
        
    def get_notas_todas(self, idusuario:int):
        cursor = self.__connex.get_connection().cursor()
        query = "select * from nota where idusuario=%s and habilitado=1"
        query_data = tuple([idusuario])
        try:
            cursor.execute(query, query_data)
            resultado = cursor.fetchall()
            cursor.close()
            self.__connex.close_connection()

            return (resultado, True)
        except:
            return (resultado, False)