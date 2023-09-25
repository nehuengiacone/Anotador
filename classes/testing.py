import Ventana
import Marcos
import tkinter
import Grid

root = Ventana.Ventana(800, 400, "Testing Marco", False, root=True, rx=True, ry=True, maximiza=False)
root.crear_ventana()

marco = Marcos.Marco(ventana=root, marco=None, width=700, height=300, background_color="blue", borde=2, tipo_borde="groove", marginx=0, marginy=0, align="top")
marco.crear_marco()

grid = Grid.Grid(marco=marco, encabezados=("Nombre", "Apellido", "DNI", "Apodo"))
grid.crear_tabla_visual()

grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Nehui"]])
grid.insertar_filas([["Nehuen", "Giacone", "37450510", "Osito"]])

def seleccion():
    grid.fila_seleccionada()
    grid.get_info_fila_seleccionada()


sc = tkinter.Scrollbar(grid.get_grid(), orient="vertical")
sc.pack(side="right", fill="y")
grid.get_grid().config(yscrollcommand=sc.set)
sc.config(command=grid.get_grid().yview)

root.get_ventana().after(3000, seleccion)
root.correr_ventana()