import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import zoo
import konstanten
# python -m pip install Pillow

#Variablen definieren
startzeile = 3
startspalte = 1

label_list = []

def tier_erstellen():
    tier = zoo.Tier("kaenguru", "Beuteltier", "Gras", "Peter", 1/1/2022, "maennlich")

def kanguru_add(app):
    global startzeile
    global startspalte

    if len(label_list) % konstanten.MAX_LABELS_PER_ROW == 0 and label_list != []:
        # Wenn das Maximum erreicht ist, in die nächste Zeile wechseln
        startzeile += 1
        startspalte = 1

    label = ttk.Label(root, image=app.photo)
    label.grid(row=startzeile, column=startspalte)
    startspalte += 1
    label_list.append(label)
    app.label_kanguru_menge["text"] =  "Kangurus: " + str(len(label_list))
    print("Kanguru wurde hinzugefügt")

def kanguru_remove():
    global startspalte
    global startzeile
    if label_list:
        label_list[-1].grid_forget()
        del label_list[-1]
        startspalte -= 1
        if startspalte == 0:
            startspalte = konstanten.MAX_LABELS_PER_ROW
            startzeile -= 1
    app.label_kanguru_menge["text"] =  "Kangurus: " + str(len(label_list))
    print("Kanguru wurde enfernt")

class App:
    def __init__(self, master):

        self.master = master

        master.title("STL Creator")

        #dinge erstellen
        #label = ttk.Label(text="Inside the LabelFrame")
        #label1 = ttk.Label(root, text="Schön, dass du da bist!")
        self.label_kanguru_menge = tk.Label(root, text = "Kangurus: " + str(len(label_list)))
        self.button_kanguru_add = tk.Button(root, text="Hinzufügen", command=lambda:kanguru_add(app))
        self.button_kanguru_remove = tk.Button(root, text="Entfernen", command=kanguru_remove)

        self.image = Image.open(konstanten.KANGURUPFAD).resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        # platzieren
        #label1.grid(row=1,column=1)
        #label.grid(row=2, column=1)
        self.label_kanguru_menge.grid(row=1, column=3)
        self.button_kanguru_add.grid(row=1, column=1)
        self.button_kanguru_remove.grid(row=1, column=2)

        for i in range(konstanten.TESTKONSTANTE):
            kanguru_add(self)
        
        if konstanten.DARK_MODE:
            root.config(bg='#333333')
            self.label_kanguru_menge.config(bg='#333333')
            self.button_kanguru_add.config(bg='#333333')
            self.button_kanguru_remove.config(bg='#333333')
            self.label_kanguru_menge.config(fg='#FFFFFF')
            self.button_kanguru_add.config(fg='#FFFFFF')
            self.button_kanguru_remove.config(fg='#FFFFFF')

    def set_kanguru_label(self, text):
        self.label_kanguru_menge["text"] =  "Kangurus: " + text

if __name__ == "__main__":
    # Root ist das Hautpfenster
    root = tk.Tk()
    #root.config(bg='#999999')
    root.title("Hauptfenster von deinem Zoo")
    root.geometry(str(konstanten.MAX_LABELS_PER_ROW)*100 + "x600")
    root.iconbitmap("favicon-zoo.ico")
    
    app = App(root)

    root.mainloop()