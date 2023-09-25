from tkinter import *
import math

class Ventana:
    """Clase generica que sirve de base para las ventanas de operaciones del sistema"""

    __width = None
    __height = None
    __titulo = None
    __completa = None
    __ventana = None
    __root = None
    __background_color = None
    __icono = None
    __resiz_x = False
    __resiz_y = False
    __maximiza = False

    def __init__(self, width:int=0, height:int=0, titulo:str='', completa:bool=False, root:bool=True, background_color:str=None, icono:str='', rx:bool=False, ry:bool=False, maximiza:bool=True):
        self.__width = width
        self.__height = height
        self.__titulo = titulo
        self.__completa = completa
        self.__root = root
        self.__background_color = background_color
        self.__icono = icono
        self.__resiz_x = rx
        self.__resiz_y = ry
        self.__maximiza = maximiza


    def crear_ventana(self, root=None):
        """Creacion y ejecucion de la ventana. Retornara True si la operacion se concreto"""

        if(not self.__root):
            self.__ventana = Toplevel(root)

            # Se posa sobre la ventana principal
            self.__ventana.transient(root)
            self.__ventana.focus_force()
        else:
            self.__ventana = Tk()
        
        self.__ventana.title(self.__titulo)

        # # Asigno el icono a la ventana
        if(self.__icono.find(".ico") != (-1)):
            self.__ventana.iconbitmap(self.__icono)

        # Configuración del redimensionamiento
        if(self.__resiz_y == False and self.__resiz_x == False):
            self.__ventana.resizable(False, False)
        elif(self.__resiz_y == False and self.__resiz_x == True):
            self.__ventana.resizable(True, False)
        elif(self.__resiz_y == True and self.__resiz_x == False):
            self.__ventana.resizable(False, True)
        else:
            self.__ventana.resizable(True, True)


        # Seteo de tamaño minimo de minimizacion.
        self.__ventana.minsize(width=self.__width, height=self.__height)

        if(self.__maximiza):
            self.__ventana.state('zoomed')

        # Si el atributo para el tamaño de la ventana es True se creara una ventana FULLSCREEN
        # Sino se creara una ventana posicionandola en el centro de la pantalla
        if(self.__completa):
            self.__ventana.geometry(f"{self.__ventana.winfo_screenwidth()}x{self.__ventana.winfo_screenheight()}+0+0")
            self.__width = self.__ventana.winfo_screenwidth()
            self.__height = self.__ventana.winfo_screenheight()
            self.__ventana.overrideredirect(True)
            # self.__ventana.state('normal')
            # self.__ventana.attributes('-fullscreen', True)
            # self.__ventana.update_idletasks()

        else:
            coords = self.__centrar_objeto()
            self.__ventana.geometry(f"{self.__width}x{self.__height}+{coords['x']}+{coords['y']}")

        # Si el atributo del color es diferente a None, setea el color enviado en la instancia.
        if(self.__background_color != None):
            self.__ventana.config(bg=self.__background_color)

        return True

    
    def crear_ventana_secundaria(self, root):
        """Creacion de una ventana secundaria
        OBSOLETO: Se realiza la operacion desde el metodo 'crear_ventana'
        """

        self.__ventana = Toplevel(root)
        self.__ventana.title(self.__titulo)

        # Asigno el icono a la ventana
        if(self.__icono.find(".ico") != (-1)):
            self.__ventana.iconbitmap(self.__icono)

        # Se posa sobre la ventana principal
        self.__ventana.transient(root)
        self.__ventana.grab_set()
        self.__ventana.focus_force()

        if(self.__completa):
            # self._ventana.attributes("-fullscreen", True)
            self.__ventana.resizable(False, False)
            self.__ventana.geometry(f"{self.__ventana.winfo_screenwidth()}x{self.__ventana.winfo_screenheight()}")
        else:
            coords = self.__centrar_objeto()
            self.__ventana.resizable(False, False)
            self.__ventana.geometry(f"{self.__width}x{self.__height}+{coords['x']}+{coords['y']}")

        return True
    

    def correr_ventana(self):
        """Ejecuta la ventana"""
        self.__ventana.mainloop()


    def __centrar_objeto(self):
        """Centra la ventana en la pantalla. Regresa las coordenadas (x, y) para centralizar"""

        width_pantalla = self.__ventana.winfo_screenwidth()
        height_pantalla = self.__ventana.winfo_screenmmheight()

        coord_x = math.floor( (width_pantalla - self.__width) / 2)
        coord_y = math.floor( (height_pantalla + self.__height) / 8)

        return {"x": coord_x, "y": coord_y}


    def cerrar_ventana(self, evento=0):
        """Destruye la ventana"""
        self.__ventana.destroy()


    def get_ventana(self):
        """Regresa la ventana creada para futuras manipulaciones"""
        return self.__ventana
    
    
    def get_dimension(self):
        """Regresa el alto y ancho de la ventana"""
        return {"height": self.__height, "width": self.__width}
    

    def get_es_completa(self)->bool: 
        """Regresa si la ventana esta configurada como FULLSCREEN"""
        return self.__completa
    

    def set_titulo(self, titulo_nuevo):
        self.__ventana.title('')
        self.__ventana.update()
        self.__ventana.title(f"{self.__titulo} - {titulo_nuevo}")
        self.__ventana.update()


    def set_cambio_dimension(self, evento=0):
        """Cambiar tamaños de la pantalla por combo de teclas."""

        # Si la pantalla esta seteada en Completa, se minimiza la pantalla con las dimensiones originales, con la ventana centrada.
        # Sino, la ventana se setea en Completa, y las dimensiones son las de la pantalla.
        if(self.__completa == True):
            self.__completa = False
            coords = self.__centrar_objeto()
            self.__ventana.geometry(f"{self.__width}x{self.__height}+{coords['x']}+{coords['y']}")
            self.__ventana.overrideredirect(False)
        else:
            self.__completa = True
            self.__ventana.geometry(f"{self.__ventana.winfo_screenwidth()}x{self.__ventana.winfo_screenheight()}+0+0")
            self.__ventana.overrideredirect(True)
