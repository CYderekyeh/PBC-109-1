import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image


def func(event):
    print(event.x, event.y, sep=',')
    
    loc_icon.place(x=event.x, y=event.y)

# main windows
window = tk.Tk()
window.title('徐雨辰吃貨')

# 118 map
image1 = Image.open('C:\\Users\\user\\Desktop\\Derek\\NTU\\PBC\\Final project\\118map.jpg')
ntumap = ImageTk.PhotoImage(image1)


window.geometry('1000x581')
label1 = ttk.Label(window, image=ntumap)
label1.pack(side='left')

# locaiton icon

image2 = Image.open('C:\\Users\\user\\Desktop\\Derek\\NTU\\PBC\\Final project\\pic\\gps_PNG63.png')
image2 = image2.resize((20,20))
loc_image = ImageTk.PhotoImage(image2)
loc_icon = ttk.Label(window, image=loc_image)


window.bind("<Button-1>", func)

window.mainloop()
