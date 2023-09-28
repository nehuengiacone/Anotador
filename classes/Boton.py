import tkinter
import Ventana
import Marcos

class Boton:

    __boton = None
    __ventana_root:Ventana.Ventana = None
    __marco_root:Marcos.Marco = None
    __texto:str = 'Boton'
    __width:int = 0
    __height:int = 0
    __estado:str = 'active'
    __background_color:str = None
    __foreground_color:str = None
    __activefg_color:str = None
    __activebg_color:str = None
    # __disablefg_color:str = None      a desarrollar
    # __disablebg_color:str = None      a desarrollar
    # __activefg:bool = False           a desarrollar
    # __activebg:bool = False           a desarrollar
    __borde:int = None
    __tborde:str = None
    __tipo_borde = ["raised", "groove", "sunken", "ridge", "flat"]
    # __cursor:str []                   a desarrollar


    def __init__(self, ventana:Ventana.Ventana=None, marco:Marcos.Marco=None, texto:str='', width:int=0, height:int=0, estado:bool=True, bgcolor:str=None, fgcolor:str=None, borde:int=0, tborde:str=''): 
        
        if(ventana == None):
            self.__marco_root = marco.get_marco()
        else:
            self.__ventana_root = ventana.get_ventana()
        
        if(texto != ''):
            self.__texto = texto
        
        if(width != 0 and height != 0):
            self.__width = width
            self.__height = height
        
        
        if(estado == False):
            self.__estado = "disabled"
        
        self.__background_color = bgcolor
        self.__foreground_color = fgcolor
        self.__borde = borde

        if(tborde in self.__tipo_borde):
            self.__tborde = tborde
        else:
            self.__tborde = 'raised'
        


    def crear_boton(self, x:int=0, y:int=0):
        
        if(self.__ventana_root != None):
            self.__boton = tkinter.Button(self.__ventana_root, text=self.__texto, width=self.__width, height=self.__height, state=self.__estado)
        else:
            self.__boton = tkinter.Button(self.__marco_root, text=self.__texto, width=self.__width, height=self.__height, state=self.__estado)

        self.__boton.config(bg=self.__background_color, fg=self.__foreground_color, borderwidth=self.__borde, relief=self.__tborde)

        self.__boton.place(x=x, y=y)


    def evento(self, evento):
        self.__boton.config(command=evento)