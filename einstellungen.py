import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
import zoo
import konstanten
import pickle
import os


class EinstellungenFenster(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.title("Einstellungen")
        self.geometry('500x250')
        self.iconbitmap("favicon-zoo.ico")
        self.parent = parent

        self.button_zurueck_home = ttk.Button(self, text="Home", command=self.back_home)
        self.button_zoo_laden = ttk.Button(self, text="Zoo laden...", command=self.zoo_laden)
        self.button_zoo_exportieren = ttk.Button(self, text="Zoo exportieren...", command=self.zoo_exportieren())

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.button_zurueck_home.grid(row=0, column=0)
        self.button_zoo_laden.grid(row=0, column=1)
        self.button_zoo_exportieren.grid(row=0, column=2)

    def back_home(self):
        self.destroy()

    def zoo_laden(self):
        file_path = filedialog.askopenfilename()
        if os.path.exists(file_path):
            with open(file_path, 'rb') as datei:
                neuer_zoo = pickle.load(datei)
        print("Du hättest den Zoo erfolgreich geladen, falls Nico nicht so unfähig wäre.")

    def zoo_exportieren(self):
        dateipfad = filedialog.askopenfilename()
        export_zoo = zoo.neuer_zoo
        with open(os.path.join(dateipfad, "zooExport.pickle"), "w") as file:
            pickle.dump(export_zoo, file)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = EinstellungenFenster()
    fenster.run()
