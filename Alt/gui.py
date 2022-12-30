import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance, ImageOps
import zoo
import konstanten

def tier_erstellen():
    tier = zoo.Tier("kaenguru", "Beuteltier", "Gras", "Peter", 1/1/2022, "maennlich")


class TierUebersichtFenster:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Tier Übersicht")
        self.window.geometry(str(konstanten.MAX_LABELS_PER_ROW)*100 + "x600")
        self.window.iconbitmap("favicon-zoo.ico")

        self.startzeile = 3
        self.startspalte = 1

        self.label_list = []

        self.label_kanguru_menge = tk.Label(self.window, text="Kangurus: 0")
        self.button_kanguru_add = tk.Button(self.window, text="Hinzufügen", command=self.kanguru_add)
        self.button_kanguru_remove = tk.Button(self.window, text="Entfernen", command=self.kanguru_remove)

        try:
            self.image = Image.open(konstanten.KANGAROO_PFAD)
            self.image = self.image.resize((100, 100))
            #if konstanten.DARK_MODE:  
            self.photo = ImageTk.PhotoImage(self.image)
        except FileNotFoundError:
            print("Bilddatei nicht gefunden")

        self.label_kanguru_menge.grid(row=1, column=3)
        self.button_kanguru_add.grid(row=1, column=1)
        self.button_kanguru_remove.grid(row=1, column=2)

        if isinstance(konstanten.TESTKONSTANTE, int) and konstanten.TESTKONSTANTE > 0:
            for i in range(konstanten.TESTKONSTANTE):
                self.kanguru_add()

        if konstanten.DARK_MODE:
            self.window.config(bg=konstanten.DARK_MODE_COLOR)
            self.label_kanguru_menge.config(bg=konstanten.DARK_MODE_COLOR)
            self.button_kanguru_add.config(bg=konstanten.DARK_MODE_COLOR)
            self.button_kanguru_remove.config(bg=konstanten.DARK_MODE_COLOR)
            self.label_kanguru_menge.config(fg='#FFFFFF')
            self.button_kanguru_add.config(fg='#FFFFFF')
            self.button_kanguru_remove.config(fg='#FFFFFF')

    def kanguru_add(self):
        if len(self.label_list) % konstanten.MAX_LABELS_PER_ROW == 0 and self.label_list != []:
            # Wenn das Maximum erreicht ist, in die nächste Zeile wechseln
            self.startzeile += 1
            self.startspalte = 1

        if konstanten.DARK_MODE:
            label = tk.Label(self.window, image=self.photo, bg=konstanten.DARK_MODE_COLOR)
        else:
            label = tk.Label(self.window, image=self.photo)
        label.grid(row=self.startzeile, column=self.startspalte)
        
        self.startspalte += 1
        self.label_list.append(label)
        self.label_kanguru_menge["text"] = "Kangurus: " + str(len(self.label_list))
        print("Kanguru wurde hinzugefügt")

    def kanguru_remove(self):
        if self.label_list:
            self.label_list[-1].grid_forget()
            del self.label_list[-1]
            self.startspalte -= 1
            if self.startspalte == 0:
                self.startspalte = konstanten.MAX_LABELS_PER_ROW
                self.startzeile -= 1
        self.label_kanguru_menge["text"] = "Kangurus: " + str(len(self.label_list))
        print("Kanguru wurde enfernt")

if __name__ == "__main__":
    root = tk.Tk()
    tier_uebersicht_fenster = TierUebersichtFenster(root)
    root.mainloop()
