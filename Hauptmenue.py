import tkinter as tk
from tkinter import ttk
import konstanten
from PIL import Image, ImageTk
from Tieruebersicht import TierUebersichtFenster
from einstellungen import EinstellungenFenster
from Uebersicht import UebersichtFenster
import zoo


class Hauptmenue(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hauptmenü")
        # self.geometry("1000x1000")
        # self.resizable(width=False, height=False)
        self.iconbitmap("favicon-zoo.ico")

        # TTK Style
        s = ttk.Style()
        s.configure('Heading.TLabel', font='default 24 bold')
        s.configure('Sub1.TLabel', font='default 12 bold')
        s.configure('TButton', width=20)

        # Frames erstellen
        self.frame_menu = ttk.Frame(self, padding=20)
        self.frame_menu.grid(row=0, column=0)

        self.right_frame = ttk.Frame(self, padding=20)
        self.right_frame.grid(row=0, column=1)

        self.frame_title = ttk.Frame(self.right_frame)
        self.frame_title.grid(row=0, column=0)

        self.frame_zooinfo = ttk.Frame(self.right_frame)
        self.frame_zooinfo.grid(row=1, column=0)

        # Zoo Titel
        self.label_zoo_titel = ttk.Label(self.frame_title, text="Zooverwaltung", style='Heading.TLabel')
        self.label_zoo_titel.grid(row=0, column=0)

        # Bild einfügen
        self.menu_image = Image.open(konstanten.ZOO_LOGO_PFAD)
        self.menu_image = self.menu_image.resize((250, 250))
        self.menu_photo = ImageTk.PhotoImage(self.menu_image)

        self.bild_label = ttk.Label(self.frame_title, image=self.menu_photo)
        self.bild_label.grid(row=1, column=0)

        # Zooinfos
        self.label_zookartei = ttk.Label(self.frame_zooinfo, text="Aktuelle Zookartei:")
        self.label_zooinfo1 = ttk.Label(self.frame_zooinfo, text=zoo.neuer_zoo.get_name(), style='Sub1.TLabel')
        adresse_1 = str(zoo.neuer_zoo.get_strasse()) + " " + str(zoo.neuer_zoo.get_hausnummer())
        self.label_zooinfo2 = ttk.Label(self.frame_zooinfo, text=str(adresse_1), anchor="w", style='Sub1.TLabel')
        adresse_2 = str(zoo.neuer_zoo.get_plz()) + " " + zoo.neuer_zoo.get_ort()
        self.label_zooinfo3 = ttk.Label(self.frame_zooinfo, text=str(adresse_2), style='Sub1.TLabel')
        self.label_zooinfo4 = ttk.Label(self.frame_zooinfo, text="Eröffnet am:", style='Sub1.TLabel')
        self.label_zooinfo5 = ttk.Label(self.frame_zooinfo, text=zoo.neuer_zoo.get_eroeffnungsdatum())
        self.label_zooinfo6 = ttk.Label(self.frame_zooinfo, text="Tiere:", style='Sub1.TLabel')
        self.label_zooinfo7 = ttk.Label(self.frame_zooinfo, text=str(zoo.neuer_zoo.get_tiere_anzahl()))
        self.label_zooinfo8 = ttk.Label(self.frame_zooinfo, text="Personal:", style='Sub1.TLabel')
        self.label_zooinfo9 = ttk.Label(self.frame_zooinfo, text=str(zoo.neuer_zoo.get_personal_anzahl()))

        self.label_zookartei.grid(row=0, column=0, sticky="w")
        self.label_zooinfo1.grid(row=1, column=0, sticky="w")
        self.label_zooinfo2.grid(row=2, column=0, sticky="w")
        self.label_zooinfo3.grid(row=3, column=0, sticky="w")
        self.label_zooinfo4.grid(row=4, column=0, sticky="w")
        self.label_zooinfo5.grid(row=4, column=1, sticky="w")
        self.label_zooinfo6.grid(row=5, column=0, sticky="w")
        self.label_zooinfo7.grid(row=5, column=1, sticky="w")
        self.label_zooinfo8.grid(row=6, column=0, sticky="w")
        self.label_zooinfo9.grid(row=6, column=1, sticky="w")

        # Button erstellen, um Fenster 1 zu öffnen
        self.button_1 = ttk.Button(self.frame_menu, text="Tierübersicht", command=self.open_tieruebersicht, width=20)
        self.button_1.grid(row=0, column=0)

        # Button erstellen, um Fenster 2 zu öffnen
        self.button_2 = ttk.Button(self.frame_menu, text="Personalübersicht",
                                   command=self.open_tieruebersicht, width=20)
        self.button_2.grid(row=1, column=0)

        # Button erstellen, um Fenster 3 zu öffnen
        self.button_3 = ttk.Button(self.frame_menu, text="Übersicht", command=self.open_uebersicht, width=20)
        self.button_3.grid(row=2, column=0)

        # Button erstellen, um Fenster 4 zu öffnen
        self.button_4 = ttk.Button(self.frame_menu, text="Einstellungen", command=self.open_einstellungen, width=20)
        self.button_4.grid(row=3, column=0)

        # Button erstellen, der das Programm beendet, wenn man darauf klickt
        self.quit_button = ttk.Button(self.frame_menu, text='Beenden', command=self.destroy, width=20)
        self.quit_button.grid(row=4, column=0)

        if konstanten.DARK_MODE:
            style = ttk.Style()
            style.configure("dark.background", background=konstanten.DARK_MODE_COLOR)

            self.configure(background=konstanten.DARK_MODE_COLOR)
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
