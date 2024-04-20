import flower as fl
import drawTruck as tr
import drawSuv as sv
import drawCar as cr
import turtle
from turtle import Screen
from tkinter import *
import random


def open_suv_window():
    turtle.clearscreen()
    fl.main()
    sv.main()


def open_truck_window():
    # Clear existing drawings
    turtle.clearscreen()
    # Draw the truck
    fl.main()
    tr.main()  # main() in truck.py contains the code to draw the truck

def open_car_window():
    turtle.clearscreen()
    fl.main()
    cr.main()



def main():
    screen = Screen()
    # screen.setup(width=800, height=700)
    # fl.main()

    # drawcar()
    canvas = screen.getcanvas()

    button_suv = Button(canvas.master,text="SUV",width=5,height=1,bg="red",fg="white",font=("Arial",12) ,command=open_suv_window)
    button_car = Button(canvas.master,text="CAR",width=5,height=1,bg="blue",fg="white",font=("Arial",12), command=open_car_window)
    button_truck = Button(canvas.master,text="TRUCK",width=5,height=1,bg="green",fg="white",font=("Arial",12), command=open_truck_window)

    button_car.pack()
    button_car.place(x=90, y=200)

    button_suv.pack()
    button_suv.place(x=90, y=250)  # place the button anywhere on the screen

    button_truck.pack()
    button_truck.place(x=90, y=300)

    screen.mainloop()

main()
# mainloop()