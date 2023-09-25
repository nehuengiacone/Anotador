import mysql.connector 
from connections import info

class DataWire:
    __connection = None
    __session_start:bool = False
    
    # Si session_start es enviado, y es True, inicia una conexion
    def __init__(self, session_start:bool=False):

        if(session_start == True):
            self.connection_start(session_start)

    # regreso la instancia de la conexion
    def get_connection(self):
        """Regresa la instancia de la conexion"""
        return self.__connection
    
    # regreso el estado de la sesion
    def get_session(self) -> bool:
        """Regresa el estado de la conexion"""
        return self.__session_start
    
    # cierro la conexion
    def close_connection(self) -> bool:
        """Cierra la conexion a la base de datos"""
        self.__session_start = False
        self.__connection.close()
        return True

    # inicio la conexion
    def connection_start(self, session_start:bool) -> bool:
        """Abre la conexion a la base de datos"""
        self.__session_start = session_start

        try:
            self.__connection = mysql.connector.connect(
                user = info.root,
                passwd = info.pwd,
                host = info.host,
                database = info.database,
                auth_plugin = info.auth_plugin 
            )

            return True
        
        except mysql.connector.errors as err:
            print(f"Hubo un problema en la conexion\n{err}")
        
        return False

    def create_cursor(self):
        return self.__connection.cursor()