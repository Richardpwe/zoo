import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
# python -m pip install Pillow


# Root ist das Hautpfenster
root = tk.Tk()
root.title("Hauptfenster von deinem Zoo")
root.geometry("800x600")
# root.iconbitmap("myIcon.ico")
# root.minsize(width=200, height=100)
# root.maxsize(width=1000, height=1000)
# root.resizable(width=False, height=False)

# man kann grundsätzliches Aussehen über Themes erreichen
# style = ttk.Style()
# style.theme_use("clam")




label1 = ttk.Label(root, text="Willkommen in deinem Zoo", background="grey", padding=40, relief="sunken", justify="center")
label1.pack(side="top", fill="x")

# optionen fuers styling nachschauen:
# for item in label1.keys():
#     print(item, ": ", label1[item])

label2 = ttk.Label(root, text="Hier ist ein Känguruh für dich.")
label2.pack()


# methode definieren
#def kangurubild():
    #dirname = os.path.dirname(__file__)
    #filename = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')
    #image = Image.open(filename).resize((100, 100))
    #photo = ImageTk.PhotoImage(image)

    #label3 = ttk.Label(root, image = photo)
    #label3.pack()

# Mehtode callen
#kangurubild()

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')
image = Image.open(filename).resize((100, 100))
photo = ImageTk.PhotoImage(image)

label3 = ttk.Label(root, image=photo)
label3.pack(side="top")

label4 = ttk.Label(root, image=photo)
label4.pack(side="bottom")



# label1.configure(text="Anderer Text")



label2 = ttk.Label(root, text="Schön, dass du da bist!")
label2.pack(side="top")


# dynamische Textvariable auf Label, immer wieder set-bar mit .set-methode
text_variable = tk.StringVar()
text_variable.set("Label mit Dynamischer Textvariable")
labelKlick = ttk.Label(root, textvariable=text_variable, padding=10)
labelKlick.pack()

# Eingabefeld
def print_entry_input():
    print(entry1.get())

entry1 = ttk.Entry(root, width=30)
entry1.pack()

button_send = ttk.Button(root, text="Eingabe ausgeben", command=print_entry_input)
button_send.pack()

def delete_content():
    entry1.delete(0, tk.END)
    
button_delete = ttk.Button(root, text="Clear", command=delete_content)
button_delete.pack()



# Mehrere Kängurus



# Beenden-Button
quit_button = ttk.Button(root, text="Programm beenden", padding=5, command=root.destroy)
quit_button.pack(side="bottom")

# Button
def say_hello():
    print("Hallo, du hast du Button gedrückt.")

button1 = ttk.Button(root, text="Klick mich", padding=5, command=say_hello)
button1.pack(side="bottom")



root.mainloop()

print("Gui wurde geschlossen")

