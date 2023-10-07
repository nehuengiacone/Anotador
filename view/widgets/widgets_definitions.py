# RUTEO DE DIRECTORIOS
import sys
sys.path.insert(0, "./view")
# sys.path.insert(0, ".")


# IMPORTACIONES
from classes import Boton, Entrada, Grilla
from tkinter import *
from PIL import Image, ImageTk
from controllers import controllers_definitions
from controllers.apps import Usuario, Nota 
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
    # btn_ingresar.evento(events_definitions.entrar_menu_principal)

    # LLAMADA A EVENTOS
    btn_ingresar.get_boton().bind("<Button-1>", lambda event:events_definitions.entrar_menu_principal_validacion(event, [ent_usuario.get_valor(), ent_clave.get_valor()]))
    btn_crear_cuenta.evento(events_definitions.entrar_crear_cuenta)





#MAIN CALL
def call_main(usuario:Usuario.Usuario):
    # INSTANCIAS DE WIDGETS
    print(f"BIENVENIDO!!!!\nUsuario : {usuario.get_nombre()}\nID : {usuario.get_id()}")
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

    # LLAMADA A EVENTOS
    # btn_crear_nota.evento(events_definitions.entrar_crear_nota)
    btn_crear_nota.get_boton().bind("<Button-1>", lambda event:events_definitions.entrar_crear_nota(event, usuario))
    # btn_buscar_nota.evento(events_definitions.entrar_buscar_nota)
    btn_buscar_nota.get_boton().bind("<Button-1>", lambda event:events_definitions.entrar_buscar_nota(event, usuario))
    # btn_listar_nota.evento(events_definitions.listar_notas)
    btn_listar_nota.get_boton().bind("<Button-1>", lambda event:events_definitions.listar_notas(event, usuario))
    btn_salir.evento(events_definitions.cerrar_programa)





#CREAR CUENTA CALL
def crear_cuenta_call():
    lbl_usuario = Label(windows_definitions.crear_cuenta.get_ventana(), text="Usuario")
    ent_usuario = Entrada.Entrada(ventana=windows_definitions.crear_cuenta, width=40, value="Usuario ...")
    lbl_clave1 = Label(windows_definitions.crear_cuenta.get_ventana(), text="Clave")
    ent_clave = Entrada.Entrada(ventana=windows_definitions.crear_cuenta, width=40, value="Clave ...", pwd=True)
    lbl_clave2 = Label(windows_definitions.crear_cuenta.get_ventana(), text="Repetir clave")
    ent_repeat_clave = Entrada.Entrada(ventana=windows_definitions.crear_cuenta, width=40, value="Repetir clave ...", pwd=True)
    btn_crear_cuenta = Boton.Boton(ventana=windows_definitions.crear_cuenta, width=40, height=2, texto="Registrar Cuenta", bgcolor="pale green", borde=3, tborde='raised')

    lbl_usuario.place(x=80, y=30)
    ent_usuario.crear_entrada(80, 50)
    lbl_clave1.place(x=80, y=80)
    ent_clave.crear_entrada(80, 100)
    lbl_clave2.place(x=80, y=130)
    ent_repeat_clave.crear_entrada(80, 150)
    btn_crear_cuenta.crear_boton(55, 200)

    # LLAMADA A EVENTOS
    btn_crear_cuenta.get_boton().bind("<Button-1>", lambda event:events_definitions.crear_cuenta_crear_usuario(event, [ent_usuario.get_valor(), ent_clave.get_valor(), ent_repeat_clave.get_valor()]))




#CREAR NOTA CALL
def crear_nota_call(usuario:Usuario.Usuario):
    # INSTANCIAS DE WIDGETS
    v_txt_cuerpo = StringVar().set('')
    ent_titulo = Entrada.Entrada(ventana=windows_definitions.crear_nota, width=40, value="Titulo ...")
    btn_crear_nota = Boton.Boton(ventana=windows_definitions.crear_nota, width=30, height=2, texto="Guardar", bgcolor='lightblue', borde=2, tborde='raised')
    txt_cuerpo = Text(windows_definitions.crear_nota.get_ventana(), width=40)

    # CREACION DE WIDGETS
    ent_titulo.crear_entrada(80, 20)
    txt_cuerpo.place(x=40, y=50)
    btn_crear_nota.crear_boton(90, 500)

    # LLAMADA A EVENTOS
    btn_crear_nota.get_boton().bind("<Button-1>", lambda event:events_definitions.crear_nota_crear_nota(event, [ent_titulo.get_valor(), txt_cuerpo.get('1.0', "end-1c")], usuario))







#BUSCAR NOTA CALL
def buscar_nota_call(usuario:Usuario.Usuario):
    print(events_definitions.notas)
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
    # btn_buscar.evento(wevento=events_definitions.buscar_nota,widget=grid_resultados)

    # LLAMADA A EVENTOS
    btn_buscar.get_boton().bind("<Button-1>", lambda event:events_definitions.buscar_nota_por_titulo(event, grid_resultados, ent_buscar.get_valor(), usuario))
    grid_resultados.get_grid().bind("<Double-1>", lambda event:events_definitions.buscar_nota_por_titulo_seleccionar(event, grid_resultados.fila_seleccionada(), events_definitions.notas))
    windows_definitions.buscar_nota.get_ventana().protocol("WM_DELETE_WINDOW", lambda:events_definitions.buscar_nota_reset_notas(grid_resultados))







#LISTAR NOTA CALL
def listar_notas_call(usuario:Usuario.Usuario):
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
    # btn_buscar.evento(wevento=events_definitions.buscar_nota_por_titulo, widget=grid_resultados)    
   
    # LLAMADA A EVENTOS
    btn_buscar.get_boton().bind("<Button-1>", lambda event:events_definitions.listar_notas_listar(event, grid_resultados, usuario))
    grid_resultados.get_grid().bind("<Double-1>", lambda event:events_definitions.listar_notas_listar_seleccionar(event, grid_resultados.fila_seleccionada(), events_definitions.notas))
    btn_modificar_nota.evento(events_definitions.entrar_modificar_nota)
    windows_definitions.listar_notas.get_ventana().protocol("WM_DELETE_WINDOW", lambda:events_definitions.listar_notas_reset_notas(grid_resultados))








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

    # LLAMADA A EVENTOS
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
def nota_view_call(key):
    # INSTANCIAS DE WIDGETS
    txt_cuerpo = Text(windows_definitions.nota.get_ventana(), width=40, height=20, state="normal")
    txt_cuerpo.insert(END, events_definitions.notas[key].get_cuerpo())
    txt_cuerpo.configure(state="disabled", bg="lightgrey")

    # CREACION DE WIDGETS
    txt_cuerpo.place(x=2, y=1)
    txt_cuerpo.pack(fill="both", expand=1)

    # LLAMADA A EVENTOS
    windows_definitions.nota.get_ventana().bind("<Control-f>", lambda event:events_definitions.nota_view_maximiza(event))
    windows_definitions.nota.get_ventana().bind("<Escape>", windows_definitions.nota.cerrar_ventana)





#PRIMERA CALL
call_login()

