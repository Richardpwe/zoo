import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import zoo
import konstanten
from idlelib.tooltip import Hovertip

#Variablen definieren
startzeile = 3
startspalte = 1

label_list = []

root = tk.Tk()
root.title("Hauptfenster von deinem Zoo")
root.geometry("800x600")
root.iconbitmap("favicon-zoo.ico")





def tier_erstellen():
    tier = zoo.Tier("kaenguru", "Beuteltier", "Gras", "Peter", 1/1/2022, "maennlich")



dirname = os.path.dirname(__file__)

file_square = os.path.join(dirname, 'icons', 'noun-square.png')
image_square = Image.open(file_square).resize((100, 100))
image_label_square = ImageTk.PhotoImage(image_square)
label_square = ttk.Label(root, image=image_label_square)
label_square.grid(row=1, column=1)


label_name = ttk.Label(root, text="Peter")
label_name.grid(row=2, column=2)

file_kangaroo = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')
image_kangaroo = Image.open(file_kangaroo).resize((100, 100))
image_label_kangaroo = ImageTk.PhotoImage(image_kangaroo)
label_kangaroo = ttk.Label(root, image=image_label_kangaroo)
label_kangaroo.grid(row=3, column=2)



label_zeile1 = ttk.Label(root, text="Frisst: " + "Gras")
label_zeile1.grid(row=4, column=2)

"kaenguru", "Beuteltier", "Gras", "Peter", 1/1/2022, "maennlich"

label_square1 = ttk.Label(root, image=image_label_square)
label_square1.grid(row=5, column=2)

image_button_kangaroo = ttk.Button(root, image=image_label_kangaroo)
image_button_kangaroo.grid(row=6, column=2)
kangaroo_tip = Hovertip(image_button_kangaroo,"Das ist " 'Peter' "\nEr ist ein " 'männlich' "es " 'Kanguru'  "\nEin " 'Beuteltier' ", er frisst " 'Gras')


root.mainloop()