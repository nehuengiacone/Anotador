import Ventana
import tkinter
from PIL import Image, ImageTk


root = Ventana.Ventana(width=600, height=600, root=True)
root.crear_ventana()

# abro la imagen con PIL
imagen = Image.open("./assets/imgs/image-login.png")
# redimensiono la imagen
imagen = imagen.resize((200, 200))
# asigno la imagen editada a imagetk
imagenTK = ImageTk.PhotoImage(imagen)
# el canvas permite dibujar la imagen y asignarle color al fondo transparente
canva = tkinter.Canvas(root.get_ventana(), width=600, height=500, background="light blue", border=0, highlightbackground="light coral")
canva.pack()
# dibujo la imagen
canva.create_image(100,250,image=imagenTK)


root.correr_ventana()