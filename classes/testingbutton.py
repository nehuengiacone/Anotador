import sys
sys.path.insert(0, '.')

import classes.Ventana
import classes.Boton
def printmensaje():
    print("Hola!")

root = classes.Ventana.Ventana(500, 500, "Prueba boton", False, True, None, maximiza=False)
boton = classes.Boton.Boton(root, None, '', 0, 0, True, 'red', None, 1, 'raised')

root.crear_ventana()
boton.crear_boton(100,100)
boton.evento(printmensaje)




root.correr_ventana()