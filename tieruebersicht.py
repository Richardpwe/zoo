import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from dateutil.parser import parse
import zoo
import konstanten


class TierUebersichtFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tier Übersicht")
        self.geometry("590" + "x500")
        self.resizable(width=False, height=True)
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")
        self.configure(padx=20, pady=20)
        self.grid_propagate(False)

        self.scrollbar = ttk.Scrollbar(self, orient='horizontal')
        self.c = tk.Canvas(self, bg='white', bd=2, relief='groove', xscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.c.xview)

        self.button_frame = ttk.Frame(self)
        self.button_zurueck_home = ttk.Button(self.button_frame, text="Home", command=self.back_home)
        self.button_tier_hinzufuegen = ttk.Button(self.button_frame, text="Tier hinzufügen",
                                                  command=self.tier_hinzufuegen)

        self.button_frame.grid(column=0, row=0, sticky="w")
        self.button_zurueck_home.grid(row=0, column=0, padx=10, pady=5)
        self.button_tier_hinzufuegen.grid(row=0, column=1)

        self.seperator = ttk.Separator(self, orient='horizontal')
        self.seperator.grid(row=1, column=0, sticky='ew', pady=5)

        self.tier_frame = ttk.Frame(self)
        self.tier_frame.grid(row=2, column=0, padx=5, pady=5)
        self.tiere_anzeigen()

    def tiere_anzeigen(self):
        tiere = zoo.neuer_zoo.get_tiere()
        row = 0
        col = 0
        for tier in tiere:
            new_frame = ttk.Frame(self.tier_frame, padding=10, width=125, height=180, relief="solid")
            new_frame.grid_propagate(False)
            tiername = tier.get_tiername()
            new_frame.bind("<Button-1>", lambda event, arg=tiername: self.neue_tierinfo(arg))

            tierart_bild = konstanten.TIERFOTOS[tier.get_bild()]
            image = Image.open(tierart_bild)
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)

            bild_label = ttk.Label(new_frame, image=photo)
            bild_label.image = photo
            bild_label.grid(row=0, column=0)

            text_label = ttk.Label(new_frame, text=tier.get_tiername(), wraplength=100)
            text_label.grid(row=1, column=0)
            text2_label = ttk.Label(new_frame, text=tier.get_artname(), wraplength=100)
            text2_label.grid(row=2, column=0)

            for widget in new_frame.winfo_children():
                widget.bind("<Button-1>", lambda event, arg=tiername: self.neue_tierinfo(arg))

            if col < 4:
                new_frame.grid(row=row, column=col, padx=5, pady=5)
                col += 1
            else:
                row += 1
                col = 0
                new_frame.grid(row=row, column=col, padx=5, pady=5)
                col += 1

    def tier_hinzufuegen(self):
        TierErstellen(self)

    def neue_tierinfo(self, tiername):
        TierInfo(self, tiername)

    def update(self):

        self.tier_frame.destroy()
        self.tier_frame = ttk.Frame(self)
        self.tier_frame.grid(row=1, column=0)
        self.tiere_anzeigen()

        zoo.neuer_zoo.zoo_speichern()

    def back_home(self):
        from hauptmenue import Hauptmenue
        self.destroy()
        Hauptmenue()

    def run(self):
        self.mainloop()


class TierInfo(tk.Toplevel):
    def __init__(self, parent, tiername):
        super().__init__(parent)
        self.tier = zoo.neuer_zoo.get_tiere_by_name(tiername)
        self.title("Tierinfo zu " + tiername + " (" + self.tier.get_artname() + ")")
        self.resizable(width=False, height=False)
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 + 300), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")
        self.parent = parent

        self.bild_frame = ttk.Frame(self, padding=20)
        self.bild_frame.grid(row=0, column=0)
        self.frame = ttk.Frame(self, padding=20)
        self.frame.grid(row=1, column=0)
        self.frame_buttonleiste = ttk.Frame(self, padding=20)
        self.frame_buttonleiste.grid(row=2, column=0)

        self.image = Image.open(konstanten.TIERFOTOS[self.tier.get_bild()])
        self.image = self.image.resize((200, 200))
        self.photo = ImageTk.PhotoImage(self.image)

        self.bild_label = ttk.Label(self.bild_frame, image=self.photo)
        self.label_tier_name = ttk.Label(self.frame, text="Name:")
        self.label_tier_name_wert = ttk.Label(self.frame, text=self.tier.get_tiername())
        self.label_tier_tierklasse = ttk.Label(self.frame, text="Tierklasse:")
        self.label_tier_tierklasse_wert = ttk.Label(self.frame, text=self.tier.get_tierklasse())
        self.label_tier_tierart = ttk.Label(self.frame, text="Tierart:")
        self.label_tier_tierart_wert = ttk.Label(self.frame, text=self.tier.get_artname())
        self.label_tier_geschlecht = ttk.Label(self.frame, text="Geschlecht:")
        self.label_tier_geschlecht_wert = ttk.Label(self.frame, text=self.tier.get_geschlecht())
        self.label_tier_geburtsdatum = ttk.Label(self.frame, text="Geburtsdatum:")
        self.label_tier_geburtsdatum_wert = ttk.Label(self.frame, text=self.tier.get_geburtsdatum())
        self.label_tier_futter = ttk.Label(self.frame, text="Futter:")
        self.label_tier_futter_wert = ttk.Label(self.frame, text=self.tier.futter.get_name())

        self.button_schliessen = ttk.Button(self.frame_buttonleiste, text="Schließen", command=self.destroy)
        self.button_loeschen = ttk.Button(self.frame_buttonleiste, text="Tier löschen", command=self.tier_loeschen)

        self.bild_label.grid(row=0, column=1)
        self.label_tier_name.grid(row=1, column=0, sticky="w", padx=10)
        self.label_tier_name_wert.grid(row=1, column=1, sticky="w", padx=10)
        self.label_tier_tierklasse.grid(row=2, column=0, sticky="w", padx=10)
        self.label_tier_tierklasse_wert.grid(row=2, column=1, sticky="w", padx=10)
        self.label_tier_tierart.grid(row=3, column=0, sticky="w", padx=10)
        self.label_tier_tierart_wert.grid(row=3, column=1, sticky="w", padx=10)
        self.label_tier_geschlecht.grid(row=4, column=0, sticky="w", padx=10)
        self.label_tier_geschlecht_wert.grid(row=4, column=1, sticky="w", padx=10)
        self.label_tier_geburtsdatum.grid(row=5, column=0, sticky="w", padx=10)
        self.label_tier_geburtsdatum_wert.grid(row=5, column=1, sticky="w", padx=10)
        self.label_tier_futter.grid(row=6, column=0, sticky="w", padx=10)
        self.label_tier_futter_wert.grid(row=6, column=1, sticky="w", padx=10)

        self.button_schliessen.grid(row=0, column=0)
        self.button_loeschen.grid(row=0, column=1)

    def tier_loeschen(self):
        zoo.neuer_zoo.tier_loeschen(self.tier)

        self.parent.update()
        self.destroy()


class TierErstellen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tier hinzufügen ...")
        self.iconbitmap("favicon-zoo.ico")
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.resizable(width=False, height=False)
        self.configure(padx=20, pady=20)

        self.label_artname = ttk.Label(self, text="Tierart:")
        self.parent = parent
        self.tierarten_liste = zoo.neuer_zoo.get_tierarten_namen()

        self.artname = tk.StringVar()
        if not self.tierarten_liste:
            self.tierarten_liste = ["leer"]

        self.entry_artname = ttk.OptionMenu(self, self.artname, 'Tierart...', *self.tierarten_liste)
        self.button_tierart_hinzufuegen = ttk.Button(self, text="+", command=self.tierart_hinzufuegen)

        self.label_name = ttk.Label(self, text="Name:")
        self.entry_name = ttk.Entry(self)
        self.label_geburtsdatum = ttk.Label(self, text="Geburtsdatum:")
        self.entry_geburtsdatum = ttk.Entry(self)
        self.label_geschlecht = ttk.Label(self, text="Geschlecht:")
        self.tiergeschlecht = tk.StringVar()
        self.entry_geschlecht = ttk.OptionMenu(self, self.tiergeschlecht, 'Geschlecht...', *konstanten.TIERGESCHLECHTER)
        self.button_create = ttk.Button(self, text="Erstelle Tier", command=self.create_tier)

        self.label_artname.grid(row=0, column=0, sticky="w")
        self.entry_artname.grid(row=0, column=1, sticky="w")
        self.button_tierart_hinzufuegen.grid(row=0, column=2, sticky="w")
        self.label_name.grid(row=3, column=0, sticky="w")
        self.entry_name.grid(row=3, column=1, sticky="w")
        self.label_geburtsdatum.grid(row=4, column=0, sticky="w")
        self.entry_geburtsdatum.grid(row=4, column=1, sticky="w")
        self.label_geschlecht.grid(row=5, column=0, sticky="w")
        self.entry_geschlecht.grid(row=5, column=1, sticky="w")
        self.button_create.grid(row=6, column=0, sticky="w")

    def create_tier(self):
        artname = self.artname.get()
        name = self.entry_name.get()
        geburtsdatum = parse(self.entry_geburtsdatum.get()).date()
        geschlecht = self.tiergeschlecht.get()
        new_tier = zoo.Tier(name, geburtsdatum, geschlecht, zoo.neuer_zoo.get_tierart_by_name(artname))
        zoo.neuer_zoo.tiere.append(new_tier)

        self.parent.update()
        self.destroy()

    def update(self):
        self.tierarten_liste = zoo.neuer_zoo.get_tierarten_namen()
        self.entry_artname.destroy()
        self.entry_artname = ttk.OptionMenu(self, self.artname, 'Tierart...', *self.tierarten_liste)
        self.entry_artname.grid(row=0, column=1)

        zoo.neuer_zoo.zoo_speichern()

    def tierart_hinzufuegen(self):
        TierartErstellen(self)


class TierartErstellen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tierart hinzufügen ...")
        self.resizable(width=False, height=False)
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")
        self.configure(padx=20, pady=20)
        self.parent = parent
        self.futter_liste = zoo.neuer_zoo.get_futter_namen()
        self.bild_name = ""

        self.label_tierart_bild = ttk.Label(self, text="Bild:")
        self.tierart_bild = Image.open(konstanten.PLATZHALTER_BILD)
        self.tierart_bild = self.tierart_bild.resize((50, 50))
        self.tierart_foto = ImageTk.PhotoImage(self.tierart_bild)
        self.label_tierart_foto = ttk.Label(self, image=self.tierart_foto)
        self.button_bild_aendern = ttk.Button(self, text="Bild auswählen", command=self.bild_aendern)

        self.label_tierart_name = ttk.Label(self, text="Tierartname:")
        self.entry_tierart_name = ttk.Entry(self)
        self.label_tierklasse = ttk.Label(self, text="Tierklasse:")
        self.tierklasse = tk.StringVar()
        self.entry_tierklasse = ttk.OptionMenu(self, self.tierklasse, 'Tierklasse...', *konstanten.TIERKLASSEN)
        self.label_futter = ttk.Label(self, text="Futter:")

        self.futter_auswahl = tk.StringVar()
        if not self.futter_liste:
            self.futter_liste = ["leer"]

        self.entry_futter = ttk.OptionMenu(self, self.futter_auswahl, 'Futter...', *self.futter_liste)
        self.button_futter_hinzufuegen = ttk.Button(self, text="+", command=self.futter_hinzufuegen)

        self.button_save_tierart = ttk.Button(self, text="Speichern", command=self.save_tierart)

        self.foto_frame = ttk.Frame(self)

        self.label_tierart_bild.grid(row=0, column=0, sticky="w")
        self.label_tierart_foto.grid(row=0, column=1, sticky="w")
        self.button_bild_aendern.grid(row=0, column=2, sticky="w")
        self.label_tierart_name.grid(row=1, column=0, sticky="w")
        self.entry_tierart_name.grid(row=1, column=1, sticky="w")
        self.label_tierklasse.grid(row=2, column=0, sticky="w")
        self.entry_tierklasse.grid(row=2, column=1, sticky="w")
        self.label_futter.grid(row=3, column=0, sticky="w")
        self.entry_futter.grid(row=3, column=1, sticky="w")
        self.button_futter_hinzufuegen.grid(row=3, column=2, sticky="w")
        self.button_save_tierart.grid(row=4, column=1, sticky="w")
        self.foto_frame.grid(row=0, column=3, sticky="w")

    def bild_aendern(self):
        TierartBildAuswahl(self)

    def save_tierart(self):
        tierart_name = self.entry_tierart_name.get()
        tierklasse = self.tierklasse.get()
        futter = self.futter_auswahl.get()
        # bild = repr(self.fotopfad)[1:-1]
        bild = self.bild_name
        # print(bild)

        tierart = zoo.Tierart(bild, tierart_name, tierklasse, zoo.neuer_zoo.get_futter_by_name(futter))
        zoo.neuer_zoo.tierarten.append(tierart)

        self.parent.update()
        self.destroy()

    def update(self):
        self.futter_liste = zoo.neuer_zoo.get_futter_namen()
        self.entry_futter.destroy()
        self.entry_futter = ttk.OptionMenu(self, self.futter_auswahl, 'Futter...', *self.futter_liste)
        self.entry_futter.grid(row=3, column=1)

        self.tierklasse.set("Tierklasse...")

        zoo.neuer_zoo.zoo_speichern()

    def update_bild(self, bildname):
        self.label_tierart_foto.destroy()
        self.bild_name = bildname
        pfad = konstanten.TIERFOTOS[bildname]

        self.tierart_bild = Image.open(pfad)
        self.tierart_bild = self.tierart_bild.resize((50, 50))
        self.tierart_foto = ImageTk.PhotoImage(self.tierart_bild)
        self.label_tierart_foto = ttk.Label(self, image=self.tierart_foto)
        self.label_tierart_foto.grid(row=0, column=1)

    def futter_hinzufuegen(self):
        FutterErstellen(self)


class TierartBildAuswahl(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Bild auswählen")
        self.resizable(width=False, height=False)
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")
        self.configure(padx=20, pady=20)
        self.parent = parent

        self.bilder_frame = ttk.Frame(self)
        self.bilder_frame.grid(row=0, column=0)

        self.image_labels = {}
        self.row = 0
        self.col = 0

        for name, path in konstanten.TIERFOTOS.items():
            self.image = Image.open(path)
            self.image = self.image.resize((50, 50))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_labels[name] = self.photo

        for label_name, image in self.image_labels.items():
            self.label_tierart_foto = ttk.Label(self.bilder_frame, image=image, name=label_name)

            if self.col < 5:
                self.label_tierart_foto.grid(row=self.row, column=self.col)
                self.col += 1
            else:
                self.col = 0
                self.row += 1
                self.label_tierart_foto.grid(row=self.row, column=self.col)

        for widget in self.bilder_frame.winfo_children():
            widget.bind("<Button-1>", lambda event: self.bild_auswahl(event))

    def bild_auswahl(self, event):
        widget = event.widget
        punkt = str(widget).rfind(".")
        animal_name = str(widget)[punkt + 1:]
        # print(animal_name)

        self.destroy()
        self.parent.update_bild(animal_name)


class FutterErstellen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Futter hinzufügen ...")
        self.resizable(width=False, height=False)
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")
        self.configure(padx=20, pady=20)
        self.parent = parent

        self.label_futter_name = ttk.Label(self, text="Futtername:")
        self.entry_futter_name = ttk.Entry(self)
        self.label_preis = ttk.Label(self, text="Preis:")
        self.entry_preis = ttk.Entry(self)

        self.button_save_futter = ttk.Button(self, text="Speichern", command=self.save_futter)

        self.label_futter_name.grid(row=0, column=0, sticky="w")
        self.entry_futter_name.grid(row=0, column=1, sticky="w")
        self.label_preis.grid(row=1, column=0, sticky="w")
        self.entry_preis.grid(row=1, column=1, sticky="w")
        self.button_save_futter.grid(row=2, column=1, sticky="w")

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
