import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Pillow Modul installieren:
# Erstens dieses: pip install --upgrade pip
# Zweitens dieses: pip install --upgrade Pillow
# -m pip install Pillow

root = tk.Tk()
root.title("Hauptfenster von deinem Zoo")
root.geometry("800x600")
root.minsize(width=200, height=100)
# root.maxsize(width=1000, height=1000)
# root.resizable(width=False, height=False)


# Root ist das Hautpfenster
label1 = ttk.Label(root, text="Willkommen in deinem Zoo")
label1.pack(side="top")

label2 = ttk.Label(root, text="Hier ist ein Känguruh für dich.")
label2.pack()

# image = Image.open("/icons/noun-kangaroo-1866921.png")

# label1.configure(text="Anderer Text")



label2 = ttk.Label(root, text="Weiterer Text")
label2.pack(side="top")

root.mainloop()

print("Gui wurde geschlossen")

