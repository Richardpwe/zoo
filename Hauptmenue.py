import tkinter as tk
from tkinter import ttk
import konstanten
from PIL import Image, ImageTk
# import zoo
from Tieruebersicht import TierUebersichtFenster
from einstellungen import EinstellungenFenster
from Uebersicht import UebersichtFenster
import zoo


class Hauptmenue(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hauptmenü")
        self.geometry("300x750")
        self.resizable(width=False, height=False)
        self.iconbitmap("favicon-zoo.ico")

        # Frames erstellen
        self.frame_title = ttk.Frame(self)
        self.frame_title.pack(padx=20, pady=20)

        self.frame_zooinfo = ttk.Frame(self)
        self.frame_zooinfo.pack(padx=0, pady=0)

        self.frame_menu = ttk.Frame(self)
        self.frame_menu.pack(padx=20, pady=20)
        
        # TTK Style
        s = ttk.Style()
        s.configure('Heading.TLabel', font='default 24 bold')
        s.configure('Sub1.TLabel', font='default 8 bold')
        s.configure('TButton', width = 20)

        # Zoo Titel
        self.label1 = ttk.Label(self.frame_title, text = "Zooverwaltung", style='Heading.TLabel')
        self.label1.pack(pady=0)

        # Bild einfügen
        self.image = Image.open(konstanten.ZOO_LOGO_PFAD).resize((250, 250))
        self.photo = ImageTk.PhotoImage(self.image) 

        self.bild_label = ttk.Label(self.frame_title, image=self.photo)
        self.bild_label.pack(pady=0)

        # Zooinfos
        self.label_zookartei = ttk.Label(self.frame_zooinfo, text="Aktuelle Zookartei:").grid(row=0, column=0, sticky="w")
        self.label_zooinfo1 = ttk.Label(self.frame_zooinfo, text=zoo.neuer_zoo.get_name(), style='Sub1.TLabel').grid(row=1, column=0, sticky="w")
        self.label_zooinfo2 = ttk.Label(self.frame_zooinfo, text=zoo.neuer_zoo.get_strasse()
            + " " + str(zoo.neuer_zoo.get_hausnummer()), anchor="w", style='Sub1.TLabel').grid(row=2, column=0, sticky="w")
        self.label_zooinfo3 = ttk.Label(self.frame_zooinfo, text=str(zoo.neuer_zoo.get_plz())
            + " " + zoo.neuer_zoo.get_ort(), style='Sub1.TLabel').grid(row=3, column=0, sticky="w")
        self.label_zooinfo4 = ttk.Label(self.frame_zooinfo, text="Eröffnet am:", style='Sub1.TLabel').grid(row=4, column=0, sticky="w")
        self.label_zooinfo5 = ttk.Label(self.frame_zooinfo, text=zoo.neuer_zoo.get_eroeffnungsdatum()).grid(row=4, column=1, sticky="w")
        self.label_zooinfo6 = ttk.Label(self.frame_zooinfo, text="Tiere:", style='Sub1.TLabel').grid(row=5, column=0, sticky="w")
        self.label_zooinfo7 = ttk.Label(self.frame_zooinfo, text=str(zoo.neuer_zoo.get_tiere_anzahl())).grid(row=5, column=1, sticky="w")
        self.label_zooinfo8 = ttk.Label(self.frame_zooinfo, text="Personal:", style='Sub1.TLabel').grid(row=6, column=0, sticky="w")
        self.label_zooinfo9 = ttk.Label(self.frame_zooinfo, text=str(zoo.neuer_zoo.get_personal_anzahl())).grid(row=6, column=1, sticky="w")

        # Button erstellen, um Fenster 1 zu öffnen
        self.button_1 = ttk.Button(self.frame_menu, text="Tierübersicht", command=self.open_tieruebersicht, width=20)
        self.button_1.pack(pady=10)

        # Button erstellen, um Fenster 2 zu öffnen
        self.button_2 = ttk.Button(self.frame_menu, text="Fenster 2", command=self.open_tieruebersicht, width=20)
        self.button_2.pack(pady=10)

        # Button erstellen, um Fenster 3 zu öffnen
        self.button_3 = ttk.Button(self.frame_menu, text="Übersicht", command=self.open_uebersicht, width=20)
        self.button_3.pack(pady=10)

        # Button erstellen, um Fenster 4 zu öffnen
        self.button_4 = ttk.Button(self.frame_menu, text="Einstellungen", command=self.open_einstellungen, width=20)
        self.button_4.pack(pady=10)

        # Button erstellen, der das Programm beendet, wenn man darauf klickt
        self.quit_button = ttk.Button(self.frame_menu, text='Beenden', command=self.destroy, width=20)
        self.quit_button.pack(pady=10)

        if konstanten.DARK_MODE:
            style = ttk.Style()
            style.configure("dark.background", background=konstanten.DARK_MODE_COLOR)

            self.configure(background=konstanten.DARK_MODE_COLOR)
            self.frame.configure(style="dark.background")
            self.button_1.configure(style="dark.background")
            self.button_2.configure(style="dark.background")
            self.button_3.configure(style="dark.background")
            self.button_4.configure(style="dark.background")
            self.quit_button.configure(style="dark.background")

    def open_tieruebersicht(self):
        self.destroy()
        tier_fenster = TierUebersichtFenster()
        tier_fenster.run()

    def open_personaluebersicht(self):
        print("Personaluebersicht")

    def open_uebersicht(self):
        self.destroy()
        uebersicht = UebersichtFenster()
        uebersicht.run()

    def open_einstellungen(self):
        self.destroy()
        einstellungen = EinstellungenFenster()
        einstellungen.run()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = Hauptmenue()
    fenster.run()
