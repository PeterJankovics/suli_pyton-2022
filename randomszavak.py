import random
szavak = ["alma","körte","banán","dinnye","barac",]
# szandom szó kiirasa
# random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))
