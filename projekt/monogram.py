# Import the required libraries
from tkinter import *
def eltol(pontok, x, y):
    vissza = []
    for i, pont in enumerate(pontok):
        if i % 2 == 0:
            vissza.append(pont + x)
        else:
            vissza.append(pont + y)
    return(vissza)        
#def nagyit(pontok, meret=1):
#    pass
    

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x300")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
canvas.pack(fill = BOTH, expand = 1)

# Add a line in canvas widget
#P
canvas.create_line(10,150,10,10, fill="green", width=10)
canvas.create_line(5,15,95,15, fill="green", width=10)
canvas.create_line(95,25,105,25, fill="green", width=10)
canvas.create_line(110,30,110,80, fill="green", width=10)
canvas.create_line(95,85,105,85, fill="green", width=10)
canvas.create_line(95,95,45,95, fill="green", width=10)
canvas.create_line(50,95,50,150, fill="green", width=10)
canvas.create_line(10,145,50,145, fill="green", width=10)
canvas.create_line(50,45,50,70, fill="green", width=10)
canvas.create_line(45,45,75,45, fill="green", width=10)
canvas.create_line(70,45,70,70, fill="green", width=10)
canvas.create_line(45,65,75,65, fill="green", width=10)
#E
canvas.create_line(150,40,150,130, fill="green", width=10)
canvas.create_line(155,35,165,35, fill="green", width=10)
canvas.create_line(165,25,245,25, fill="green", width=10)
canvas.create_line(245,20,245,60, fill="green", width=10)
canvas.create_line(250,55,185,55, fill="green", width=10)
canvas.create_line(190,55,190,70, fill="green", width=10)
canvas.create_line(250,70,185,70, fill="green", width=10)
canvas.create_line(245,100,245,70, fill="green", width=10)
canvas.create_line(185,100,250,100, fill="green", width=10)
canvas.create_line(190,120,190,100, fill="green", width=10)
canvas.create_line(250,115,185,115, fill="green", width=10)
canvas.create_line(245,150,245,115, fill="green", width=10)
canvas.create_line(165,145,250,145, fill="green", width=10)
canvas.create_line(155,135,165,135, fill="green", width=10)
canvas.create_line(190,16,250,10, fill="green", width=10)

pontok0 = [10,10,30,10,30,10,90,60,90,60,150,10,150,10,170,10,150,170,170,170,10,170,30,170,10,10,10,170,30,30,30,170,170,10,170,170,150,30,150,170,30,30,90,80,90,80,150,30]

#P= [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]
P = [10,150,10,10,5,15,95,15,95,25,105,25,110,30,110,80,95,85,105,85,95,95,45,95,50,95,50,150,10,145,50,145,50,45,50,70,45,45,75,45,70,45,70,70,45,65,75,65]
#canvas.create_line(P, fill="green", width=10)
p2 = eltol(P, 20, 20)
#canvas.create_line(p2, fill="blue", width=10)

#win.mainloop()


