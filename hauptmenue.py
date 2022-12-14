import tkinter as tk
from tkinter import ttk
import konstanten
from PIL import Image, ImageTk
from tieruebersicht import TierUebersichtFenster
from personaluebersicht import PersonalUebersichtFenster
from einstellungen import EinstellungenFenster
from uebersicht import UebersichtFenster
import zoo


class Hauptmenue(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zooverwaltung")
        self.resizable(width=False, height=False)
        # Fenster in die Mitte des Bildschirms
        self.geometry("+{}+{}".format(int(self.winfo_screenwidth() / 2-200), int(self.winfo_screenheight() / 2-150)))
        self.iconbitmap("favicon-zoo.ico")

        # TTK Style
        s = ttk.Style()
        s.configure('Heading.TLabel', font='default 24 bold')
        s.configure('Sub1.TLabel', font='default 10 bold')
        s.configure('TButton', width=20)

        # Frames erstellen
        self.oben_frame = ttk.Frame(self)
        self.oben_frame.grid(row=0, column=0)
        self.unten_frame = ttk.Frame(self, padding=20)
        self.unten_frame.grid(row=1, column=0)

        self.left_frame = ttk.Frame(self.unten_frame)
        self.left_frame.grid(row=0, column=0)
        self.frame_menu_oben = ttk.Frame(self.left_frame)
        self.frame_menu_oben.grid(row=0, column=0, pady=20)
        self.frame_menu_unten = ttk.Frame(self.left_frame)
        self.frame_menu_unten.grid(row=1, column=0, pady=20)

        self.right_frame = ttk.Frame(self.unten_frame)
        self.right_frame.grid(row=0, column=1)

        self.frame_title = ttk.Frame(self.right_frame)
        self.frame_title.grid(row=0, column=0)

        self.frame_zooinfo = ttk.Frame(self.right_frame)
        self.frame_zooinfo.grid(row=1, column=0)

        # Zoo Titel
        self.label_zoo_titel = ttk.Label(self.oben_frame, text=zoo.neuer_zoo.get_name(), style='Heading.TLabel')
        self.label_zoo_titel.grid(row=0, column=0)

        # Bild einfügen
        self.menu_image = Image.open(konstanten.ZOO_LOGO_PFAD)
        self.menu_image = self.menu_image.resize((250, 220))
        self.menu_photo = ImageTk.PhotoImage(self.menu_image)

        self.bild_label = ttk.Label(self.frame_title, image=self.menu_photo)
        self.bild_label.grid(row=1, column=0)

        # Zooinfos
        # self.label_zookartei = ttk.Label(self.frame_zooinfo, text="Zoo Daten:")
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

        # self.label_zookartei.grid(row=0, column=0, sticky="w")
        self.label_zooinfo1.grid(row=1, column=0, sticky="w")
        self.label_zooinfo2.grid(row=2, column=0, sticky="w")
        self.label_zooinfo3.grid(row=3, column=0, sticky="w")
        self.label_zooinfo4.grid(row=4, column=0, sticky="w")
        self.label_zooinfo5.grid(row=4, column=1, sticky="w")
        self.label_zooinfo6.grid(row=5, column=0, sticky="w")
        self.label_zooinfo7.grid(row=5, column=1, sticky="w")
        self.label_zooinfo8.grid(row=6, column=0, sticky="w")
        self.label_zooinfo9.grid(row=6, column=1, sticky="w")

        self.button_1 = ttk.Button(self.frame_menu_oben, text="Tierübersicht", command=self.open_tieruebersicht,
                                   padding=10)
        self.button_1.grid(row=0, column=0, padx=10, pady=5)

        self.button_2 = ttk.Button(self.frame_menu_oben, text="Personalübersicht",
                                   command=self.open_tieruebersicht, padding=10)
        self.button_2.grid(row=1, column=0, padx=10, pady=5)

        self.button_3 = ttk.Button(self.frame_menu_oben, text="Übersicht", command=self.open_uebersicht, padding=10)
        self.button_3.grid(row=2, column=0, padx=10, pady=5)

        self.button_4 = ttk.Button(self.frame_menu_unten, text="Einstellungen", command=self.open_einstellungen,
                                   padding=10)
        self.button_4.grid(row=3, column=0, padx=10, pady=5)

        self.quit_button = ttk.Button(self.frame_menu_unten, text='Beenden', command=self.destroy, padding=10)
        self.quit_button.grid(row=4, column=0, padx=10, pady=5)

    def open_tieruebersicht(self):
        self.destroy()
        tier_fenster = TierUebersichtFenster()
        tier_fenster.run()

    def open_personaluebersicht(self):
        self.destroy()
        personal_fenster = PersonalUebersichtFenster()
        personal_fenster.run()

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
