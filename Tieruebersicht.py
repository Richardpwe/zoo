import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import zoo
import konstanten


class TierUebersichtFenster:
    def __init__(self):
        self.fenster = tk.Tk()
        self.fenster.title("Tier Übersicht")
        self.fenster.geometry(str(konstanten.MAX_LABELS_PER_ROW) * 100 + "x600")
        self.fenster.iconbitmap("favicon-zoo.ico")

        self.button_zurueck_home = tk.Button(self.fenster, text="Home", command=self.back_home)
        self.button_tier_hinzufuegen = tk.Button(self.fenster,
                                                 text="Tier Hinzufügen", command=self.tier_hinzufuegen)

        try:
            self.image = Image.open(konstanten.KANGAROO_PFAD)
            self.image = self.image.resize((100, 100))
            # if konstanten.DARK_MODE:
            self.photo = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print("Bilddatei nicht gefunden")

        self.button_zurueck_home.grid(row=1, column=2)
        self.button_tier_hinzufuegen.grid(row=1, column=4)

        if konstanten.DARK_MODE:
            self.fenster.config(bg=konstanten.DARK_MODE_COLOR)
            self.button_zurueck_home.config(bg=konstanten.DARK_MODE_COLOR)
            self.button_zurueck_home.config(fg='#FFFFFF')

    def tiere_anzeigen(self):
        print(self)

    def tier_hinzufuegen(self):
        TierErstellen(self.fenster)

    def back_home(self):
        self.fenster.destroy()

    def run(self):
        self.fenster.mainloop()


class TierErstellen:
    def __init__(self, tier_uebersicht_fenster):
        self.fenster = tk.Tk()
        self.fenster.title("Tier Erstellung Formular")
        self.label_artname = tk.Label(self.fenster, text="Tierart:")
        self.tier_uebersicht_fenster = tier_uebersicht_fenster

        if zoo.neuer_zoo.tierarten:
            self.artname = tk.StringVar()
            self.artname.set("Tierart...")
            self.entry_artname = tk.OptionMenu(self.fenster, self.artname, *zoo.neuer_zoo.tierarten)
            self.entry_artname.grid(row=0, column=1)

        self.button_tierart_hinzufuegen = tk.Button(self.fenster, text="+", command=self.tierart_hinzufuegen)

        self.label_name = tk.Label(self.fenster, text="Name:")
        self.entry_name = tk.Entry(self.fenster)
        self.label_geburtsdatum = tk.Label(self.fenster, text="Geburtsdatum:")
        self.entry_geburtsdatum = tk.Entry(self.fenster)
        self.label_geschlecht = tk.Label(self.fenster, text="Geschlecht:")
        self.tiergeschlecht = tk.StringVar()
        self.tiergeschlecht.set("Geschlecht...")
        self.entry_geschlecht = tk.OptionMenu(self.fenster, self.tiergeschlecht, *konstanten.TIERGESCHLECHTER)
        self.button_create = tk.Button(self.fenster, text="Erstelle Tier", command=self.create_tier)

        self.label_artname.grid(row=0, column=0)
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
        new_tier = zoo.Tier(artname, zoo.neuer_zoo.tierarten[artname].tierklasse,
                            zoo.neuer_zoo.tierarten[artname].futter.name, name, geburtsdatum, geschlecht)
        zoo.neuer_zoo.tiere.append(new_tier)
        print(zoo.neuer_zoo)

        self.fenster.destroy()

    def tierart_hinzufuegen(self):
        TierartErstellen(self.fenster)


class TierartErstellen:
    def __init__(self, tier_erstellen_fenster):
        self.tierart_erstellen_fenster = tk.Tk()
        self.tierart_erstellen_fenster.title("Tierart Erstellung Formular")
        self.tier_erstellen_fenster = tier_erstellen_fenster

        self.label_tierart_name = tk.Label(self.tierart_erstellen_fenster, text="Tierartname:")
        self.entry_tierart_name = tk.Entry(self.tierart_erstellen_fenster)
        self.label_tierklasse = tk.Label(self.tierart_erstellen_fenster, text="Tierklasse:")
        self.tierklasse = tk.StringVar()
        self.tierklasse.set("Tierklasse...")
        self.entry_tierklasse = tk.OptionMenu(self.tierart_erstellen_fenster, self.tierklasse, *konstanten.TIERKLASSEN)
        self.label_futter = tk.Label(self.tierart_erstellen_fenster, text="Futter:")

        if zoo.neuer_zoo.futter:
            self.futter_auswahl = tk.StringVar()
            self.futter_auswahl.set("Futter...")
            self.entry_futter = tk.OptionMenu(self.tierart_erstellen_fenster,
                                              self.futter_auswahl, *zoo.neuer_zoo.futter)
            self.entry_futter.grid(row=2, column=1)

        self.button_futter_hinzufuegen = tk.Button(self.tierart_erstellen_fenster, text="+",
                                                   command=self.futter_hinzufuegen)

        self.button_save_tierart = tk.Button(self.tierart_erstellen_fenster,
                                             text="Speichern", command=self.save_tierart)

        self.label_tierart_name.grid(row=0, column=0)
        self.entry_tierart_name.grid(row=0, column=1)
        self.label_tierklasse.grid(row=1, column=0)
        self.entry_tierklasse.grid(row=1, column=1)
        self.label_futter.grid(row=2, column=0)
        self.button_futter_hinzufuegen.grid(row=2, column=2)
        self.button_save_tierart.grid(row=3, column=1)

    def save_tierart(self):

        tierart_name = self.entry_tierart_name.get()
        tierklasse = self.tierklasse.get()
        futter = self.futter_auswahl.get()

        tierart = zoo.Tierart(tierart_name, tierklasse, futter)
        zoo.neuer_zoo.tierarten.append(tierart)

        self.tier_erstellen_fenster.update()
        self.tierart_erstellen_fenster.destroy()

    def futter_hinzufuegen(self):
        FutterErstellen(self.tierart_erstellen_fenster)


class FutterErstellen:
    def __init__(self, tierart_erstellen_fenster):
        self.futter_erstellen_fenster = tk.Tk()
        self.futter_erstellen_fenster.title("Futter Erstellung Formular")
        self.tierart_erstellen_fenster = tierart_erstellen_fenster

        self.label_futter_name = tk.Label(self.futter_erstellen_fenster, text="Futtername:")
        self.entry_futter_name = tk.Entry(self.futter_erstellen_fenster)
        self.label_preis = tk.Label(self.futter_erstellen_fenster, text="Preis:")
        self.entry_preis = tk.Entry(self.futter_erstellen_fenster)

        self.button_save_futter = tk.Button(self.futter_erstellen_fenster, text="Speichern", command=self.save_futter)

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

        self.tierart_erstellen_fenster.update()
        self.futter_erstellen_fenster.destroy()


if __name__ == "__main__":
    fenster = TierUebersichtFenster()
    fenster.run()
