import tkinter as tk
from tkinter import ttk
import konstanten
import zoo
from Tieruebersicht import TierUebersichtFenster

# Hauptfenster erstellen
root = tk.Tk()
root.title("Hauptmenü")
root.geometry("500"+"x350")
root.iconbitmap("favicon-zoo.ico")


# Funktionen für die Menüpunkte erstellen
def open_window_1():
    # Fenster 1 öffnen Tierübersicht
    TierUebersichtFenster()


def open_window_2():
    # Fenster 2 öffnen Personalübersicht
    TierUebersichtFenster()


def open_window_3():
    # Fenster 3 öffnen Einstellungen
    TierUebersichtFenster()


def open_window_4():
    # Fenster 4 öffnen
    TierUebersichtFenster()


# Frame erstellen
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Button erstellen, um Fenster 1 zu öffnen
button_1 = ttk.Button(frame, text="Fenster 1 öffnen Tierübersicht", command=open_window_1, width=500)
button_1.pack(pady=10)

# Button erstellen, um Fenster 2 zu öffnen
button_2 = ttk.Button(frame, text="Fenster 2 öffnen Personalübersicht", command=open_window_2, width=500)
button_2.pack(pady=10)

# Button erstellen, um Fenster 3 zu öffnen
button_3 = ttk.Button(frame, text="Fenster 3 öffnen Einstellungen", command=open_window_3, width=500)
button_3.pack(pady=10)

# Button erstellen, um Fenster 4 zu öffnen
button_4 = ttk.Button(frame, text="Fenster 4 öffnen", command=open_window_4, width=500)
button_4.pack(pady=10)

# Button erstellen, der das Programm beendet, wenn man darauf klickt
quit_button = ttk.Button(frame, text='Beenden', command=root.destroy, width=500)
quit_button.pack(pady=10)

if konstanten.DARK_MODE:
    root.config(bg=konstanten.DARK_MODE_COLOR)
    frame.config(bg=konstanten.DARK_MODE_COLOR)
    button_1.config(bg=konstanten.DARK_MODE_COLOR)
    button_2.config(bg=konstanten.DARK_MODE_COLOR)
    button_3.config(bg=konstanten.DARK_MODE_COLOR)
    button_4.config(bg=konstanten.DARK_MODE_COLOR)
    quit_button.config(bg=konstanten.DARK_MODE_COLOR)

# Hauptfenster anzeigen
root.mainloop()
