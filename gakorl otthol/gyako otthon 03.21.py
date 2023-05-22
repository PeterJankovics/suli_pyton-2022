print("1. feladat: ")
mondat = input("Add meg a mondatot!")

print("2. feladat: ")
szures = " ,?!."
betuk = [karakter for karakter in mondat if karakter not in szures]
print("a mondatban {} betu van.".format(len(betuk)))

print("3. feladat: ")
szavak = mondat[:-1].lower().replace(","," ").split()
#print(szavak)
print(f"a mondatban {len(szavak)} szó van.")

print("4. feladat: ")
maganhangzo = 0
mgh = ["e","u","i","o","a"]
for karakter in mondat.lower():
    if karakter in mgh:
        maganhangzo = maganhangzo +1
print(f"A mondatban {maganhangzo} maganhangzo van.")


print("5. feladat: ")
leghosszabb = ""
maxszo = 0
for szo in szavak:
    if maxszo < len(szo):
        maxszo = len(szo)
        leghosszabb = szo
print(f"a mondatban a leghosszabb szó a ˝{leghosszabb}˝, {maxszo} betűs.")

print("6. feladat: ")
szobeker = input("add meg a keresett szót: ")
if szobeker not in mondat:
    print("nincs benn a mondatban.")
else:
    print("benne van a mondatban.")
