from tkinter import *


master = Tk()

# .minsize method sets the default size of the GUI as w=1000, h=500

master.minsize(width=1000, height=500)

# background set to white to mirror a sheet of paper

master.configure(background='white')

# I'm going to try to display lines because IDK why

line = Canvas(master, height=10, width=10)
line.bbox()
# Button currently set to DISABLED bc program function has not been created yet

run = Button(master, text="Create Quiz", compound=CENTER, background='green')

# run.pack actually packs the button onto the screen at the bottom

run.pack(side=BOTTOM)

master.mainloop()

