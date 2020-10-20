
import tkinter as tk
from tkinter.constants import HIDDEN, LEFT

HEIGHT = 100
WIDTH = 500


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


def box():
    text = entry_url.get()
    return str(text)


entry_url = tk.Entry(root)
entry_url.pack()

button = tk.Button(root, text='press', command=box)
button.pack()
# button2 = tk.Button(root, text='main', command=run_main)
# button2.pack()


root.mainloop()
