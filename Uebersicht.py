import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
import zoo
import konstanten
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        self.label_anzahl_tiere_wert = ttk.Label(self, text=zoo.neuer_zoo.get_tiere_anzahl())
        self.label_anzahl_personal = ttk.Label(self, text="Gesamtanzahl Mitarbeiter:")
        self.label_anzahl_personal_wert = ttk.Label(self, text=zoo.neuer_zoo.get_personal_anzahl())

        combo = ttk.Combobox(self)
        combo['values'] = ['Geburtsdaten Tiere', 'Geburtsdaten Personal', 'Futterbedarf', 'Geschlechterverteilung Tiere']
        combo.current(0)  # Setze die Standardauswahl auf "Option 1"

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.button_zurueck_home.grid(row=0, column=0)
        self.label_anzahl_tiere.grid(row=1, column=3)
        self.label_anzahl_tiere_wert.grid(row=1, column=4)
        combo.grid(row=3, column=0)
        self.label_anzahl_personal.grid(row=2, column=3)

        # Erstelle eine Funktion zum Bearbeiten der Auswahl in der Combobox
        def combo_selection(event):
            selection = combo.get()  # Lese die aktuelle Auswahl aus der Combobox
            if selection == 'Geburtsdaten Tiere':
                # Zeige Geburtsdaten Tiere an
                print("Geburtsdaten Tiere")
                self.ausgabe_geburtsdaten()
            elif selection == 'Geburtsdaten Personal':
                # Zeige Geburtsdaten Personal an
                print("Geburtsdaten Personal")
            elif selection == 'Futterbedarf':
                # Zeige Futterbedarf an
                print("Futterbedarf")
            elif selection == 'Geschlechterverteilung Tiere':
                # Zeige Geschlechterverteilung an
                print("Geschlechterverteilung")

        # Binde die Funktion an das "comboboxselected" -Ereignis
        combo.bind("<<ComboboxSelected>>", combo_selection)


    def ausgabe_geburtsdaten(self):
        # Erstelle das Histogramm-Figure
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Liste von Geburtsdaten im Format (Jahr, Monat, Tag)
        birthdays = [
            (1980, 1, 1),
            (1985, 3, 15),
            (1990, 9, 20),
            (1995, 4, 5),
            (2000, 6, 30),
            (2005, 8, 15),
            (2010, 12, 31),
        ]

        # Extrahiere die Jahre aus den Geburtsdaten und speichere sie in einer Liste
        years = [year for (year, month, day) in birthdays]

        # Erstelle das Histogramm
        ax.hist(years, bins=50)

        # Füge eine Beschriftung hinzu
        ax.set_xlabel('Jahr')
        ax.set_ylabel('Anzahl der Geburten')

        # Erstelle ein Canvas-Element, um das Histogramm anzuzeigen
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=5)

    def back_home(self):
        from Hauptmenue import Hauptmenue
        self.destroy()
        Hauptmenue()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = UebersichtFenster()
    fenster.run()
