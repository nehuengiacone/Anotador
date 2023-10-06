import tkinter
from tkinter import ttk
import classes.Ventana
import classes.Marcos



class Entrada:
    __entrada = None
    __ventana_root:classes.Ventana.Ventana = None
    __marco_root:classes.Marcos.Marco = None
    __width:int = None
    __readonly:bool = False
    __pwd:bool = False
    __value = None
    __value_entrada = None


    def __init__(self, ventana:classes.Ventana.Ventana=None, marco:classes.Marcos.Marco=None, width:int=None, read:bool=False, pwd:bool=False, value=None):
        
        if(ventana == None):
            self.__marco_root = marco.get_marco()
        else:
            self.__ventana_root = ventana.get_ventana()
        
        self.__width = width
        self.__readonly = read
        self.__pwd = pwd
        self.__value = value
    
    def crear_entrada(self, x:int=0, y:int=0):

        if(self.__ventana_root != None):
            self.__entrada = tkinter.Entry(self.__ventana_root)
        else:
            self.__entrada = tkinter.Entry(self.__marco_root)

        if(self.__width != None):
            self.__entrada.configure(width=self.__width)

        if(self.__readonly == True):
            self.__entrada.configure(state="readonly")
        
        if(self.__pwd == True):
            self.__entrada.configure(show='*')
        
        if(self.__value != None):
            self.__value_entrada = tkinter.StringVar()
            self.__value_entrada.set(self.__value)
            self.__entrada.configure(textvariable=self.__value_entrada)

        # self.__entrada.pack(padx=x, pady=y, ipadx=5, ipady=5)
        self.__entrada.place(x=x, y=y)
        # print(self.__entrada.get()) 

    def get_entrada(self):
        return self.__entrada
    
    def get_valor(self):
        return self.__entrada.get()
    
    def set_valor(self):
        self.__value_entrada.set()
