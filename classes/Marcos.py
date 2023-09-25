from tkinter import *
import classes.Ventana

class Marco:
    """Clase generica que sirve de base para el desarrollo de Frames"""    

    __marco = None
    __ventana:classes.Ventana.Ventana = None
    __backgrund_color = None
    __width = None
    __height = None
    __marginx = None
    __marginy = None
    __align = None
    __tipos_bordes = ["raised", "groove", "sunken", "ridge", "flat"]
    __alignarr = ["top", "left", "bottom", "right"]
    __tipo_borde = None
    __borde = None

    def __init__(self, ventana:classes.Ventana.Ventana = None, marco = None, width:int = 0, height:int = 0, background_color:str = None, borde:int = 0, tipo_borde:str = "groove", marginx:int=0, marginy:int=0, align:str="top"):

        self.__width = width
        self.__height = height
        self.__marginx = marginx
        self.__marginy = marginy
        self.__align = align
        self.__tipo_borde = tipo_borde
        self.__borde = borde
        self.__backgrund_color = background_color
        
        if(ventana != None):
            self.__ventana = ventana.get_ventana()
        if(marco != None):
            self.__marco = marco.get_marco()


    def crear_marco(self):
        """Creción del Frame"""

        if(self.__ventana == None):
            self.__marco = Frame(self.__marco)
        else:
            self.__marco = Frame(self.__ventana)
        
        if self.__tipo_borde in self.__tipos_bordes:
            self.__marco.config(relief=self.__tipo_borde)

        self.__marco.config(width=self.__width, height=self.__height, bd=self.__borde, bg=self.__backgrund_color)
        
        if(self.__align in self.__alignarr):
            self.__marco.pack(padx=self.__marginx, pady=self.__marginy, side=self.__align, fill="both", expand=True)


    def get_marco(self):
        """Retorna el objeto Frame de la instancia para su manipulación en otras operaciones"""
    
        return self.__marco
    