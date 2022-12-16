szam = "safdafsgolidrsgnirgzgir"
while len(szam) != 3:
    szam = input("kerek 3 jegyu szamot: ")
szam = int(szam)

if szam % 12 == 0:
    print("osztható!!!!444!4!")
print(szam)

szoveg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vitae mattis ipsum. Mauris mauris tortor, pharetra vitae mi lobortis, malesuada dapibus sapien. Duis quis metus ut leo bibendum malesuada id sit amet erat. Vivamus vitae arcu non lorem venenatis aliquet ut vitae tellus. In hendrerit, sem non facilisis iaculis, quam est ultricies erat, auctor hendrerit eros nisi vitae metus. Nullam efficitur a neque vitae vehicula. Mauris nisl magna, ultrices ut turpis vel, vehicula rutrum arcu. Curabitur vitae efficitur risus. Aliquam non porta lectus, luctus placerat augue. Proin mauris quam, luctus et velit ut, fringilla bibendum tellus. Proin vitae laoreet dui, a vulputate velit. Vivamus hendrerit venenatis molestie."
betu="i"
print(len(szoveg.split(" ")))
szoveg2 = szoveg.replace(betu,betu.upper())
print(szoveg2)































