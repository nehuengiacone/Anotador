from tkinter import *
import classes.Ventana

class MenuBar:
    """Clase generica que sirve de base para las barras de ventanas del sistema"""

    __ventana = None
    __menu = None
    __menuDropdown = None

    def __init__(self, ventana:classes.Ventana.Ventana, titulo:str=""):
        self.__ventana = ventana.get_ventana()
        self.__titulo = titulo
    
    def crear_menu(self):
        """Creación de barra de menu"""

        frame_menu = LabelFrame(self.__ventana, bd=1, padx=5, pady=5)
        frame_menu.pack(fill="both", expand=True)
        self._menu = Menu(frame_menu)
        self.__ventana.config(menu=self.__menu)

        return self.__menu
    
    def crear_dropdown(self):
        """Creación de desplegable"""
        
        self.__menuDropdown = Menu(self.__menu, tearoff=0)
        return self.__menuDropdown
    
