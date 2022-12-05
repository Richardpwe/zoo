import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import zoo
# python -m pip install Pillow

# Root ist das Hautpfenster
root = tk.Tk()
root.title("Hauptfenster von deinem Zoo")
root.geometry("800x600")
root.iconbitmap("favicon-zoo.ico")


#allgemeines
dirname = os.path.dirname(__file__)
    #kangurupfad
filename = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')

#kangurumenge definieren
menge_kangurus = 0

label_list = []

def tier_erstellen():
    zoo.Tier(artname, tierklasse, futter, name, geburtsdatum, geschlecht)

def say_hello():
    print("Hallo, du hast du Button gedrückt.")

def kanguru_add():
    global menge_kangurus
    menge_kangurus += 1
    label = ttk.Label(root, image=photo)
    label.grid(row=2, column=2+len(label_list))
    label_list.append(label)
    label_kanguru_menge["text"] =  "Kangurus: " + str(menge_kangurus)
    print("Kanguru wurde hinzugefügt")

def kanguru_remove():
    global menge_kangurus
    menge_kangurus -= 1
    if label_list:
        label_list[-1].grid_forget()
        del label_list[-1]
    label_kanguru_menge["text"] =  "Kangurus: " + str(menge_kangurus)
    print("Kanguru wurde enfernt")

#dinge erstellen
button1 = ttk.Button(root, text="Klick mich", padding=5, command=say_hello)
label = ttk.Label(text="Inside the LabelFrame")
label1 = ttk.Label(root, text="Schön, dass du da bist!")
label_kanguru_menge = ttk.Label(root, text = "Kangurus: " + str(menge_kangurus))
button_kanguru_add = ttk.Button(root, text="Kanguru hinzufügen", padding=5, command=kanguru_add)
button_kanguru_remove = ttk.Button(root, text="Kanguru entfernen", padding=5, command=kanguru_remove)

image = Image.open(filename).resize((100, 100))
photo = ImageTk.PhotoImage(image)


# platzieren
label1.grid(row=1,column=1)
label.grid(row=4, column=1)
button1.grid(row=5, column=2)
label_kanguru_menge.grid(row=2, column=1)
button_kanguru_add.grid(row=3, column=1)
button_kanguru_remove.grid(row=3, column=2)

for x in range(menge_kangurus):
        labelname = "labelKangurubild"+ str(x)
        labelname = ttk.Label(root, image=photo)
        labelname.grid(row=2, column=x+2)
        label_list.append(labelname)

print(len(label_list))
root.mainloop()