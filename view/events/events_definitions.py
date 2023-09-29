# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, "./view/")
sys.path.insert(1, ".")

# IMPORTACIONES
from classes import Grid
from widgets import widgets_definitions
from windows import windows_definitions
from controllers import controllers_definitions





# FUNCIONES DE EVENTOS PARA BUTTONS
def entrar_menu_principal():
    windows_definitions.root.cerrar_ventana()
    windows_definitions.main.crear_ventana()
    widgets_definitions.call_main()

# FUNCIONES DE EVENTOS PARA GRIDS


# FUNCIONES DE EVENTOS PARA ENTRIES
