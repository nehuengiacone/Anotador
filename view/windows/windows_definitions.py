# import sys
# sys.path.insert(0, '.')

from classes import Ventana


# INSTANCIAS DE VENTANA
#instancia de ventana principal
root = Ventana.Ventana(width=400, height=300, titulo="Anotador - Login", root=True, completa=False, maximiza=False)
main = Ventana.Ventana(width=400, height=300, titulo="Anotador - Login", root=True, completa=False, maximiza=False)



# CREAR LA VENTANA
root.crear_ventana()




# RUN DEF
def run():
    root.correr_ventana()





