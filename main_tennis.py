from tkinter import messagebox, ttk
import OpenCV_test as OC
from tkinter import *
import tkinter as tk



def display_selection():
    # Get the selected value.
    hr=0
    day = combo.get()
    court = combo3.get()
    p_court = combo2.get()
    p_time = combo4.get()
    ball = v.get()
    #print(ball," it is ")

    courts =[1,2,3,4]
    if court=="1. Indoor Hard Courts 1-4 ": 
        court=1
  
    if court == "2. Clay Courts 5-8 ": 
        court = 2
 
    if court == "3. Hard Courts 9 - 12 ": 
        court = 3

    if court == "4. Rooftop 13 - 16 ": 
        court = 4

    
    if int(day)==0:
        hr = 0
        print('same dat booking')

    if int(day)==1:
        hr=20
        print("Booking for Day + 1, Time to book is : 8 PM ")

    if int(day) == 2:
        hr = 10
        print("Booking for Day + 2, Time to book is : 10 AM ")

    counter = 0

    print('Activating Tennis booking bot version 2.0 ... powered by Brute Force Solutions.')
    while counter < 3:
        print(hr)
        x =OC.book_c(int(day),int(court),int(p_court),int(p_time),int(hr),ball,courts)
        if x == True:
            counter = 3
        else:
            counter+=1


main_window = tk.Tk()
main_window.config(width=600, height=450)
main_window.title("Tennis Booking BOT")


v = tk.IntVar()
combo3 = ttk.Combobox(state="readonly",values=["1. Indoor Hard Courts 1-4 ", "2. Clay Courts 5-8 ", "3. Hard Courts 9 - 12 ", "4. Rooftop 13 - 16 "])
combo2 = ttk.Combobox(state="readonly",values=["1", "2", "3", "4"])
combo = ttk.Combobox(state="readonly",values=["0","1", "2"])
combo4 = ttk.Combobox(state="readonly",values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"])
rd1=ttk.Radiobutton(text="Book Ball Machine", variable=v,value=1)

button = ttk.Button(text="Book Now", command=display_selection)

dayselection = ttk.Label(text="Select Day to Book")
courtsel = ttk.Label(text="Select Court Type to Book")
courtsel_1 = ttk.Label(text="Select Court No. to Book")
courtsel_2 = ttk.Label(text="Select Timeslot 1-16")

dayselection.place(x=50, y=30)
courtsel.place(x=200, y=30)
combo.place(x=50, y=50)
combo3.place(x=200, y=50)
combo4.place(x=200, y=100)

# Goes in next line
combo2.place(x=50, y=100)
courtsel_1.place(x=50, y=80)
courtsel_2.place(x=200, y=80)
button.place(x=50, y=200)
rd1.place(x=50, y=150)

main_window.mainloop()