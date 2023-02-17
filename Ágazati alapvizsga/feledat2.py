import haromszog



def ujabb(darab=3):
    haromszogek = []
    for i in range(darab):
        haromszogek.append(haromszog.haromszog())
    for e in haromszogek:
        print("\ta={}, b={}, c={}".format(e[0], e[1], e[2]))
    return haromszogek
    


def haromszoge(haromszogek):
    for e in haromszogek:
        if sum(e) - max(e) > max(e):
            print("Lehet haromszog.")
        else:
            print("nem lehet haromszog.")

h = ujabb(3)
haromszoge(h)
#lista = haromszog.haromszog()
#print(lista)
