""" # traffic lights - Autimatic Control

#package

import tkinter as tk 
from tkinter import Canvas
from time import sleep

play =tk.Tk()
play.title("Traffic Lights - Manual Control")
play.geometry("300x600")
play.configure(bg='Light blue')

# Function to switch light colors
def red():
    c1.create_oval(110,110,20,20, fill="red",outline="white",width=3)
    c2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    c3.create_oval(110,110,20,20, fill="white",outline="white",width=3)

def yellow():
    c1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    c2.create_oval(110,110,20,20, fill="yellow",outline="white",width=3)
    c3.create_oval(110,110,20,20, fill="white",outline="white",width=3)

def green():
    c1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    c2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    c3.create_oval(110,110,20,20, fill="green",outline="white",width=3)

def counter(data):
    if data > 0:
        data = data -1
        intervals(data)

def start():
    global count
    count = 25
    counter (count)

def intervals(c):
    if c> 15:
        red()
        timerData.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    elif c > 10 and c<=15:
        yellow()
        timerData.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    elif c >0 and c <= 10:
        green()
        timerData.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    elif c==0:
        red()
        timerData.config(text=c)
        play.update()
        sleep(1)
        count = 25
        counter(count) 

# Create a canvas for the traffic light
canvas = tk.Canvas(play, width=100, height=300, bg="black")
canvas.grid(row=0, column=0, columnspan=3)

# Create buttons to control the lights
red_button = tk.Button(play, text="Red", command=red, bg="red")
red_button.grid(row=8, column=0)

yellow_button = tk.Button(play, text="Yellow", command=yellow, bg="yellow")
yellow_button.grid(row=8, column=1)

green_button = tk.Button(play, text="Green", command=green, bg="green")
green_button.grid(row=8, column=2)

Start_button = tk.Button(play, text="Start", command=start, bg="gray",width = 10, height = 1)
Start_button.place(x=100, y=480)

# Create a canvas for the traffic light
c1 = Canvas(play, width = 130, height = 120, bg='black')
c1.place(x=80, y=50)
c2 = Canvas(play, width = 130, height = 120, bg='black')
c2.place(x=80, y=170)
c3 = Canvas(play, width = 130, height = 120, bg='black')
c3.place(x=80, y=290)

timerData = tk.Label(play,font=('calibri',30,'bold'), bg='black', fg='red')
timerData.place(x=220,y=410)

play.mainloop() """

import tkinter as tk
from tkinter import Canvas
from time import sleep

play = tk.Tk()
play.title("Traffic Lights - 3 Systems")
play.geometry("600x600")
play.configure(bg='Light blue')

# Function to switch light colors for traffic system 1
def update_traffic_system_1(c):
    if c > 25:
        c1_1.create_oval(110,110,20,20, fill="red",outline="white",width=3)
        c2_1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c3_1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    elif c > 20:
        c1_1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c2_1.create_oval(110,110,20,20, fill="yellow",outline="white",width=3)
        c3_1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    else:
        c1_1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c2_1.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c3_1.create_oval(110,110,20,20, fill="green",outline="white",width=3)

# Function to switch light colors for traffic system 2
def update_traffic_system_2(c):
    if c > 25:
        c1_2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c2_2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c3_2.create_oval(110,110,20,20, fill="green",outline="white",width=3)
    elif c > 5 and c<=20:
        c1_2.create_oval(110,110,20,20, fill="red",outline="white",width=3)
        c2_2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c3_2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    elif c <=5:
        c1_2.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c2_2.create_oval(110,110,20,20, fill="yellow",outline="white",width=3)
        c3_2.create_oval(110,110,20,20, fill="white",outline="white",width=3)

# Function to switch light colors for traffic system 3
def update_traffic_system_3(c):
    if c > 25:
        c1_3.create_oval(110,110,20,20, fill="red",outline="white",width=3)
        c2_3.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c3_3.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    elif c > 20:
        c1_3.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c2_3.create_oval(110,110,20,20, fill="yellow",outline="white",width=3)
        c3_3.create_oval(110,110,20,20, fill="white",outline="white",width=3)
    else:
        c1_3.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c2_3.create_oval(110,110,20,20, fill="white",outline="white",width=3)
        c3_3.create_oval(110,110,20,20, fill="green",outline="white",width=3)

def counter(data):
    if data > 0:
        data -= 1
        intervals(data)

def start():
    global count
    count = 45
    counter(count)

def intervals(c):
    update_traffic_system_1(c)
    update_traffic_system_2(c)
    update_traffic_system_3(c)
    timerData_1.config(text=c)
    timerData_2.config(text=c)
    play.update()
    sleep(1)
    if c > 0:
        counter(c)
    else:
        start()

# Create start button
Start_button = tk.Button(play, text="Start", command=start, bg="gray",width=10, height=1)
Start_button.place(x=150, y=530)

# Create traffic light canvases for System 1
c1_1 = Canvas(play, width=130, height=120, bg='black')
c1_1.place(x=50, y=50)
c2_1 = Canvas(play, width=130, height=120, bg='black')
c2_1.place(x=50, y=170)
c3_1 = Canvas(play, width=130, height=120, bg='black')
c3_1.place(x=50, y=290)

# Create traffic light canvases for System 2
c1_2 = Canvas(play, width=130, height=120, bg='black')
c1_2.place(x=220, y=50)
c2_2 = Canvas(play, width=130, height=120, bg='black')
c2_2.place(x=220, y=170)
c3_2 = Canvas(play, width=130, height=120, bg='black')
c3_2.place(x=220, y=290)

# Create traffic light canvases for System 3
c1_3 = Canvas(play, width=130, height=120, bg='black')
c1_3.place(x=390, y=50)
c2_3 = Canvas(play, width=130, height=120, bg='black')
c2_3.place(x=390, y=170)
c3_3 = Canvas(play, width=130, height=120, bg='black')
c3_3.place(x=390, y=290)

# Timer display
timerData_1 = tk.Label(play, font=('calibri', 30, 'bold'), bg='black', fg='red',border=10)
timerData_1.place(x=200, y=430)

timerData_2 = tk.Label(play, font=('calibri', 30, 'bold'), bg='black', fg='red',border=10)
timerData_2.place(x=350, y=430)

play.mainloop()
