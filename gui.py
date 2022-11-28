import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
# python -m pip install Pillow

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


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')
image = Image.open(filename).resize((100, 100))
photo = ImageTk.PhotoImage(image)

label3 = ttk.Label(root, image=photo)
label3.pack()

# label1.configure(text="Anderer Text")



label2 = ttk.Label(root, text="Schön, dass du da bist!")
label2.pack(side="top")

root.mainloop()

print("Gui wurde geschlossen")

