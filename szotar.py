<<<<<<< HEAD
Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! fdf
fdfjelentese: 3
['fdf', '3']

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! sd
sdjelentese: 3
kerek szot! s
sjelentese: 3
kerek szot! 

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! 3
3jelentese: d
kerek szot! 
['3', 'd']

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! 3dd
3ddjelentese: 3
kerek szot! s
sjelentese: 
kerek szot! 
['3dd', '3']
['s', '']

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! fds
fdsjelentese: 3
kerek szot! s
sjelentese: 
kerek szot! 

= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! wew
wewjelentese: 3
kerek szot! d
djelentese: 
kerek szot! 


= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! fasd
fasdjelentese: 3
kerek szot! s
sjelentese: 3
kerek szot! 


= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! 
= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! 
= RESTART: \\sulixerver\users\students\jankovicsp21\Downloads\szotar (1).py
kerek szot! alma
almajelentese: apple
kerek szot! desk
deskjelentese: szek
kerek szot! 
=======
import random

def szobeker ():
    szo = input("kerek szot! ")
    if szo == "":
        jelentes = ""
    else:
        jelentes = input(szo + "jelentese: ")
    return [szo, jelentes]


szavak = []
def sokbeker ():
    szo = szobeker()
    while szo[0] != "":
        szavak.append(szo)
        szo = szobeker()



    return szavak


def filebair(lista):
    f = open("szotar.txt", "a")
    
    f.close()
>>>>>>> 237c8dd85ad0437f2ea8224477354e78dea283ff
