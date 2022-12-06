import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import zoo
import konstanten

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
    app.label_kanguru_menge["text"] = "Kangurus: " + str(len(label_list))
    print("Kanguru wurde enfernt")

class App:
    def __init__(self, master):
        self.master = master

        master.title("ZOO")

        #dinge erstellen
        #label = ttk.Label(text="Inside the LabelFrame")
        #label1 = ttk.Label(root, text="Schön, dass du da bist!")
        self.label_kanguru_menge = ttk.Label(root, text = "Kangurus: " + str(len(label_list)))
        self.button_kanguru_add = ttk.Button(root, text="Hinzufügen", padding=5, command=lambda:kanguru_add(app))
        self.button_kanguru_remove = ttk.Button(root, text="Entfernen", padding=5, command=kanguru_remove)
        self.button_tier_erstellen = ttk.Button(root, text="Tier erstellen", padding=5, command=lambda:app.tier_erstellen_fenster_öffnen())
        self.tier_erstellen_fenster = TierErstellenFenster(self.master)

        self.image = Image.open(konstanten.KANGURUPFAD).resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)

        # platzieren
        #label1.grid(row=1,column=1)
        #label.grid(row=2, column=1)
        self.label_kanguru_menge.grid(row=1, column=3)
        self.button_kanguru_add.grid(row=1, column=1)
        self.button_kanguru_remove.grid(row=1, column=2)
        self.button_tier_erstellen.grid(row=2, column=1, columnspan=2)

        for i in range(konstanten.TESTKONSTANTE):
            kanguru_add(self)

    def set_kanguru_label(self, text):
        self.label_kanguru_menge["text"] =  "Kangurus: " + text

    def tier_erstellen_fenster_öffnen(self):
        self.tier_erstellen_fenster = tk.Toplevel(self.master)
        self.tier_erstellen_fenster("500x500")
        self.tier_erstellen_fenster.title("Tier erstellen")
        self.app = TierErstellenFenster(self.tier_erstellen_fenster)

class TierErstellenFenster:
    def __init__(self, master):
        self.master = master

        self.fenster = tk.Frame(self.master)

        # Erstelle Eingabefelder
        self.entry_name = ttk.Entry(self.fenster)
        self.entry_art = ttk.Entry(self.fenster)
        self.entry_futter = ttk.Entry(self.fenster)
        self.entry_pfleger = ttk.Entry(self.fenster)
        self.entry_geburtsdatum = ttk.Entry(self.fenster)
        self.entry_geschlecht = ttk.Entry(self.fenster)

        # Erstelle Labels
        self.label_name = ttk.Label(self.fenster, text="Name:")
        self.label_art = ttk.Label(self.fenster, text="Art:")
        self.label_futter = ttk.Label(self.fenster, text="Futter:")
        self.label_pfleger = ttk.Label(self.fenster, text="Pfleger:")
        self.label_geburtsdatum = ttk.Label(self.fenster, text="Geburtsdatum:")
        self.label_geschlecht = ttk.Label(self.fenster, text="Geschlecht:")

        # Platziere Labels und Eingabefelder
        self.label_name.grid(row=1, column=1)
        self.entry_name.grid(row=1, column=2)
        # Platziere die restlichen Labels und Eingabefelder
        self.label_art.grid(row=2, column=1)
        self.entry_art.grid(row=2, column=2)
        self.label_futter.grid(row=3, column=1)
        self.entry_futter.grid(row=3, column=2)
        self.label_pfleger.grid(row=4, column=1)
        self.entry_pfleger.grid(row=4, column=2)
        self.label_geburtsdatum.grid(row=5, column=1)
        self.entry_geburtsdatum.grid(row=5, column=2)
        self.label_geschlecht.grid(row=6, column=1)
        self.entry_geschlecht.grid(row=6, column=2)
        # Erstelle einen Button, um das Tier zu erstellen
        self.button_tier_erstellen = ttk.Button(self.fenster, text="Tier erstellen",
                                                command=lambda:self.tier_erstellen(self.entry_name.get(),
                                                                                self.entry_art.get(),
                                                                                self.entry_futter.get(),
                                                                                self.entry_pfleger.get(),
                                                                                self.entry_geburtsdatum.get(),
                                                                                self.entry_geschlecht.get()))
        self.button_tier_erstellen.grid(row=7, column=1, columnspan=2)

    def tier_erstellen(self, name, art, futter, pfleger, geburtsdatum, geschlecht):
        tier = zoo.Tier(name, art, futter, pfleger, geburtsdatum, geschlecht)
        self.fenster.withdraw()

if __name__ == "__main__":
    # Root ist das Hautpfenster
    root = tk.Tk()
    root.title("Hauptfenster von deinem Zoo")
    root.geometry(str(konstanten.MAX_LABELS_PER_ROW)*100 + "x600")
    root.iconbitmap("favicon-zoo.ico")
    app = App(root)

    root.mainloop()