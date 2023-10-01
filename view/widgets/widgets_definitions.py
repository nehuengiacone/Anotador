# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, "./view")
sys.path.insert(1, ".")


# IMPORTACIONES
from classes import Boton, Entrada, Grilla
from tkinter import *
from PIL import Image, ImageTk
from controllers import controllers_definitions
from windows import windows_definitions
from frames import frames_definitions
from events import events_definitions










#LOGIN CALL
def call_login():
    # INSTANCIAS DE WIDGETS
    lbl_usuario = Label(windows_definitions.root.get_ventana(), text="Usuario")
    ent_usuario = Entrada.Entrada(ventana=windows_definitions.root, width=30, value="Ingrese su usuario")
    lbl_clave = Label(windows_definitions.root.get_ventana(), text="Clave")
    ent_clave = Entrada.Entrada(ventana=windows_definitions.root, width=30, value="clave", pwd=True)
    btn_ingresar = Boton.Boton(ventana=windows_definitions.root, width=40, height=2, texto="Ingresar", bgcolor="LIGHTBLUE", borde=3, tborde='raised')
    btn_crear_cuenta = Boton.Boton(ventana=windows_definitions.root, width=40, height=2, texto="Crear Cuenta", bgcolor="LIGHTBLUE", borde=3, tborde='raised')

    # CREACION DE WIDGETS
    lbl_usuario.place(x=110, y=40)
    ent_usuario.crear_entrada(110, 60)
    lbl_clave.place(x=110, y=90)
    ent_clave.crear_entrada(110, 110)
    btn_ingresar.crear_boton(55, 150)
    btn_crear_cuenta.crear_boton(55, 220)
    btn_ingresar.evento(events_definitions.entrar_menu_principal)
    btn_crear_cuenta.evento(events_definitions.entrar_crear_cuenta)

#MAIN CALL
def call_main():
    # INSTANCIAS DE WIDGETS
    
    btn_crear_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Crear Nota", bgcolor='pale green', borde=2, tborde='raised')
    btn_buscar_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Buscar Nota", bgcolor='lightblue', borde=2, tborde='raised')
    btn_listar_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Listar Nota", bgcolor='lightblue', borde=2, tborde='raised')
    btn_modificar_nota = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Modificar Nota", bgcolor='lightblue', borde=2, tborde='raised')
    btn_salir = Boton.Boton(ventana=windows_definitions.main, width=15, height=2, texto="Salir", bgcolor='light coral', borde=2, tborde='raised')

    # CREACION DE WIDGETS
    btn_crear_nota.crear_boton(20, 50)
    btn_buscar_nota.crear_boton(20, 130)
    btn_listar_nota.crear_boton(260, 50)
    # btn_modificar_nota.crear_boton(260, 130)
    btn_salir.crear_boton(260, 130)
    btn_crear_nota.evento(events_definitions.entrar_crear_nota)
    # btn_modificar_nota.evento(events_definitions.entrar_modificar_nota)
    btn_buscar_nota.evento(events_definitions.entrar_buscar_nota)
    btn_listar_nota.evento(events_definitions.listar_notas)
    btn_salir.evento(events_definitions.cerrar_programa)

#CREAR CUENTA CALL
def crear_cuenta_call():

    lbl_usuario = Label(windows_definitions.crear_cuenta.get_ventana(), text="Usuario")
    ent_usuario = Entrada.Entrada(ventana=windows_definitions.crear_cuenta, width=40, value="Usuario ...")
    lbl_clave1 = Label(windows_definitions.crear_cuenta.get_ventana(), text="Clave")
    ent_clave = Entrada.Entrada(ventana=windows_definitions.crear_cuenta, width=40, value="Clave ...", pwd=True)
    lbl_clave2 = Label(windows_definitions.crear_cuenta.get_ventana(), text="Repetir clave")
    ent_repeat_clave = Entrada.Entrada(ventana=windows_definitions.crear_cuenta, width=40, value="Clave ...", pwd=True)
    btn_crear_cuenta = Boton.Boton(ventana=windows_definitions.crear_cuenta, width=40, height=2, texto="Registrar Cuenta", bgcolor="pale green", borde=3, tborde='raised')

    lbl_usuario.place(x=80, y=30)
    ent_usuario.crear_entrada(80, 50)
    lbl_clave1.place(x=80, y=80)
    ent_clave.crear_entrada(80, 100)
    lbl_clave2.place(x=80, y=130)
    ent_repeat_clave.crear_entrada(80, 150)
    btn_crear_cuenta.crear_boton(55, 200)



#CREAR NOTA CALL
def crear_nota_call():
    # INSTANCIAS DE WIDGETS
    ent_titulo = Entrada.Entrada(ventana=windows_definitions.crear_nota, width=40, value="Titulo ...")
    btn_crear_nota = Boton.Boton(ventana=windows_definitions.crear_nota, width=30, height=2, texto="Guardar", bgcolor='lightblue', borde=2, tborde='raised')
    txt_cuerpo = Text(windows_definitions.crear_nota.get_ventana(), width=40)

    # CREACION DE WIDGETS
    ent_titulo.crear_entrada(80, 20)
    txt_cuerpo.place(x=40, y=50)
    btn_crear_nota.crear_boton(90, 500)

#BUSCAR NOTA CALL
def buscar_nota_call():
    # INSTANCIAS DE WIDGETS
    lbl_titulo = Label(windows_definitions.buscar_nota.get_ventana(), text="Titulo")
    ent_buscar = Entrada.Entrada(ventana=windows_definitions.buscar_nota, width=40, value="Buscar por Titulo ...")
    btn_buscar = Boton.Boton(ventana=windows_definitions.buscar_nota, width=30, height=2, texto="Buscar", bgcolor='lightblue', borde=2, tborde='raised')
    grid_resultados = Grilla.Grid(ventana=windows_definitions.buscar_nota, encabezados=("TITULO", "F. CREACIÓN"), width=100, align="bottom")

    # CREACION DE WIDGETS
    lbl_titulo.place(x=20 ,y=20)
    ent_buscar.crear_entrada(x=80, y=20)
    btn_buscar.crear_boton(x=190, y=50)
    grid_resultados.crear_grid()
    btn_buscar.evento(wevento=events_definitions.buscar_nota,widget=grid_resultados)
    grid_resultados.get_grid().bind("<Double-1>", lambda event:events_definitions.seleccionar(widget=grid_resultados))

#LISTAR NOTA CALL
def listar_notas_call():
    # INSTANCIAS DE WIDGETS
    lbl_titulo = Label(windows_definitions.listar_notas.get_ventana(), text="Listado de Notas")
    btn_buscar = Boton.Boton(ventana=windows_definitions.listar_notas, width=15, height=2, texto="Buscar", bgcolor='lightblue', borde=2, tborde='raised')
    btn_modificar_nota = Boton.Boton(ventana=windows_definitions.listar_notas, width=15, height=2, texto="Modificar Nota", bgcolor='lightblue', borde=2, tborde='raised')
    grid_resultados = Grilla.Grid(ventana=windows_definitions.listar_notas, encabezados=("TITULO", "F. CREACIÓN"), width=100, align="bottom")

    # CREACION DE WIDGETS
    lbl_titulo.place(x=250 ,y=20)
    btn_buscar.crear_boton(x=90, y=50)
    btn_modificar_nota.crear_boton(x=390, y=50)
    grid_resultados.crear_grid()
    btn_buscar.evento(wevento=events_definitions.buscar_nota,widget=grid_resultados)    
    btn_modificar_nota.evento(events_definitions.entrar_modificar_nota)




#MODIFICAR NOTA CALL
def modificar_nota_call():
    # INSTANCIAS DE WIDGETS
    ent_titulo = Entrada.Entrada(ventana=windows_definitions.modificar_nota, width=40, value="Titulo ...", read=True)
    btn_modificar_nota = Boton.Boton(ventana=windows_definitions.modificar_nota, width=30, height=2, texto="Guardar", bgcolor='lightblue', borde=2, tborde='raised')
    txt_cuerpo = Text(windows_definitions.modificar_nota.get_ventana(), width=40)

    # CREACION DE WIDGETS
    ent_titulo.crear_entrada(80, 20)
    txt_cuerpo.place(x=40, y=50)
    btn_modificar_nota.crear_boton(90, 500)
    btn_modificar_nota.evento(events_definitions.guardar_nota)


#NOTA CALL
def nota_call():
    # INSTANCIAS DE WIDGETS
    txt_cuerpo = Text(windows_definitions.nota.get_ventana(), width=40, height=20, state="normal")
    txt_cuerpo.insert(END, "Hola Mundo!!!!")
    txt_cuerpo.configure(state="disabled", bg="lightgrey")

    # CREACION DE WIDGETS
    txt_cuerpo.place(x=2, y=1)

#NOTA VIEW CALL
def nota_view_call():
    # INSTANCIAS DE WIDGETS
    txt_cuerpo = Text(windows_definitions.nota.get_ventana(), width=40, height=20, state="normal")
    txt_cuerpo.insert(END, "Hola Mundo!!!!")
    txt_cuerpo.configure(state="disabled", bg="lightgrey")

    # CREACION DE WIDGETS
    txt_cuerpo.place(x=2, y=1)

#PRIMERA CALL
call_login()

