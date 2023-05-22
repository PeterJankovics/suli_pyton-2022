while True:
    try:
        szoveg = str(input("Kérem, adjon meg egy szöveget: "))
        szam = int(input("Kérem, adjon meg egy egész számot: "))
        break
    except ValueError:
        print("Hiba! Nem megfelelő formátumú számot adott meg!")

karakter = szoveg[szam - 1]
eredmeny = karakter * szam

print(f"Az adott szöveg {szam}. karaktere: '{karakter}'")
print(f"Az eredmény: {eredmeny}")
