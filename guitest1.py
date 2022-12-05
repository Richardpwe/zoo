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
global mengeKangurus
mengeKangurus = 5



def say_hello():
    print("Hallo, du hast du Button gedrückt.")

def kanguruAdd():
    global mengeKangurus
    mengeKangurus += 1
    dinge_erstellen()
    print("Kanguru wurde hinzugefügt")

def dinge_erstellen():
    #dinge erstellen
    button1 = ttk.Button(root, text="Klick mich", padding=5, command=say_hello)
    label = ttk.Label(text="Inside the LabelFrame")
    label1 = ttk.Label(root, text="Schön, dass du da bist!")
    labelKanguruMenge = ttk.Label(root, text = "Kangurus: " + str(mengeKangurus))
    buttonKanguruAdd = ttk.Button(root, text="Kanguru hinzufügen", padding=5, command=kanguruAdd)

    image = Image.open(filename).resize((100, 100))
    photo = ImageTk.PhotoImage(image)


    # platzieren
    label1.grid(row=1,column=1)
    label.grid(row=4, column=1)
    button1.grid(row=5, column=2)
    labelKanguruMenge.grid(row=2, column=1)
    buttonKanguruAdd.grid(row=3, column=1)

    #Kangurus erstellen
    x=0
    while x < mengeKangurus:
        labelname = "labelKangurubild"+ str(x)
        #print(labelname)
        labelname = ttk.Label(root, image=photo)
        labelname.grid(row=2, column=x+2)
        x += 1


dinge_erstellen()
root.mainloop()