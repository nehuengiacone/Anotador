# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, "./view/")
sys.path.insert(1, ".")

# IMPORTACIONES
from classes import Grilla
from widgets import widgets_definitions
from windows import windows_definitions
from controllers import controllers_definitions





# FUNCIONES DE EVENTOS PARA BUTTONS
def entrar_menu_principal():
    windows_definitions.root.cerrar_ventana()
    windows_definitions.main.crear_ventana()
    widgets_definitions.call_main()

def entrar_crear_cuenta():
    windows_definitions.crear_cuenta.crear_ventana(windows_definitions.root.get_ventana())
    widgets_definitions.crear_cuenta_call()

def cerrar_programa():
    windows_definitions.main.cerrar_ventana()

def entrar_crear_nota():
    windows_definitions.crear_nota.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.crear_nota_call()

def entrar_modificar_nota():
    windows_definitions.modificar_nota.crear_ventana(windows_definitions.main.get_ventana())
    windows_definitions.nota.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.modificar_nota_call()
    widgets_definitions.nota_call()

def entrar_buscar_nota():
    windows_definitions.buscar_nota.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.buscar_nota_call()

def guardar_nota():
    windows_definitions.modificar_nota.cerrar_ventana()
    windows_definitions.nota.cerrar_ventana()

def listar_notas():
    windows_definitions.listar_notas.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.listar_notas_call()
    

# FUNCIONES DE EVENTOS PARA GRIDS
def buscar_nota(widget:Grilla.Grid=None):
    widget.insertar_filas([["compra","30/09/2023"]])

def seleccionar(widget:Grilla.Grid=None):
    windows_definitions.nota.crear_ventana(windows_definitions.buscar_nota.get_ventana())
    widgets_definitions.nota_view_call()

# FUNCIONES DE EVENTOS PARA ENTRIES
