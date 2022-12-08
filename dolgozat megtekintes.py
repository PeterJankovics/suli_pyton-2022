szamok = []
for i in range(10):
    szamok.append(int(input("Kerek egy szamot: ")))

for i in szamok:
    print(str(i),end="")
print()


for i in range(10):
    print(str(szamok[i])+"\t",end="")
    if i % 3 == 2:
        print()
print()
atlag = sum(szamok) / len(szamok)
print(atlag)

osszeg = 0
for i in szamok:
    osszeg += i
atlag = osszeg / len(szamok)
print(atlag)

szoveg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar metus sed consequat laoreet. Donec elementum commodo lorem non porta. In mauris nunc, elementum a justo auctor, vehicula condimentum urna. Praesent elit eros, molestie eget malesuada sed, varius non mauris. Fusce ut nibh leo. Ut gravida rhoncus mauris, et eleifend ante tempus vitae. Nunc malesuada diam nec lectus iaculis pharetra."
betu = "asd"
while betu != "":
    betu = input("kerek egy betut: ")
    szoveg = szoveg.replace(betu, betu.upper())
    print(szoveg)

lista=szoveg.split(" ")
lista.reverse()
szoveg2 = " ".join(lista)
print(szoveg2)
jelek = ",.!?-:;"

for i in range(len(jelek)):
    szoveg = szoveg.replace(jelek[i],"")
print(szoveg)



