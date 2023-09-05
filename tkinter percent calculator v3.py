#This code is to create a small Tkinter window that asks for a number and
#calculates what percentage it is of a larger number (hardcoded in).

#Tried to incorporate some code from this example: https://insolor.github.io/effbot-tkinterbook-archive/entry.htm
#Still get error where the entry window returns an empty string

from sys import argv
import tkinter as tk


#making tkinter window
window = tk.Tk()


#make greeting line
lbl = tk.Label(text = "What is your number?",
                    width = 20,
                    height = 5)
lbl.pack()


#making entry box with variable
string = tk.StringVar()
ent = tk.Entry(textvariable=string)
ent.pack()

string.set("")
out_string = string.get()


#making an "OK" button
btn = tk.Button(text = "OK",
                    width = 5,
                    height = 1)
btn.pack()


#make output line
lbl = tk.Label(text = "",
                        width = 20,
                        height = 3)
lbl.pack()


#define calculate restuls function
def convert(s):
    n = int(s)
    total = n/225*100
    return print(str(round(total,2)))


#button click event --> calculate what's in the box
def handle_click(event):
    total = convert(out_string)
    to_display = "You're " + total + " % done!"
    lbl.configure(text = to_display)

btn.bind("<Button-1>", handle_click)


#run the window
window.mainloop()