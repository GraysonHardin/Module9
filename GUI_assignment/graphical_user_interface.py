"""
Program: graphical_user_interface.py
Author: Grayson Hardin
Last date modified: 10/26/2020

This program opens a GUI page with some labels and clickable buttons.
"""
import tkinter


def on_breakfast_pick():
    label.config(text="Your favorite is breakfast!")


def on_second_breakfast_pick():
    label.config(text="Your favorite is second breakfast!")


def on_lunch_pick():
    label.config(text="Your favorite is lunch!")


def on_dinner_pick():
    label.config(text="Your favorite is dinner!")


m = tkinter.Tk()
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)

var1 = tkinter.IntVar()
tkinter.Checkbutton(m, text='Breakfast', variable=var1, command=on_breakfast_pick).grid(row=1)

var2 = tkinter.IntVar()
tkinter.Checkbutton(m, text='Second Breakfast', variable=var2, command=on_second_breakfast_pick).grid(row=2)

var3 = tkinter.IntVar()
tkinter.Checkbutton(m, text='Lunch', variable=var3, command=on_lunch_pick).grid(row=3)

var4 = tkinter.IntVar()
tkinter.Checkbutton(m, text='Dinner', variable=var4, command=on_dinner_pick).grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=50, command=m.destroy)
exit_button.grid(row=6)

m.mainloop()
