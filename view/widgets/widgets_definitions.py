# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, "./view")
sys.path.insert(1, ".")


# IMPORTACIONES
# from classes import Boton
from classes import Boton, Entrada
from tkinter import Label
from controllers import controllers_definitions
from windows import windows_definitions
from frames import frames_definitions
from events import events_definitions







#LOGIN CALL
def call_login():
    # INSTANCIAS DE WIDGEDTS
    lbl_correo = Label(windows_definitions.root.get_ventana(), text="Email")
    ent_correo = Entrada.Entrada(ventana=windows_definitions.root, width=30, value="Ingrese su correo")
    lbl_clave = Label(windows_definitions.root.get_ventana(), text="Clave")
    ent_clave = Entrada.Entrada(ventana=windows_definitions.root, width=30, value="clave", pwd=True)
    btn_ingresar = Boton.Boton(ventana=windows_definitions.root, width=40, height=2, texto="Ingresar", bgcolor="LIGHTBLUE", borde=3, tborde='raised')

    # CREACION DE WIDGETS
    lbl_correo.place(x=110, y=80)
    ent_correo.crear_entrada(110, 100)
    lbl_clave.place(x=110, y=130)
    ent_clave.crear_entrada(110, 150)
    btn_ingresar.crear_boton(55, 220)
    btn_ingresar.evento_nueva_ventana(events_definitions.entrar_menu_principal)


#MAIN CALL
def call_main():
    # INSTANCIAS DE WIDGEDTS
    btn_crear_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Crear Nota", bgcolor='lightblue', borde=2, tborde='raised')
    btn_buscar_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Buscar Nota", bgcolor='lightblue', borde=2, tborde='raised')
    btn_listar_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Listar Nota", bgcolor='lightblue', borde=2, tborde='raised')
    btn_modificar_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Modificar Nota", bgcolor='lightblue', borde=2, tborde='raised')

    # CREACION DE WIDGETS
    btn_crear_nota.crear_boton(20, 50)
    btn_buscar_nota.crear_boton(20, 130)
    btn_listar_nota.crear_boton(260, 50)
    btn_modificar_nota.crear_boton(260, 130)



#PRIMERA CALL
call_login()

