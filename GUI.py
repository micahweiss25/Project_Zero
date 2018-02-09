<<<<<<< Updated upstream
import Tkinter

from tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

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

# Menu functions

    # save the notes
def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = self.textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

    # This function will actually create the quiz

# This function will up the text editor widget
def openPad():
    pad = Tkinter.Tk() # creates new GUI and all code between here and pad.mainloop() control that GUI
    textPad = ScrolledText(pad, width=100, height=80)
    def dummy():
        print "I am a Dummy Command, I will be removed in the next step"
    menu = Menu(pad)
    pad.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Create Quiz", command=dummy)
    filemenu.add_command(label="New", command=dummy)
    filemenu.add_command(label="Open...", command=dummy)
    filemenu.add_command(label="Save", command=dummy)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=dummy)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=dummy)
    textPad.pack()
    pad.mainloop()


# Button to create quiz

run = Button(master, text="Create Quiz", compound=CENTER, background='green', command=bla)
run.pack(side=BOTTOM)

# button to pull up a text editor

note = Button(master, text="Start your notes", compound=CENTER, background='red', command=openPad)
note.pack(side=BOTTOM)



master.mainloop()
=======
import Tkinter
from tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox


pad = Tkinter.Tk()  # creates new GUI and all code between here and pad.mainloop() control that GUI
textPad = ScrolledText(pad, width=100, height=80)

# Menu functions

    # Open function

def open_command():
    file = tkFileDialog.askopenfile(parent=pad, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()

    # Save file

def fuckPython():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()

    # create quiz

dicktickler = {}
"""side note about this function: it won't display the text in the editor when you open it but it does open it """

def quiz():
    file = tkFileDialog.askopenfile(parent=pad, mode='rb', title='Select a file')
    if file != None:



        for i,line in enumerate(file):
            if "#" and ":" in line:
                dicktickler[str(line[line.index("#")+1 : line.index(':')])] = line[line.index(':')+1:]
                print(i, line)
    print(dicktickler)
    file.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        pad.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")

def dummy():
        print "I am a Dummy Command, I will be removed in the next step"

menu = Menu(pad)
pad.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Create Quiz", command=quiz)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=fuckPython)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
textPad.pack()




pad.mainloop()
>>>>>>> Stashed changes
