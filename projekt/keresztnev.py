# Import the required libraries
from tkinter import *
import math

class forgato():
    canvas = 0
    vonalak = []
    szog = 0
    szogsebesseg = 0.2
    def __init__(self, canvas, vonalak):
        self.canvas = canvas
        self.vonalak = vonalak
        #self.szog = szog
        #self.szogsebesseg = szogsebesseg
    def rajzol(self):
        canvas.delete("all")
        self.szog += self.szogsebesseg
        #print(szog)
        for betu in self.vonalak:
            betu = self.nagyit(betu, 1)
            betu = self.eltol(betu, -kozep[0], -kozep[1])
            betu = self.forgat(betu, self.szog)
            betu = self.eltol(betu, 325, 300)
            betu = self.eltol(betu, kozep[0], kozep[1])
            self.canvas.create_line(betu, fill="blue", width=3)
    def eltol(self, pontok, x, y):
        vissza = []
        for i, pont in enumerate(pontok):
            if i % 2 == 0:
                vissza.append(pont + x)
            else:
                vissza.append(pont + y)
        return vissza
    def nagyit(self, pontok, meret=1):
        vissza = []
        for pont in pontok:
            vissza.append(pont * meret )
        return vissza    
    def forgat(self, pontok ,szog):
        vissza = []
        for i, pont in enumerate(pontok):
            if i % 2 == 0:
                szogRadian = math.radians(szog)
                x = pontok[i]*math.cos(szogRadian)-pontok[i + 1]*math.sin(szogRadian)
                y = pontok[i]*math.sin(szogRadian)+pontok[i+1]*math.cos(szogRadian)

                vissza.append(x)
                vissza.append(y)
        return vissza            
                
            
    

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1280x720")

# Create a canvas widget
canvas=Canvas(win, width=1280, height=720)
canvas.configure(bg = "lightgray")
canvas.pack(fill = BOTH, expand = 1)

# Add a line in canvas widget


PETER = [[0,0,90,0, 90,10,100,10, 100,30,100,70, 100,80,90,80, 90,90,40,90, 40,90,40,140, 40,140,0,140, 0,0,0,140],
         [40,35,65,35, 65,35,65,60, 65,60,40,60, 40,60,40,35],
        
         [110,20,110,130, 110,130,120,130, 120,140,210,140, 210,140,210,110 ,210,110,150,110, 150,110,150,90, 150,90,210,90 ,210,90,210,60, 210,60,150,60,
          150,60,150,40, 150,40,210,40, 210,40,210,10, 210,10,160,10, 160,10,180,-20, 180,-20,160,-20, 160,-20,145,10, 145,10,120,10, 120,20,110,20,],

         [220,0,320,0, 320,0,320,30, 320,30,290,30, 290,40,290,140, 290,140,250,140, 250,140,250,30, 250,30,220,30, 220,30,220,0],

         [330,20,330,130, 330,130,340,130, 340,140,430,140, 430,140,430,110, 430,110,370,110, 370,110,370,90, 370,90,430,90, 430,90,430,60, 430,60,370,60,
          370,60,370,40, 370,40,430,40, 430,40,430,10, 430,10,340,10, 340,20,330,20],

         [440,0,520,0, 520,0,520,10, 520,10,530,10, 530,10,530,60, 530,60,520,60, 520,60,520,70, 520,70,530,70, 530,70,530,140, 530,140,490,140,
          490,140,490,80, 490,80,480,80, 480,80,480,140, 480,140,440,140, 440,140,440,0,], [495,47,495,30, 495,30,480,30, 480,30,480,47, 480,47,495,47]]
                         


elso = forgato(canvas, PETER)

kozep = [0,0]
db = 0
for betu in PETER:
    xK = betu[::2]
    yK = betu[1::2]
    kozep[0] += sum(xK)
    kozep[1] += sum(yK)
    db += len(xK)

kozep[0] /= db
kozep[1] /= db
szog = 0
while True:
    elso.rajzol()
    win.update_idletasks()
    win.update()
    #win.mainloop()



#for betu in PETER:
 #   betu = forgat(betu, 10)
  #  canvas.create_line(PETER, fill="blue", width=5)
win.mainloop()


