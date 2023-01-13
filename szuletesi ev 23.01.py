import random
   
def datum ():
# for i in range(100):
    ev = random.randint(2003,2008)
    ho = random.randint(1,12)
    if ho == 1 or ho  == 3 or ho == 5 or ho == 7 or ho == 8 or ho == 10 or ho == 12:
        nap = random.randint(1,31)
    elif ho == 2 or ho == 4 or ho == 6 or ho == 9 or ho == 11:
        nap = random.randint(1,30)  
    else:
        if ev % 4 ==0:
            nap = random.randint(1,29)
        else:
            nap = random.randint(1,28)
    evszam = str(ev) + "." + str(ho) + "-" + str(nap) + "-"
    return evszam
    
def datumfile():   
    f = open("evszam.txt","w")     
    for i in range (10):
        f.write(datum()+"\n")
    f.close()

