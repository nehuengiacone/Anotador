import tkinter
from tkinter import ttk
import classes.Ventana
import classes.Marcos


class Grid:
    """Clase genérica para el desarrollo de tableros de grillas."""

    __ventana_root = None
    __marco = None
    __grid = None
    __scrollbar = None
    __num_columnas = 0
    __columnas = []
    __encabezados = ()
    __width = 0
    __align = None
    __alignarr = ["top", "bottom", "left", "right"]
    __fila_seleccionada = None
    __id_fila = []

    def __init__(self, ventana:classes.Ventana.Ventana=None, marco:classes.Marcos.Marco=None, encabezados:tuple = (), width:int=100, align:str="top"):
        self.__columnas = []
        if(ventana != None):
            self.__ventana_root = ventana.get_ventana()
        else:
            self.__marco = marco.get_marco()

        if(align in self.__alignarr):
            self.__align = align

        # asigno la tupla de encabezados y la cantidad de columnas mientras esta tenga contenido.
        # si la tupla de encabezados no tiene contenido, asigna por defecto una tupla con un encabezado y asigna una columna.
        if(len(encabezados) > 0):
            self.__encabezados = encabezados
            self.__num_columnas = len(encabezados)
            print(f"columnas totales = {self.__num_columnas}")
        else:
            self.__encabezado = ("Titulo")
            self.__num_columnas = len(encabezados)
            print(f"columnas totales = {self.__num_columnas}")
        
        # Genero una tupla con el indice de las columnas del tablero (es un ayuda)
        for col in range(self.__num_columnas):
            self.__columnas.append(f"col{col+1}")
        
        self.__columnas = tuple(self.__columnas)
        self.__width = width




    def crear_grid(self):
        """Creación del objeto Grid con sus características."""

        # instancia de la clase Treeview
        if(self.__ventana_root != None):
            self.__grid = ttk.Treeview(self.__ventana_root, columns=self.__columnas)
        else:
            self.__grid = ttk.Treeview(self.__marco, columns=self.__columnas)


        # configuracion de la columa.
        # el 'for' genera tantas columnas como tenga asignado self.__column.
        # column es el identificador de la columna, anchor indica su posicion, width su ancho
        self.__grid.column("#0", width=0, stretch=tkinter.NO)
        for column in self.__columnas:
            self.__grid.column(column, anchor=tkinter.CENTER, width=self.__width)
            print(column)

        # configuracion del encabezado
        # el 'for' genera encabezados por columnas
        self.__grid.heading("#0", text="", anchor=tkinter.CENTER)
        col = 1
        for head, column in zip(self.__encabezados, self.__columnas):
            self.__grid.heading(column, text=head, anchor=tkinter.CENTER)
            col += 1
            print(f"{head} /espacio/  {column}")
        # ipadx=self.__ventana_root.get_dimension()["width"] 
        self.__grid.pack(side=self.__align, fill="x", expand=False, ipady=30)
        self.__grid.pack_configure(padx=0, pady=10)

        self.__grid.configure(selectmode="browse")
        

        
    def insertar_filas(self, filas_datos:list):
        """Permite la insercción de filas nuevas al tablero mediante una lista de datos a ingresar."""
        
        # filas_datos es una lista compuesta por listas donde cada una es una fila con sus datos por columnas.
        # values de insert acepta listas, por lo que la fila a insertar, es una lista de filas_datos.
        for fila in filas_datos:
            # print(self.__grid.insert(parent="", index="end", iid=None, values=fila))
            self.__id_fila.append(self.__grid.insert(parent="", index="end", iid=None, values=fila))

    def insertar_fila(self, fila_datos:list):
        id_fila = self.__grid.insert(parent="", index="end", iid=None, values=fila_datos)
        self.__id_fila.append(id_fila)
        
        return id_fila


    def get_grid(self):
        """Retorno del objeto Grid para futura manipulación."""
        return self.__grid
    
    
    def fila_seleccionada(self):
        """Selección de un registro en el tablero y el almacenamiento de la información impresa seleccionada."""

        # obtengo los datos de la fila seleccionada
        seleccion = self.__grid.selection()
        # print(seleccion)

        if seleccion:
            self.__fila_seleccionada = self.__grid.item(seleccion)['values']
            # print(self.__fila_seleccionada)
            return (seleccion, self.__fila_seleccionada)
        else:
            print("nada")
            return ((), None)
    


    def get_info_fila_seleccionada(self):
        """Retorno de los datos recuperados en el metodo 'fila_seleccionada'. (informativo)"""
        return self.__fila_seleccionada
    
    def get_filas_id(self):
        return self.__id_fila