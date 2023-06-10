animals=("bance","martin","girrafe","kelgyó","kágyilló")
print(animals[1])
print(animals[-1])
print(animals[1:4:2])
animals=list(animals)
animals[1]="milan"
animals=tuple(animals)
print(animals[1])
ures=[]
print(ures)
for i in range(4,-1,-1):
    print(i)
    ures.append(animals[i])
print(ures)    
