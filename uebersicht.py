import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
import zoo
import konstanten
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date
import pickle
import os


class UebersichtFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Übersicht")
        self.geometry('1200x700')
        # Fenster in die Mitte des Bildschirms
        self.geometry(
            "+{}+{}".format(int(self.winfo_screenwidth() / 2 - 200), int(self.winfo_screenheight() / 2 - 150)))
        self.iconbitmap("favicon-zoo.ico")

        self.button_zurueck_home = ttk.Button(self, text="Home", command=self.back_home)
        self.label_anzahl_tiere = ttk.Label(self, text="Gesamtanzahl Tiere:")
        self.label_anzahl_tiere_wert = ttk.Label(self, text=zoo.neuer_zoo.get_tiere_anzahl())
        self.label_anzahl_personal = ttk.Label(self, text="Gesamtanzahl Mitarbeiter:")
        self.label_anzahl_personal_wert = ttk.Label(self, text=zoo.neuer_zoo.get_personal_anzahl())
        self.diagram_frame = ttk.Frame(self)
        grafik = plt.figure()
        self.canvas = FigureCanvasTkAgg(grafik, master=self)

        combo = ttk.Combobox(self)
        combo['state'] = 'readonly'
        combo['values'] = ['Auswahl...', 'Geburtsdaten Tiere', 'Geschlechter Tiere']
        # ,'Geburtsdaten Personal', 'Futterbedarf', 'Kosten pro Tierart', 'Futterkosten pro Tag', 'Wie alt ist der Zoo',
        # 'Wie alt ist sind die Tiere', 'Durchschnittsalter der Belegschaft', 'Personalkosten',
        # 'Tierbetreeungsschlüssel AnzahlTiere/AnzahlPfleger',
        combo.current(0)  # Setze die Standardauswahl auf "Option 1"

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.button_zurueck_home.grid(row=0, column=0)
        self.label_anzahl_tiere.grid(row=1, column=3)
        self.label_anzahl_tiere_wert.grid(row=1, column=4)
        self.diagram_frame.grid(row=4, column=1)

        combo.grid(row=3, column=0)
        self.label_anzahl_personal.grid(row=2, column=3)
        self.ausgabe_auswahl()

        # Erstelle eine Funktion zum Bearbeiten der Auswahl in der Combobox
        def combo_selection(event):
            selection = combo.get()  # Lese die aktuelle Auswahl aus der Combobox
            if selection == 'Auswahl...':
                # Zeige leeres Rechteck
                print("Auswahl...")
                self.ausgabe_auswahl()
            elif selection == 'Geburtsdaten Tiere':
                # Zeige Geburtsdaten Tiere an
                print("Geburtsdaten Tiere")
                self.ausgabe_geburtsdaten()
            elif selection == 'Geschlechter Tiere':
                self.ausgabe_geschlechter_tiere()
                # Zeige Geschlechterverteilung an
                print("Geschlechterverteilung")
            # elif selection == 'Geburtsdaten Personal':
            # Zeige Geburtsdaten Personal an
            # print("Geburtsdaten Personal")
            # elif selection == 'Futterbedarf':
            # Zeige Futterbedarf an
            # print("Futterbedarf")

        # Binde die Funktion an das "comboboxselected" -Ereignis
        combo.bind("<<ComboboxSelected>>", combo_selection)

    def renew_diagram_frame(self):
        # Frame löschen und neu hinzufügen.
        self.diagram_frame.destroy()
        self.diagram_frame = tk.Frame(self)
        self.diagram_frame.grid(row=4, column=1)
        print("Frame für Grafik erneuert.")

    def ausgabe_auswahl(self):
        self.renew_diagram_frame()
        # Leere Grafik, Canvas in den Frame packen
        grafik = plt.figure()
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(grafik, master=self.diagram_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def update_geburtsdaten_liste(self):
        print("Liste von Geburtsdaten geupdatet")
        tiere = zoo.neuer_zoo.get_tiere()
        geburtstage_tiere = []
        for tier in tiere:
            geburtstage_tiere.append(tier.get_geburtsdatum())
        print(geburtstage_tiere)
        return geburtstage_tiere

    def ausgabe_geburtsdaten(self):
        self.renew_diagram_frame()

        # Erstelle das Histogramm-Figure
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Extrahiere die Jahre aus den Geburtsdaten und speichere sie in einer Liste
        geburtstage_tiere = self.update_geburtsdaten_liste()
        years = []
        for datum in geburtstage_tiere:
            years.append(datum.year)
        print(years)

        # Erstelle das Histogramm
        ax.hist(years, bins=50)

        # Füge eine Beschriftung hinzu
        ax.set_xlabel('Jahr')
        ax.set_ylabel('Anzahl der Geburten')

        # Erstelle ein Canvas-Element und ein Frame, um das Histogramm anzuzeigen
        self.canvas.get_tk_widget().pack_forget()
        canvas = FigureCanvasTkAgg(fig, master=self.diagram_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def ausgabe_geschlechter_tiere(self):
        self.renew_diagram_frame()
        self.ausgabe_auswahl()
        # weil ansonsten die Grafik nicht korrekt geladen wird, falls die Geburtsdaten vorher ausgegeben wurden

        tiere = zoo.neuer_zoo.get_tiere()
        maennliche_tiere = 0
        weibliche_tiere = 0
        unbekannte_tiere = 0
        for tier in tiere:
            if tier.get_geschlecht() == "Weiblich":
                weibliche_tiere += 1
                print("w" + str(weibliche_tiere))
            elif tier.get_geschlecht() == "Männlich":
                maennliche_tiere += 1
                print("m" + str(maennliche_tiere))
            elif tier.get_geschlecht() == "Unbekannt":
                unbekannte_tiere += 1
            else:
                print("else")

        # Definieren der x- und y-Werte der Säulen
        beschriftungen = [1, 2, 3]

        werte = [maennliche_tiere, weibliche_tiere, unbekannte_tiere]

        # Erstellen der Grafik mit den Säulen
        plt.bar(beschriftungen, werte)

        # Setzen der x-Achsenbeschriftungen
        plt.xticks(beschriftungen, ["Männlich", "Weiblich", "Unbekannt"])
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.diagram_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def back_home(self):
        from hauptmenue import Hauptmenue
        self.destroy()
        Hauptmenue()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = UebersichtFenster()
    fenster.run()
