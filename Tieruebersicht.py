import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import zoo
import konstanten


def tier_erstellen():
    tier = zoo.Tier("kaenguru", "Beuteltier", "Gras", "Peter", 1 / 1 / 2022, "maennlich")


class TierUebersichtFenster:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tier Übersicht")
        self.window.geometry(str(konstanten.MAX_LABELS_PER_ROW) * 100 + "x600")
        self.window.iconbitmap("favicon-zoo.ico")

        self.startzeile = 3
        self.startspalte = 1

        self.label_list = []

        # self.label_kanguru_menge = tk.Label(self.window, text="Kangurus: 0")
        # self.button_kanguru_add = tk.Button(self.window, text="Hinzufügen", command=self.kanguru_add)
        # self.button_kanguru_remove = tk.Button(self.window, text="Entfernen", command=self.kanguru_remove)
        self.button_tier_hinzufuegen = tk.Button(self.window, text="Tier Hinzufügen", command=self.open_formular)

        try:
            self.image = Image.open(konstanten.KANGAROO_PFAD)
            self.image = self.image.resize((100, 100))
            # if konstanten.DARK_MODE:
            self.photo = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print("Bilddatei nicht gefunden")

        # self.label_kanguru_menge.grid(row=1, column=3)
        # self.button_kanguru_add.grid(row=1, column=1)
        # self.button_kanguru_remove.grid(row=1, column=2)
        self.button_tier_hinzufuegen.grid(row=1, column=4)

        # if isinstance(konstanten.TESTKONSTANTE, int) and konstanten.TESTKONSTANTE > 0:
        # for i in range(konstanten.TESTKONSTANTE):
        # self.kanguru_add()

        if konstanten.DARK_MODE:
            self.window.config(bg=konstanten.DARK_MODE_COLOR)
            # self.label_kanguru_menge.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_kanguru_add.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_kanguru_remove.config(bg=konstanten.DARK_MODE_COLOR)
            # self.label_kanguru_menge.config(fg='#FFFFFF')
            # self.button_kanguru_add.config(fg='#FFFFFF')
            # self.button_kanguru_remove.config(fg='#FFFFFF')

    def tiere_anzeigen(self):
        print(self)

    def open_formular(self):
        formular_window = tk.Toplevel(self.window)
        formular = TierErstellen(formular_window)

    def run(self):
        self.window.mainloop()


class TierErstellen:
    def __init__(self, master):
        self.master = master
        master.title("Tier Erstellung Formular")
        self.label_artname = tk.Label(master, text="Tierart:")

        if zoo.neuer_zoo.tierarten:
            self.artname = tk.StringVar()
            self.artname.set("Tierart...")
            self.entry_artname = tk.OptionMenu(master, self.artname, *zoo.neuer_zoo.tierarten)
            self.entry_artname.grid(row=0, column=1)

        self.button_tierart_hinzufuegen = tk.Button(master, text="+", command=self.open_tierart_formular)

        self.label_tierklasse = tk.Label(master, text="Tierklasse:")
        self.tierklasse = tk.StringVar()
        self.tierklasse.set("Tierklasse...")
        self.entry_tierklasse = tk.OptionMenu(master, self.tierklasse, *konstanten.TIERKLASSEN)
        self.label_futter = tk.Label(master, text="Futter:")
        self.entry_futter = tk.Entry(master)
        self.label_name = tk.Label(master, text="Name:")
        self.entry_name = tk.Entry(master)
        self.label_geburtsdatum = tk.Label(master, text="Geburtsdatum:")
        self.entry_geburtsdatum = tk.Entry(master)
        self.label_geschlecht = tk.Label(master, text="Geschlecht:")
        self.tiergeschlecht = tk.StringVar()
        self.tiergeschlecht.set("Geschlecht...")
        self.entry_geschlecht = tk.OptionMenu(master, self.tiergeschlecht, *konstanten.TIERGESCHLECHTER)
        self.button_create = tk.Button(master, text="Erstelle Tier", command=self.create_tier)

        self.label_artname.grid(row=0, column=0)
        self.button_tierart_hinzufuegen.grid(row=1, column=2)
        self.label_tierklasse.grid(row=1, column=0)
        self.entry_tierklasse.grid(row=1, column=1)
        self.label_futter.grid(row=2, column=0)
        self.entry_futter.grid(row=2, column=1)
        self.label_name.grid(row=3, column=0)
        self.entry_name.grid(row=3, column=1)
        self.label_geburtsdatum.grid(row=4, column=0)
        self.entry_geburtsdatum.grid(row=4, column=1)
        self.label_geschlecht.grid(row=5, column=0)
        self.entry_geschlecht.grid(row=5, column=1)
        self.button_create.grid(row=6, column=0)

    def create_tier(self):
        artname = self.artname.get()
        tierklasse = self.tierklasse.get()
        futter = self.entry_futter.get()
        name = self.entry_name.get()
        geburtsdatum = self.entry_geburtsdatum.get()
        geschlecht = self.tiergeschlecht.get()
        new_tier = zoo.Tier(artname, tierklasse, futter, name, geburtsdatum, geschlecht)
        zoo.neuer_zoo.tiere.append(new_tier)
        print(zoo.neuer_zoo)

    def open_tierart_formular(self):
        tierart_formular_window = TierartErstellen(self.master)


class TierartErstellen:
    def __init__(self, master):
        self.master = master
        self.master("Tierart Erstellung Formular")

        self.label_tierart_name = tk.Label(master, text="Tierartname:")
        self.entry_tierart_name = tk.Entry(master)

        self.button_save_tierart = tk.Button(master, text="Speichern", command=self.save_tierart)

        self.label_tierart_name.grid(row=0, column=0)
        self.entry_tierart_name.grid(row=0, column=1)
        self.button_save_tierart.grid(row=1, column=0)

    def save_tierart(self):
        # Hole den Wert aus dem entry_tierart_name Entry-Feld
        tierart_name = self.entry_tierart_name.get()
        # Erstelle ein neues Tierart-Objekt mit dem Namen
        tierart = zoo.Tierart()
        # Füge das Tierart-Objekt der Liste der Tierarten hinzu
        zoo.neuer_zoo.tierarten.append(tierart)
        # Aktualisiere das Dropdown-Menü mit den Tierarten im Hauptfenster
        #self.master.entry_artname["menu"].add_command(label=tierart_name, command=tk._setit(self.master.artname, tierart_name))
        # Schließe das Fenster
        #self.destroy()


if __name__ == "__main__":
    fenster = TierUebersichtFenster()
    fenster.run()
