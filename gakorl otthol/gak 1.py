szam = []

for i in range (10):
    szam.append (int(input("kerek szamot!!! ")))

for i in szam:
    print(str(i),end = "")
print()    

for i in range (10):
    print(str(szam[i])+"\t",end="")
    if i % 3 == 2:
        print()
        
print()


atlag = sum(szam) / len(szam)
print(atlag)

szoveg = "Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."
betu = "sdf"
while betu != "":
    betu = input("betut!!!")
    szoveg = szoveg.replace(betu, betu.upper())
    print(szoveg)
    

jelek = ".,?!:;"

for i in  range (len(jelek)):
    szoveg = szoveg.replace(jelek[i],"")
print(szoveg)    

