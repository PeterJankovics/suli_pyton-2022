szamok = []

for i in range (8):
    szamok.append(int(input("Kerek szamot!!! ")))

for i in szamok:
    print(str(i),end="")
print()    

for i in range (8):  
    if i % 4 == 0:
        print()
    print(str(szamok[i])+"\t",end = "")        
        
    
print()


osszeg = sum(szamok)  
print(osszeg)


szoveg = "Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."

betu = "sdsd"
while betu != "end":
    betu = (input("kerek betut!! "))
    for i in betu:
        x = betu.find(betu)
        print(x)


torol = "orna"

for i in range (len(torol)):
    szoveg2 = szoveg.replace(torol[i],"")
print(len(szoveg))
print(len(szoveg2))
    

beker = ""
while beker != "1":
    beker = input("kerek karaktert!!! ")
    for i in rajz:
        print("" * i[0],beker * i[1])
    














