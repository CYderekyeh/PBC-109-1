import tkinter as tk
from tkinter import messagebox as mb
from PIL import ImageTk,Image
import pandas as pd


# main windows
window = tk.Tk()
window.title('徐雨辰吃貨')
window.geometry('1000x581')


# import 118 map & location icon image on canvas
image1 = Image.open('C:\\Users\\user\\Desktop\\Derek\\NTU\\PBC\\Final project\\118map.jpg')
ntumap = ImageTk.PhotoImage(image1)

loc_image = Image.open('C:\\Users\\user\\Desktop\\Derek\\NTU\\PBC\\Final project\\pic\\gps_PNG63.png')
loc_icon = ImageTk.PhotoImage(image=loc_image.resize((30, 30)))

canvas = tk.Canvas(window, bg='white', height=581, width=1000)
canvas.create_image(420, 295, image=ntumap)
canvas.pack()


class  restaurant:
    
    def __init__(self, name, review, price, kind, style, coordinate, image):
        
        self.name = name
        
        self.review = review
        
        self.price = price
        
        self.kind = kind
        
        self.style = style 
    
        self.coordinate = coordinate
        
        self.image= image

        self.button = self.add_button()

     
    def add_button(self):
        
        button_loc = tk.Button(canvas, image=loc_icon, command=self.show_restaurant)
        
        return button_loc

            
        
    def show_restaurant(self):
        
        global rest_image, rest_label
        
        new_window = tk.Toplevel(window)
            
        new_window.geometry('750x500')

        rest_image = ImageTk.PhotoImage(Image.open(self.image).resize((750,500)))
            
        rest_label = tk.Label(new_window, image=rest_image)
        
        rest_label.pack()
    

def order_with_price(alist):
    category = []
    item = ['0-100', '100-200', '200-300', '300以上']
    for i in range(4):
        category.append([priceVar_list[i],item[i]])
    price = []
    for i in range(4):
        if category[i][0].get() == 1:
            price.append(category[i][1])  # 先把符合的條件找出來
    
    selected_restaurant = []
    for item in price:  # 再一個一個餐廳做篩選
        for res in alist:
            if len(res.price) == 1:
                if item == '300以上':
                    selected_restaurant.append(res)
            else:
                if item == '0-100':
                    if int(res.price[1]) <= 100 :
                        selected_restaurant.append(res)
                if item == '100-200':
                    if int(res.price[1]) <= 200 and int(res.price[0]) >= 100:
                        selected_restaurant.append(res)
                if item == '200-300':
                    if int(res.price[1]) <= 300 and int(res.price[0]) >= 200:
                        selected_restaurant.append(res)
                if item == '300以上':
                    if  int(res.price[0]) >= 300:
                        selected_restaurant.append(res)

    return selected_restaurant



def order_with_kind(alist):
    category = []
    item = ['早餐', '中餐', '晚餐', '下午茶', '點心', '飲料']
    for i in range(6):
        category.append([kindVar_list[i], item[i]])
    kind = []
    for i in range(6):
        if category[i][0].get() == 1:
            kind.append(category[i][1])  # 先把符合的條件找出來

    selected_restaurant = []
    for item in kind:   
        for res in alist:  # 再一個一個餐廳做篩選
            if item in res.kind:
                if res not in selected_restaurant:
                    selected_restaurant.append(res)
    return selected_restaurant



def order_with_style(alist):
    category = []
    item = ['台式', '中式', '西式', '泰式', '馬來式', '韓式', '義式']
    for i in range(7):
        category.append([styleVar_list[i], item[i]])
    style = []
    for i in range(6):
        if category[i][0].get() == 1:
            style.append(category[i][1])  # 先把符合的條件找出來

    selected_restaurant = []
    for item in style:   
        for res in alist:  # 再一個一個餐廳做篩選
            if item in res.style:
                if res not in selected_restaurant:
                    selected_restaurant.append(res)
    return selected_restaurant



def ordering(alist):
    
    ordered_list = alist
    
    ordered_list = order_with_price(ordered_list)
    
    ordered_list = order_with_kind(ordered_list)
    
    ordered_list = order_with_style(ordered_list)
    
    return ordered_list



def running_program():
    
    global  x_coordinate, y_coordinate
    
    ordered_list = ordering(all_restaurants)
    
    ordered_list = sorted(ordered_list, key=lambda x: x.review, reverse=True)
    
    if len(ordered_list) == 0:  # show no_match
        mb.showerror("Error", "NO_MATCH!")
    

    for i,res in enumerate(ordered_list):
        if i >= 3:
            break
        x_coordinate = int(res.coordinate[0]) - 15
        y_coordinate = int(res.coordinate[1]) - 15
        button = res.button
        button.place(x=x_coordinate, y=y_coordinate)


# ______________________________seperating line_____________________________
# input of restaurant file

data = pd.read_excel('C:\\Users\\user\\Downloads\\範圍內餐廳(new).xlsx')

list_name = data['店名']
oldlist_price = data['價位']
list_price = []
list_review = data['評價']
oldlist_style = data['風格']
list_style = []
oldlist_kind = data['種類']
list_kind = []
oldlist_coordinate = data['座標']
list_coordinate = []
oldlist_image = data['圖檔']
list_image = []

for i,price in enumerate(oldlist_price):
    price = str(price)
    list_price.append(price.split('-'))
for i,style in enumerate(oldlist_style):
    style_newlisti = style.split(',')
    list_style.append(style_newlisti)
for i,kind in enumerate(oldlist_kind):
    kind_newlisti = kind.split(',')
    list_kind.append(kind_newlisti)
for i,coordinate in enumerate(oldlist_coordinate):
    coordinate_newlisti = str(coordinate).split(',')
    list_coordinate.append(coordinate_newlisti)
for i,image in enumerate(oldlist_image):
    image = image.replace('//', '////') 
    list_image.append(image)


all_restaurants = []

for i in range(len(list_name)):
    name = list_name[i]
    price = list_price[i]
    review = list_review[i]
    style = list_style[i]
    kind = list_kind[i]
    coordinate = list_coordinate[i]
    image = list_image[i]
    
    restauranti = restaurant(name, review, price, kind, style, coordinate, image)
    all_restaurants.append(restauranti)


# ______________________________seperating line_____________________________
# GUI 

# menu button 

price = tk.Menubutton(window, text='價格', font=('標楷體', '16'), relief='raised', 
                        bg='white', activebackground='yellow')
kind = tk.Menubutton(window, text='種類',  font=('標楷體', '16'), relief='raised', 
                        bg='white', activebackground='yellow')
style = tk.Menubutton(window, text='風格',  font=('標楷體', '16'), relief='raised', 
                        bg='white', activebackground='yellow')

catlog_price = tk.Menu(price, tearoff=0)
catlog_kind = tk.Menu(kind, tearoff=0)
catlog_style = tk.Menu(style, tearoff=0)

priceVar_list = []
kindVar_list = []
styleVar_list = []

for i,text in enumerate(['0-100', '100-200', '200-300', '300以上']):
    priceVar = tk.IntVar()
    priceVar_list.append(priceVar)
    catlog_price.add_checkbutton(label=text, variable=priceVar, onvalue=1, offvalue=0)

for i,text in enumerate(['早餐', '中餐', '晚餐', '下午茶', '點心', '飲料']):
    kindVar = tk.IntVar()
    kindVar_list.append(kindVar)
    catlog_kind.add_checkbutton(label=text, variable=kindVar, onvalue=1, offvalue=0)

for i,text in enumerate(['台式', '中式', '西式', '泰式', '馬來式', '韓式', '義式']):
    styleVar = tk.IntVar()
    styleVar_list.append(styleVar)
    catlog_style.add_checkbutton(label=text, variable=styleVar, onvalue=1, offvalue=0)


price.config(menu=catlog_price)
kind.config(menu=catlog_kind)
style.config(menu=catlog_style)



price.place(x=885, y=100)
kind.place(x=885, y=220)
style.place(x=885, y=340)


# confirm button 

confirm_button = tk.Button(window, text='確認', font=('華文行楷', '20'), bg='white', activebackground='red',
                           fg='black', relief='raised', command=running_program)
confirm_button.place(x=875, y=500)

title = tk.Label(window, text='今晚想來點什麼？', font=('標楷體', '14'), fg='black', bg='white')
title.place(x=835, y=50)



window.mainloop()