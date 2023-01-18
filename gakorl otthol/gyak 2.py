szam = []

for i in range (8):
    szam.append(int(input("kerek szamot")))
    
for i in szam:
    print(str(i), end= " ")
print()    

for i in range(8):
    print(str(szam[i])+"\t", end= "")
    if i % 4 == 2:
        print()
print()    


osszeg = sum(szam) + len(szam)
print(osszeg)


szoveg = "Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
betu = "asd"
while betu != "end":
    betu = input("kerek betut!!")
    pass


for i in szoveg:
     szoveg.remove (str("orna"))
     print(len(szoveg))














