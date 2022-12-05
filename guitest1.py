import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
# python -m pip install Pillow

# Root ist das Hautpfenster
root = tk.Tk()
root.title("Hauptfenster von deinem Zoo")
root.geometry("800x600")

#allgemeines
dirname = os.path.dirname(__file__)
    #kangurupfad
filename = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')

    #kangurumenge definieren



def say_hello():
    print("Hallo, du hast du Button gedrückt.")

#dinge erstellen
button1 = ttk.Button(root, text="Klick mich", padding=5, command=say_hello)
label = ttk.Label(text="Inside the LabelFrame")
label1 = ttk.Label(root, text="Schön, dass du da bist!")



image = Image.open(filename).resize((100, 100))
photo = ImageTk.PhotoImage(image)

labelKangurubild1 = ttk.Label(root, image=photo)
labelKangurubild2 = ttk.Label(root, image=photo)

# platzieren
label1.grid(row=1,column=1)
labelKangurubild1.grid(row=2, column=1)
labelKangurubild2.grid(row=2, column=2)
label.grid(row=3, column=1)
button1.grid(row=4, column=2)



root.mainloop()