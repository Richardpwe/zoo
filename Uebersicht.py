import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
import zoo
import konstanten
import pickle
import os


class UebersichtFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Übersicht")
        self.geometry('500x250')
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")

        self.button_zurueck_home = ttk.Button(self, text="Home", command=self.back_home)
        self.label_anzahl_tiere = ttk.Label(self, text="Gesamtanzahl Tiere:")
        anzahl_tiere = 10 #zoo.Zoo.get_tiere_anzahl(self)
        self.label_anzahl_tiere_wert = ttk.Label(self, text=anzahl_tiere)
        self.label_anzahl_personal = ttk.Label(self, text="Gesamtanzahl Mitarbeiter:")
        # self.label_anzahl_personal_wert = ttk.Label(self, text=zoo.Zoo.get_personal_anzahl)

        self.diagram = tk.StringVar()
        diagramme = ["Futterbedarf", "Geburtsdaten", "Anzeige..."]
        self.entry_diagram_auswahl = ttk.OptionMenu(self, self.diagram, 'Anzeige...', *diagramme)

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.button_zurueck_home.grid(row=0, column=0)
        self.label_anzahl_tiere.grid(row=1, column=3)
        self.label_anzahl_tiere_wert.grid(row=1, column=4)
        self.entry_diagram_auswahl.grid(row=3, column=0)
        # self.label_anzahl_personal.grid(row=2,column=3)

    #def ausgabe_geburtsdaten(self):


    def back_home(self):
        from Hauptmenue import Hauptmenue
        self.destroy()
        Hauptmenue()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = UebersichtFenster()
    fenster.run()
