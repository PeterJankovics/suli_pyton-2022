# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1280x720")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300, bg ="skyblue")
canvas.pack(fill = BOTH, expand = 1)

canvas2=Canvas(win, width=500, height=300, bg ="orange")
canvas2.pack(fill = BOTH, expand = 1)
# Add a line in canvas widget
canvas.create_line(90,180,90,90, fill="purple", width=5)
canvas.create_line(90,180,180,180, fill="red", width=5)
canvas.create_line(180,180,180,90, fill="green", width=5)
canvas.create_line(90,90,180,90, fill="orange", width=5)


canvas.create_line(300,90,380,210, fill="blue", width=5)
canvas.create_line(300,90,220,210, fill="purple", width=5)
canvas.create_line(220,210,380,210, fill="brown", width=5)


canvas.create_line(500,90,500,90, fill="blue", width=5)

win.mainloop()
