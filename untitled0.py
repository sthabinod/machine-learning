import tkinter
from tkinter import *
import finalspider


top = tkinter.Tk()
top.geometry("500x500")
top.title("Weather forecasting using machine learning")
top.configure(background='#9FB6CD')

#adding button
button = tkinter.Button(top,height=2,width=10,text="Submit")
button.pack()
button.place(x=225,y=215)

#i/p part
label_1 = Label(top, text="INPUT DATA ", width=20, font=("bold", 15),bg="#9FB6CD")
label_1.place(x=150, y=10)

label_2 = Label(top, text="Date : ", width=10, font=("bold", 15),bg="#9FB6CD")
label_2.place(x=10, y=50)
E2 = Entry(top, bd=5)
E2.place(x=200, y=50)

label_3 = Label(top, text="Humidity : ", width=10, font=("bold", 15),bg="#9FB6CD")
label_3.place(x=24, y=85)
E3 = Entry(top, bd=5)
E3.place(x=200, y=85)

label_4 = Label(top, text="Dewpoint : ", width=10, font=("bold", 15),bg="#9FB6CD")
label_4.place(x=27, y=120)
E4 = Entry(top, bd=5)
E4.place(x=200, y=120)

label_5 = Label(top, text="Precipitation : ", width=15, font=("bold", 15),bg="#9FB6CD")
label_5.place(x=13, y=155)
E5 = Entry(top, bd=5)
E5.place(x=200, y=155)

#o/p part
label_6 = Label(top, text="OUTPUT DATA ", width=20, font=("bold", 15),bg="#9FB6CD")
label_6.place(x=150, y=285)

label_7 = Label(top, text="Temperature : ", width=15, font=("bold", 15),bg="#9FB6CD")
label_7.place(x=13, y=325)
E7 = Entry(top, bd=5)
E7.place(x=200, y=325)

label_8 = Label(top, text="Pressure : ", width=10, font=("bold", 15),bg="#9FB6CD")
label_8.place(x=27, y=360)
E8 = Entry(top, bd=5)
E8.place(x=200, y=360)

label_9 = Label(top, text="Description : ", width=10, font=("bold", 15),bg="#9FB6CD")
label_9.place(x=35, y=395)
E9 = Entry(top, bd=5)
E9.place(x=200, y=395)

#function
def sub() -> None:
    my_dic1= {'Humidity_Max':E3.get(),'Dew_Point_Max':E4.get()}
    my_dic= finalspider.get_input(my_dic1)
    print(my_dic['temperature'],my_dic['pressure'])
    #E7["text"]=my_dic['temperature']
    #E8["text"] = my_dic['pressure']

button.config(command=sub)

top.mainloop()