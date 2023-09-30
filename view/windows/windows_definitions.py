# import sys
# sys.path.insert(0, '.')

from classes import Ventana


# INSTANCIAS DE VENTANA
#instancia de ventana principal
root = Ventana.Ventana(width=400, height=300, titulo="Anotador - Login", root=True, completa=False, maximiza=False)
main = Ventana.Ventana(width=400, height=300, titulo="Anotador - Main", root=True, completa=False, maximiza=False)
crear_nota = Ventana.Ventana(width=400, height=600, titulo="Anotador - Crear Nota", root=False, completa=False, maximiza=False)
modificar_nota = Ventana.Ventana(width=400, height=600, titulo="Anotador - Modificar Nota", root=False, completa=False, maximiza=False)
nota = Ventana.Ventana(width=330, height=330, titulo="Anotador - Nota", root=False, completa=False, maximiza=False)
buscar_nota = Ventana.Ventana(width=600, height=400, titulo="Anotador - Buscar Notas", root=False, completa=False, maximiza=False)
listar_notas = Ventana.Ventana(width=600, height=400, titulo="Anotador - Listar Notas", root=False, completa=False, maximiza=False)

# CREAR LA VENTANA
root.crear_ventana()    




# RUN DEF
def run():
    root.correr_ventana()





