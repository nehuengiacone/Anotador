import sys
sys.path.insert(0, './view')

from classes import Ventana


# INSTANCIAS DE VENTANA
#instancia de ventana principal
<<<<<<< HEAD
root = classes.Ventana.Ventana(width=500, height=800, completa=False, maximiza=False)




=======
root = Ventana.Ventana(width=400, height=300, titulo="Anotador - Login", root=True, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
crear_cuenta = Ventana.Ventana(width=400, height=300, titulo="Anotador - Crear Cuenta", root=False, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
main = Ventana.Ventana(width=400, height=300, titulo="Anotador - Main", root=True, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
crear_nota = Ventana.Ventana(width=400, height=600, titulo="Anotador - Crear Nota", root=False, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
modificar_nota = Ventana.Ventana(width=400, height=600, titulo="Anotador - Modificar Nota", root=False, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
nota = Ventana.Ventana(width=330, height=330, titulo="Anotador - Nota", root=False, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
buscar_nota = Ventana.Ventana(width=600, height=400, titulo="Anotador - Buscar Notas", root=False, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
listar_notas = Ventana.Ventana(width=600, height=400, titulo="Anotador - Listar Notas", root=False, completa=False, maximiza=False, background_color="lightyellow", icono="assets/imgs/icono.ico")
>>>>>>> desarrollo

# CREAR LA VENTANA
root.crear_ventana()    




# RUN DEF
def run():
    root.correr_ventana()




