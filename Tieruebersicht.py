import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import zoo
import konstanten


class TierUebersichtFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tier Übersicht")
        self.geometry(str(konstanten.MAX_LABELS_PER_ROW) * 100 + "x600")
        self.iconbitmap("favicon-zoo.ico")

        self.button_zurueck_home = ttk.Button(self, text="Home", command=self.back_home)
        self.button_tier_hinzufuegen = ttk.Button(self, text="Tier Hinzufügen", command=self.tier_hinzufuegen)

        try:
            self.image = Image.open(konstanten.KANGAROO_PFAD)
            self.image = self.image.resize((100, 100))
            # if konstanten.DARK_MODE:
            self.photo = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print("Bilddatei nicht gefunden")

        self.button_zurueck_home.grid(row=0, column=0)
        self.button_tier_hinzufuegen.grid(row=0, column=1)

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.tier_frame = tk.Frame(self)
        self.tier_frame.grid(row=1, column=0)
        self.tiere_anzeigen()

    def tiere_anzeigen(self):
        tiere = zoo.neuer_zoo.get_tiere()
        row = 0
        col = 0
        for tier in tiere:
            new_frame = tk.Frame(self.tier_frame)
            bild_label = tk.Label(new_frame, image=self.photo)
            text_label = tk.Label(new_frame, text=tier.name)
            text_label.grid(row=1, column=0)
            bild_label.grid(row=0, column=0)

            if col < 4:
                new_frame.grid(row=row, column=col)
                col += 1
            else:
                row += 1
                col = 0
                new_frame.grid(row=row, column=col)

    def tier_hinzufuegen(self):
        TierErstellen(self)

    def update(self):

        self.tier_frame.destroy()
        self.tier_frame = tk.Frame(self)
        self.tier_frame.grid(row=1, column=0)
        self.tiere_anzeigen()

        zoo.neuer_zoo.zoo_speichern()

    def back_home(self):
        self.destroy()

    def run(self):
        self.mainloop()


class TierErstellen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tier Erstellung Formular")
        self.label_artname = ttk.Label(self, text="Tierart:")
        self.parent = parent
        self.tierarten_liste = zoo.neuer_zoo.get_tierarten_namen()

        self.artname = tk.StringVar()
        self.artname.set("Tierart...")
        if not self.tierarten_liste:
            self.tierarten_liste = ["leer"]

        self.entry_artname = ttk.OptionMenu(self, self.artname, *self.tierarten_liste)
        self.button_tierart_hinzufuegen = ttk.Button(self, text="+", command=self.tierart_hinzufuegen)

        self.label_name = ttk.Label(self, text="Name:")
        self.entry_name = ttk.Entry(self)
        self.label_geburtsdatum = ttk.Label(self, text="Geburtsdatum:")
        self.entry_geburtsdatum = ttk.Entry(self)
        self.label_geschlecht = ttk.Label(self, text="Geschlecht:")
        self.tiergeschlecht = tk.StringVar()
        self.tiergeschlecht.set("Geschlecht...")
        self.entry_geschlecht = ttk.OptionMenu(self, self.tiergeschlecht, *konstanten.TIERGESCHLECHTER)
        self.button_create = ttk.Button(self, text="Erstelle Tier", command=self.create_tier)

        self.label_artname.grid(row=0, column=0)
        self.entry_artname.grid(row=0, column=1)
        self.button_tierart_hinzufuegen.grid(row=0, column=2)
        self.label_name.grid(row=3, column=0)
        self.entry_name.grid(row=3, column=1)
        self.label_geburtsdatum.grid(row=4, column=0)
        self.entry_geburtsdatum.grid(row=4, column=1)
        self.label_geschlecht.grid(row=5, column=0)
        self.entry_geschlecht.grid(row=5, column=1)
        self.button_create.grid(row=6, column=0)

    def create_tier(self):
        artname = self.artname.get()
        name = self.entry_name.get()
        geburtsdatum = self.entry_geburtsdatum.get()
        geschlecht = self.tiergeschlecht.get()
        new_tier = zoo.Tier(name, geburtsdatum, geschlecht, zoo.neuer_zoo.get_tierart_by_name(artname))
        zoo.neuer_zoo.tiere.append(new_tier)

        self.parent.update()
        self.destroy()

    def update(self):
        self.tierarten_liste = zoo.neuer_zoo.get_tierarten_namen()
        self.entry_artname.destroy()
        self.entry_artname = ttk.OptionMenu(self, self.artname, *self.tierarten_liste)
        self.entry_artname.grid(row=0, column=1)

        zoo.neuer_zoo.zoo_speichern()

    def tierart_hinzufuegen(self):
        TierartErstellen(self)


class TierartErstellen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tierart Erstellung Formular")
        self.parent = parent
        self.futter_liste = zoo.neuer_zoo.get_futter_namen()

        self.label_tierart_name = ttk.Label(self, text="Tierartname:")
        self.entry_tierart_name = ttk.Entry(self)
        self.label_tierklasse = ttk.Label(self, text="Tierklasse:")
        self.tierklasse = tk.StringVar()
        self.tierklasse.set("Tierklasse...")
        self.entry_tierklasse = ttk.OptionMenu(self, self.tierklasse, *konstanten.TIERKLASSEN)
        self.label_futter = ttk.Label(self, text="Futter:")

        self.futter_auswahl = tk.StringVar()
        if not self.futter_liste:
            self.futter_liste = ["leer"]

        self.futter_auswahl.set("Futter...")

        self.entry_futter = ttk.OptionMenu(self, self.futter_auswahl, *self.futter_liste)
        self.button_futter_hinzufuegen = ttk.Button(self, text="+", command=self.futter_hinzufuegen)

        self.button_save_tierart = ttk.Button(self, text="Speichern", command=self.save_tierart)

        self.label_tierart_name.grid(row=0, column=0)
        self.entry_tierart_name.grid(row=0, column=1)
        self.label_tierklasse.grid(row=1, column=0)
        self.entry_tierklasse.grid(row=1, column=1)
        self.label_futter.grid(row=2, column=0)
        self.entry_futter.grid(row=2, column=1)
        self.button_futter_hinzufuegen.grid(row=2, column=2)
        self.button_save_tierart.grid(row=3, column=1)

    def save_tierart(self):

        tierart_name = self.entry_tierart_name.get()
        tierklasse = self.tierklasse.get()
        futter = self.futter_auswahl.get()

        tierart = zoo.Tierart(tierart_name, tierklasse, zoo.neuer_zoo.get_futter_by_name(futter))
        zoo.neuer_zoo.tierarten.append(tierart)

        self.parent.update()
        self.destroy()

    def update(self):
        self.futter_liste = zoo.neuer_zoo.get_futter_namen()
        self.entry_futter.destroy()
        self.entry_futter = ttk.OptionMenu(self, self.futter_auswahl, *self.futter_liste)
        self.entry_futter.grid(row=2, column=1)

        zoo.neuer_zoo.zoo_speichern()

    def futter_hinzufuegen(self):
        FutterErstellen(self)


class FutterErstellen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Futter Erstellung Formular")
        self.parent = parent

        self.label_futter_name = ttk.Label(self, text="Futtername:")
        self.entry_futter_name = ttk.Entry(self)
        self.label_preis = ttk.Label(self, text="Preis:")
        self.entry_preis = ttk.Entry(self)

        self.button_save_futter = ttk.Button(self, text="Speichern", command=self.save_futter)

        self.label_futter_name.grid(row=0, column=0)
        self.entry_futter_name.grid(row=0, column=1)
        self.label_preis.grid(row=1, column=0)
        self.entry_preis.grid(row=1, column=1)
        self.button_save_futter.grid(row=2, column=1)

    def save_futter(self):
        futter_name = self.entry_futter_name.get()
        preis = self.entry_preis.get()

        futter = zoo.Futter(futter_name, preis)
        zoo.neuer_zoo.futter.append(futter)

        self.parent.update()
        self.destroy()


if __name__ == "__main__":
    fenster = TierUebersichtFenster()
    fenster.run()
