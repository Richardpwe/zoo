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
mengeKangurus = 0

label_list = []

def say_hello():
    print("Hallo, du hast du Button gedrückt.")

def kanguruAdd():
    global mengeKangurus
    mengeKangurus += 1
    label = tk.Label(root, image=photo)
    label.grid(row=2, column=2+len(label_list))
    label_list.append(label)
    labelKanguruMenge["text"] =  "Kangurus: " + str(mengeKangurus)
    print("Kanguru wurde hinzugefügt")

def kanguruRemove():
    global mengeKangurus
    mengeKangurus -= 1
    if label_list:
        label_list[-1].grid_forget()
        del label_list[-1]
    print("Kanguru wurde enfernt")

#dinge erstellen
button1 = ttk.Button(root, text="Klick mich", padding=5, command=say_hello)
label = ttk.Label(text="Inside the LabelFrame")
label1 = ttk.Label(root, text="Schön, dass du da bist!")
labelKanguruMenge = ttk.Label(root, text = "Kangurus: " + str(mengeKangurus))
buttonKanguruAdd = ttk.Button(root, text="Kanguru hinzufügen", padding=5, command=kanguruAdd)
buttonKanguruRemove = ttk.Button(root, text="Kanguru entfernen", padding=5, command=kanguruRemove)

image = Image.open(filename).resize((100, 100))
photo = ImageTk.PhotoImage(image)


# platzieren
label1.grid(row=1,column=1)
label.grid(row=4, column=1)
button1.grid(row=5, column=2)
labelKanguruMenge.grid(row=2, column=1)
buttonKanguruAdd.grid(row=3, column=1)
buttonKanguruRemove.grid(row=3, column=2)

for x in range(mengeKangurus):
        labelname = "labelKangurubild"+ str(x)
        labelname = ttk.Label(root, image=photo)
        labelname.grid(row=2, column=x+2)
        label_list.append(labelname)

print(len(label_list))
root.mainloop()