import Tkinter
from tkinter import *
from ScrolledText import *
import tkFileDialog
pad = Tkinter.Tk()  # creates new GUI and all code between here and pad.mainloop() control that GUI
textPad = ScrolledText(pad, width=100, height=80)

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

def fuckPython():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()


menu = Menu(pad)
pad.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Make Quiz", command=quiz)
filemenu.add_command(label="Save", command=fuckPython)
textPad.pack()






pad.mainloop()