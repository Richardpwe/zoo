import tkinter as tk
from tkinter import ttk
import konstanten
from PIL import Image, ImageTk
# import zoo
from Tieruebersicht import TierUebersichtFenster
from einstellungen import EinstellungenFenster
from Uebersicht import UebersichtFenster


class Hauptmenue(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hauptmenü")
        self.geometry("500x430")
        self.iconbitmap("favicon-zoo.ico")
        self.resizable(width=False, height=False)

        # Frame erstellen
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=20, pady=20)

        # Bild einfügen
        self.image = Image.open(konstanten.KANGAROO_PFAD).resize((200, 200))
        self.photo = ImageTk.PhotoImage(self.image) 

        self.bild_label = ttk.Label(self.frame, image=self.photo)
        self.bild_label.pack()

        # Button erstellen, um Fenster 1 zu öffnen
        self.button_1 = ttk.Button(self.frame, text="Tierübersicht", command=self.open_tieruebersicht, width=500)
        self.button_1.pack(pady=10)

        # Button erstellen, um Fenster 2 zu öffnen
        self.button_2 = ttk.Button(self.frame, text="Fenster 2", command=self.open_tieruebersicht, width=500)
        self.button_2.pack(pady=10)

        # Button erstellen, um Fenster 3 zu öffnen
        self.button_3 = ttk.Button(self.frame, text="Übersicht", command=self.open_uebersicht, width=500)
        self.button_3.pack(pady=10)

        # Button erstellen, um Fenster 4 zu öffnen
        self.button_4 = ttk.Button(self.frame, text="Einstellungen", command=self.open_einstellungen, width=500)
        self.button_4.pack(pady=10)

        # Button erstellen, der das Programm beendet, wenn man darauf klickt
        self.quit_button = ttk.Button(self.frame, text='Beenden', command=self.destroy, width=500)
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
        print("a")

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
