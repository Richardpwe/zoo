import tkinter as tk
from tkinter import ttk
import konstanten


class PersonalUebersichtFenster(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tier Übersicht")
        self.geometry("420" + "x500")
        # self.minsize(width=500, height=500)
        # Fenster in die Mitte des Bildschirms
        self.geometry("+{}+{}".format(int(self.winfo_screenwidth() / 2-200), int(self.winfo_screenheight() / 2-150)))
        self.iconbitmap("favicon-zoo.ico")

        self.button_frame = ttk.Frame(self)
        self.button_zurueck_home = ttk.Button(self.button_frame, text="Home", command=self.back_home)

        self.button_frame.grid(column=0, row=0)
        self.button_zurueck_home.grid(row=0, column=0)

        if konstanten.DARK_MODE:
            self.config(bg=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.configure(background=konstanten.DARK_MODE_COLOR)
            # self.button_zurueck_home.config(fg='#FFFFFF')

        self.seperator = ttk.Separator(self, orient='horizontal')
        self.seperator.grid(row=1, column=0, sticky='ew')

        self.tier_frame = ttk.Frame(self)
        self.tier_frame.grid(row=2, column=0)

    def back_home(self):
        from hauptmenue import Hauptmenue
        self.destroy()
        Hauptmenue()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    fenster = PersonalUebersichtFenster()
    fenster.run()
