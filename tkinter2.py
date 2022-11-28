from tkinter import *
import os


root = Tk()
root.title("Tk Example")
root.minsize(200, 200)  # width, height
root.geometry("300x300+50+50")

# Create Label in our window
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'icons', 'noun-kangaroo-1866921.png')
image = PhotoImage(file=filename)
#resize_image = image.resize((100, 100))
img = Label(root, image=image)
img.pack()
root.mainloop()