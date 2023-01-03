import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

# Erstellen Sie das Hauptfenster
root = tk.Tk()

# Erstellen Sie ein neues Bild mit den Abmessungen 100x50 und der Hintergrundfarbe blau
image = Image.new("RGB", (100, 50), "#000000") #grundform

# Erstellen Sie einen Zeichenkontext für das Bild
draw = ImageDraw.Draw(image)

# Zeichnen Sie ein Rechteck mit abgerundeten Ecken auf das Bild
draw.rounded_rectangle((0, 0, 100, 50), fill="#00ffff", outline="#ffffff", radius=20) #abgerundet oben drauf

# Speichern Sie das Bild als JPEG-Datei
# draw.save("rounded_corners.jpg")

# Konvertieren Sie das Bild in ein PhotoImage, das von tkinter verwendet werden kann
draw = ImageTk.PhotoImage(image)

# Erstellen Sie einen Button mit dem Bild als Hintergrund
button2 = ttk.Button(root, image=draw, text="Klick mich")

# Erstellen Sie einen neuen Stil namens "Custom.TButton"
style = ttk.Style()
style.configure("Custom.TButton", background="#555555", foreground="#000000", font="Arial 16")

# Erstellen Sie einen Button mit dem Stil "Custom.TButton"
button = ttk.Button(root, text="Klick mich", style="Custom.TButton")

# Packen Sie den Button in das Hauptfenster
button.pack(padx=30, pady=30)
button2.pack(padx=30, pady=30)

# Starten Sie den Hauptloop
root.mainloop()