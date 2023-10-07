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
from tkinter import messagebox


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
            messagebox.showinfo(message=f"BIENVENIDO {usuario.get_nombre()}", title=f"usuario: {usuario.get_nombre()} - id: {usuario.get_id()}")
        else:
            messagebox.showwarning(message="Datos Incorrectos\nUsuario o claves incorrectos", title="No se inició sesión")
            print("No se inicio Sesion: datos incorrectos")
    else:
        messagebox.showerror(message="No puede ingresar con datos vacios", title="No se inició sesión")
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
            resultado = usuario_controller.set_usuario(entradas[0], entradas[1])
            # print(entradas[0])
            # print(entradas[1])
            # print(entradas[2])
            if(resultado):
                messagebox.showinfo(message="Usuario registrado", title="Registro de nuevo Usuario")
                windows_definitions.crear_cuenta.cerrar_ventana()
            else:
                messagebox.showerror(message=f"El usuario '{entradas[0]}' ya se encuentra en uso.\nPor favor, elija otro nombre de usuario.", title="Registro de nuevo Usuario")
        else:
            messagebox.showerror(message=f"Las claves estan vacias o no son iguales\nclave : '{entradas[1]}'\nclave repetida : '{entradas[2]}'", title="Datos incorrectos")
            # print("datos incorrectos! las claves estan vacias o son desiguales")
            # print(f"clave : '{entradas[1]}'\nclave repetida : '{entradas[2]}'")
    else:
        messagebox.showerror(message="El nombre de usuario esta vacio", title="Datos incorrectos")
        # print("El nombre de usuario esta en blanco!")
 



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
            messagebox.showinfo(message="Se registró la Nota", title="Creación de Nota")
            # print("Se registro la nota.")
            windows_definitions.crear_nota.cerrar_ventana()
        else:
            messagebox.showerror(message="Ocurrió un problema.\nNo se pudo registrar la Nota.", title="Creación de Nota")
            # print("No se pudo registrar la nota. Hubo un problema")
    else:
        messagebox.showerror(message=f"Hay campos vacios\n'{entradas[0]}'\n'{entradas[1]}'", title="Creación de Nota")





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

def nota_view_maximiza(evento):
    print("pase por el evento")
    windows_definitions.nota.set_cambio_dimension()
    



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
        messagebox.showerror(message="No se recuperó nada.\nFalló la busqueda.", title="Busqueda por título")
        # print("No se recuperó nada")




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




def listar_notas_listar(evento, widget:Grilla.Grid, usuario:Usuario.Usuario):
    widget.get_grid().delete(*widget.get_grid().get_children())
    nota_controller = controllers_definitions.NotaController()
    resultado = nota_controller.get_notas_todas(usuario.get_id())
    print(resultado)
    if(resultado[1]):
        for registros in resultado[0]:
            nota = Nota.Nota(registros[1], registros[2])
            id_fila = widget.insertar_fila([registros[1],registros[3]])
            notas.setdefault(id_fila, nota)
    else:
        messagebox.showerror(message="No se recuperó nada.\nFalló la busqueda.", title="Busqueda por título")
        # print("No se recuperó nada")




def listar_notas_listar_seleccionar(event, seleccion:tuple, notas:dict):
    if(seleccion[0] != ()):
        if(seleccion[0][0] in notas.keys()):
            print("Existe key para nota seleccionada")
            key = seleccion[0][0]
            windows_definitions.nota.crear_ventana(windows_definitions.listar_notas.get_ventana())
            widgets_definitions.nota_view_call(key)
        else:
            print("No existe key")
    else:
        print("No existe seleccion")





def buscar_nota_reset_notas(grid:Grilla.Grid):
    print(notas)
    notas.clear()
    grid.get_grid().delete(*grid.get_grid().get_children())
    print(notas)
    windows_definitions.buscar_nota.cerrar_ventana()


def listar_notas_reset_notas(grid:Grilla.Grid):
    print(notas)
    notas.clear()
    grid.get_grid().delete(*grid.get_grid().get_children())
    print(notas)
    windows_definitions.listar_notas.cerrar_ventana()
# FUNCIONES DE EVENTOS PARA ENTRIES




