import sys
sys.path.insert(0, '.')

from classes import Ventana


# INSTANCIAS DE VENTANA
#instancia de ventana principal
root = Ventana.Ventana(width=500, height=500, titulo="Anotador - Login", root=True, completa=False, maximiza=False)
# root = Ventana.Ventana(width=500, height=500, titulo="Anotador - Main", root=False, completa=False, maximiza=False)




# CREAR LA VENTANA
root.crear_ventana()




# RUN DEF
def run():
    root.correr_ventana()





