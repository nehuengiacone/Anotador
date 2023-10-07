# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, "./view/")
sys.path.insert(1, ".")

# IMPORTACIONES
from classes import Grilla, Entrada
from widgets import widgets_definitions
from windows import windows_definitions
from controllers import controllers_definitions
from controllers.apps import Usuario, Nota



# VARIABLES GLOBALES
notas = {}

# FUNCIONES DE EVENTOS PARA BUTTONS
def entrar_menu_principal_validacion(evento, entradas):
    if(entradas != []):
        usuario_controller = controllers_definitions.UsuarioController()
        sesion = usuario_controller.get_usuario(entradas[0], entradas[1])
        if(sesion[1]):
            usuario = Usuario.Usuario(sesion[0][0][0], sesion[0][0][1], sesion[0][0][2])
            entrar_menu_principal(usuario)
        else:
            print("No se inicio Sesion: datos incorrectos")
    else:
        print("ERROR: DATOS VACIOS")




def entrar_menu_principal(usuario:Usuario.Usuario):
    windows_definitions.root.cerrar_ventana()
    windows_definitions.main.crear_ventana()
    widgets_definitions.call_main(usuario)





def entrar_crear_cuenta():
    windows_definitions.crear_cuenta.crear_ventana(windows_definitions.root.get_ventana())
    widgets_definitions.crear_cuenta_call()
    



def crear_cuenta_crear_usuario(evento, entradas):
    if( entradas[0] != ''):
        if (entradas[1] != '' and entradas[1] == entradas[2]):
            usuario_controller = controllers_definitions.UsuarioController()
            usuario_controller.set_usuario(entradas[0], entradas[1])
            print(entradas[0])
            print(entradas[1])
            print(entradas[2])
            windows_definitions.crear_cuenta.cerrar_ventana()
        else:
            print("datos incorrectos! las claves estan vacias o son desiguales")
            print(f"clave : '{entradas[1]}'\nclave repetida : '{entradas[2]}'")
    else:
        print("El nombre de usuario esta en blanco!")
 



def cerrar_programa():
    windows_definitions.main.cerrar_ventana()



def entrar_crear_nota(event, usuario:Usuario.Usuario):
    windows_definitions.crear_nota.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.crear_nota_call(usuario)

def crear_nota_crear_nota(event, entradas, usuario:Usuario.Usuario):
    if(entradas[0] != '' and entradas[1] != ''):
        nota_controller = controllers_definitions.NotaController()
        response = nota_controller.set_nota_nueva(entradas[0], entradas[1], usuario.get_id())
        if(response):
            print("Se registro la nota.")
            windows_definitions.crear_nota.cerrar_ventana()
        else:
            print("No se pudo registrar la nota. Hubo un problema")

def entrar_modificar_nota():
    windows_definitions.modificar_nota.crear_ventana(windows_definitions.main.get_ventana())
    windows_definitions.nota.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.modificar_nota_call()
    widgets_definitions.nota_call()




def entrar_buscar_nota(event, usuario:Usuario.Usuario):
    windows_definitions.buscar_nota.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.buscar_nota_call(usuario)




def guardar_nota():
    windows_definitions.modificar_nota.cerrar_ventana()
    windows_definitions.nota.cerrar_ventana()




def listar_notas(evento, usuario:Usuario.Usuario):
    windows_definitions.listar_notas.crear_ventana(windows_definitions.main.get_ventana())
    widgets_definitions.listar_notas_call(usuario)
    



# # FUNCIONES DE EVENTOS PARA GRIDS
def buscar_nota_por_titulo(evento, widget:Grilla.Grid, titulo:str, usuario:Usuario.Usuario):
    widget.get_grid().delete(*widget.get_grid().get_children())
    nota_controller = controllers_definitions.NotaController()
    resultado = nota_controller.get_notas_por_titulo(titulo, usuario.get_id())
    if(resultado[1]):
        for registros in resultado[0]:
            nota = Nota.Nota(registros[1], registros[2])
            id_fila = widget.insertar_fila([registros[1],registros[3]])
            notas.setdefault(id_fila, nota)
    else:
        print("No se recuperó nada")




def buscar_nota_por_titulo_seleccionar(event, seleccion:tuple, notas:dict):
    if(seleccion[0] != ()):
        if(seleccion[0][0] in notas.keys()):
            print("Existe key para nota seleccionada")
            key = seleccion[0][0]
            windows_definitions.nota.crear_ventana(windows_definitions.buscar_nota.get_ventana())
            widgets_definitions.nota_view_call(key)
        else:
            print("No existe key")
    else:
        print("No existe seleccion")



def reset_notas(grid:Grilla.Grid):
    print(notas)
    notas.clear()
    grid.get_grid().delete(*grid.get_grid().get_children())
    print(notas)
    windows_definitions.buscar_nota.cerrar_ventana()

# FUNCIONES DE EVENTOS PARA ENTRIES




