from tkinter import *

master = Tk()

# .minsize method sets the default size of the GUI as w=1000, h=500

master.minsize(width=1000, height=500)

# background set to white to mirror a sheet of paper

master.configure(background='white')

# this is where the user inputs the name of the doc they want converted into a quiz

e = Entry(master)
e.pack()
e.delete(0, END)

# assign entry to var file_name when button is pressed and create Text widget to display entry

def bla():
    file_name = e.get()
    with open(file_name, "r") as f:
        filedata = f.read()
    T = Text(master, height=2, width=30)
    T.pack(side=LEFT)
    T.insert(END, filedata)

# Button currently set to DISABLED bc program function has not been created yet

run = Button(master, text="Create Quiz", compound=CENTER, background='green', command=bla)

# run.pack actually packs the button onto the screen at the bottom

run.pack(side=BOTTOM)

master.mainloop()
