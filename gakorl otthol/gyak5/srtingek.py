bekert = []

for e in range(8):
    beker = int(input("Kerek 8 szamot!!! ")) 
    bekert.append(beker)

for e in bekert:
    print(str(e),end = "")

for i in range (8):  
    if i % 4 == 0:
        print()
    print(str(bekert[i])+"\t",end = "")    

print()

print(sum(bekert))


szoveg = """Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare.
            Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque,
            diam non pellentesque rhoncus, risus lorem porttitor leo,
            ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus,
            eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl,
            non dapibus ex fermentum vitae."""

talalt = 0
betu = input("kerek egy betut!!!")
while betu != "end":       
    for e in szoveg:
        if betu == e:
            talalt += 1
    if talalt == 0:
        print("nincs benne.")
    print(talalt)
    talalt = 0
    betu = input("kerek egy betut!!!") 
    




