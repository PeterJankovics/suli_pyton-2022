# Import the required libraries
from tkinter import *

def eltol(pontok, x, y):
    vissza = []
    for i, pont in enumerate(pontok):
        if i % 2 == 0:
            vissza.append(pont + x)
        else:
            vissza.append(pont + y)
    return vissza
def nagyit(pontok, meret=1):
    vissza = []
    for pont in pontok:
        vissza.append(pont * meret )
    return vissza    
def forgat(pontok ,szog):
    vissza = []
    for i, pont in enumerate(pontok):
        if i % 2 == 0:
            x = pontok[i]*math.cos(math.radians(szog))-pontok[i + 1]*math.sin

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("600x300")

# Create a canvas widget
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg = "lightgray")
canvas.pack(fill = BOTH, expand = 1)

# Add a line in canvas widget
#P
"""
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
"""
#pontok0 = [10,10,30,10,30,10,90,60,90,60,150,10,150,10,170,10,150,170,170,170,10,170,30,170,10,10,10,170,30,30,30,170,170,10,170,170,150,30,150,170,30,30,90,80,90,80,150,30]

#P= [10,10,30,10,90,60,150,10,170,10,170,170,150,170,150,30,90,80,30,30,30,170,10,170,10,10]
P  = [0,0,90,0, 90,10,100,10, 100,30,100,70, 100,80,90,80, 90,90,40,90, 40,90,40,140, 40,140,0,140, 0,0,0,140,]
P2 = [40,35,65,35, 65,35,65,60, 65,60,40,60, 40,60,40,35]

E = [110,20,110,130, 110,130,120,130, 120,140,210,140, 210,140,210,110 ,210,110,150,110, 150,110,150,90, 150,90,210,90 ,210,90,210,60, 210,60,150,60,
     150,60,150,40, 150,40,210,40, 210,40,210,10, 210,10,160,10, 160,10,180,-20, 180,-20,160,-20, 160,-20,145,10, 145,10,120,10, 120,20,110,20,]

T = [220,0,320,0, 320,0,320,30, 320,30,290,30, 290,40,290,140, 290,140,250,140, 250,140,250,30, 250,30,220,30, 220,30,220,0 ]

E2 = [330,20,330,130, 330,130,340,130, 340,140,430,140, 430,140,430,110, 430,110,370,110, 370,110,370,90, 370,90,430,90, 430,90,430,60, 430,60,370,60,
      370,60,370,40, 370,40,430,40, 430,40,430,10, 430,10,340,10, 340,20,330,20]

#PETER = [[0,0,90,0, 90,10,100,10, 100,30,100,70, 100,80,90,80, 90,90,40,90, 40,90,40,140, 40,140,0,140, 0,0,0,140,][40,35,65,35, 65,35,65,60, 65,60,40,60, 40,60,40,35]]
#Pe = [[10,150,10,10,5,15,95,15,95,25,105,25,110,30,110,80,95,85,105,85,95,95,45,95,50,95,50,150,10,145,50,145,50,45,50,70,45,45,75,45,70,45,70,70,45,65,75,65],
      #[150,40,150,130,155,35,165,35,165,25,245,25,245,20,245,60,250,55,185,55,190,55,190,70,250,70,185,70,185,100,250,100,190,120,190,100,250,115,185,115,245,150,245,115,165,145,250,145,155,135,165,135,190,16,250,10,]]
"""canvas.create_line(P, fill="green", width=10)"""
p1 = eltol(P, 10, 10)
p2 = eltol (P2, 10 ,10)
e = eltol(E, 10, 10)
t = eltol(T, 10, 10)
e2 = eltol(E2, 10, 10)
canvas.create_line(p1, fill="blue", width=5)
canvas.create_line(p2, fill="blue", width=5)
canvas.create_line(e, fill="blue", width=5)
canvas.create_line(t, fill="blue", width=5)
canvas.create_line(e2, fill="blue", width=5)
for betu in P:
    betu += betu[:2]
    betu = nagyit(betu,10)
    betu = eltol(betu,200,200)
    
win.mainloop()


