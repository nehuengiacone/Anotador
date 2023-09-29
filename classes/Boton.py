import tkinter
import math
import classes.Ventana
import classes.Marcos

class Boton:

    __boton = None
    __ventana_root:classes.Ventana.Ventana = None
    __marco_root:classes.Marcos.Marco = None
    __texto:str = 'Boton'
    __width:int = 0
    __height:int = 0
    # __estado:str = 'active'           esta ROTO!
    __background_color:str = None
    __borde:int = None
    __tborde:str = None
    __tipo_borde = ["raised", "groove", "sunken", "ridge", "flat"]


    def __init__(self, ventana:classes.Ventana.Ventana=None, marco:classes.Marcos.Marco=None, texto:str='', width:int=0, height:int=0, estado:bool=True, bgcolor:str=None, borde:int=0, tborde:str=''): 
        
        if(ventana == None):
            self.__marco_root = marco
        else:
            self.__ventana_root = ventana
        
        if(texto != ''):
            self.__texto = texto
        
        if(width != 0 and height != 0):
            self.__width = width
            self.__height = height
        
        
        if(estado == False):
            self.__estado = "disabled"
        
        self.__background_color = bgcolor
        self.__borde = borde

        if(tborde in self.__tipo_borde):
            self.__tborde = tborde
        else:
            self.__tborde = 'groove'
        


    def crear_boton(self, x:int=0, y:int=0):
        
        if(self.__ventana_root != None):
            self.__boton = tkinter.Button(self.__ventana_root.get_ventana(), text=self.__texto, width=self.__width, height=self.__height)
        else:
            self.__boton = tkinter.Button(self.__marco_root.get_marco(), text=self.__texto, width=self.__width, height=self.__height)

        self.__boton.configure(background=self.__background_color, borderwidth=self.__borde, relief=self.__tborde)

        self.__boton.place(x=x, y=y)


    def __centrar_objeto(self):
        """Centra el boton en la ventana. Regresa las coordenadas (x, y) para centralizar"""

        dimensiones_ventana = self.__ventana_root.get_dimension()
        print(dimensiones_ventana)
        coord_x = math.floor( (dimensiones_ventana['width'] - self.__width) / 4)
        coord_y = math.floor( (dimensiones_ventana['height'] + self.__height) / 8)

        return {"x": coord_x, "y": coord_y}


    def evento_nueva_ventana(self, evento):
        self.__boton.config(command=evento)
