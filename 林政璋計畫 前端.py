import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image

window = tk.Tk()
window.title('林政璋吃甚麼')
window.geometry('1000x800')
window.configure()
image2 =Image.open('')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
app.geometry('%dx%d+0+0' % (w,h))


window.mainloop()