import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
import zoo
import konstanten
import pickle
import os


class EinstellungenFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Einstellungen")
        self.geometry('300x150')
        self.resizable(width=False, height=False)
        # Fenster in die Mitte des Bildschirms
        self.geometry("+{}+{}".format(int(self.winfo_screenwidth()/2-200), int(self.winfo_screenheight()/2-150)))
        self.iconbitmap("favicon-zoo.ico")

        self.button_zurueck_home = ttk.Button(self, text="Home", command=self.back_home)
        self.button_zoo_laden = ttk.Button(self, text="Zoo laden ...", command=self.zoo_laden)
        self.button_zoo_exportieren = ttk.Button(self, text="Zoo exportieren ...", command=self.zoo_exportieren)
        self.button_zoo_bearbeiten = ttk.Button(self, text="Zoo Daten Ändern", command=self.back_home)

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.button_zurueck_home.grid(row=0, column=0)
        self.button_zoo_laden.grid(row=1, column=0)
        self.button_zoo_exportieren.grid(row=2, column=0)
        self.button_zoo_bearbeiten.grid(row=3, column=0)

    def back_home(self):
        from hauptmenue import Hauptmenue
        self.destroy()
        Hauptmenue()

    def zoo_laden(self):
        file_path = filedialog.askopenfilename()
        if os.path.exists(file_path):
            with open(file_path, 'rb') as datei:
                neuer_zoo = pickle.load(datei)
        print("Du hast einen Zoo geladen.")

    def zoo_exportieren(self):
        dateipfad = filedialog.askdirectory()
        export_zoo = zoo.neuer_zoo
        with open(os.path.join(dateipfad, "zooExport.pickle"), "wb") as file:
            pickle.dump(export_zoo, file)
        print("Du hast einen Zoo exportiert.")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = EinstellungenFenster()
    fenster.run()
