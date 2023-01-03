import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import zoo
import konstanten


class EinstellungenFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Einstellungen")
        self.geometry('500x250')
        self.iconbitmap("favicon-zoo.ico")

        self.button_zurueck_home = ttk.Button(self, text="Home", command=self.back_home)
        self.button_zoo_laden = ttk.Button(self, text="Zoo laden...", command=self.zoo_laden)
        self.button_zoo_exportieren = ttk.Button(self, text="Zoo exportieren...", command=self.zoo_exportieren)

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
        #inhalt aus zoo.pickle mit dem zoo konstruktor laden
        print("Du hättest den Zoo erfolgreich geladen, falls Nico nicht so unfähig wäre.")

    def zoo_exportieren(self):
        #das Objekt zoo in die zoo.pickle reintun
        print("Du hättest den Zoo erfolgreich exportiert, falls Nico nicht so unfähig wäre.")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = EinstellungenFenster()
    fenster.run()
