import random
first_names = ["Anna", "Bence", "Csaba", "Dóra", "Eszter", "Ferenc"]
last_names = ["Gál", "Hajdú", "Iglódi", "Juhász", "Kovács", "Lakatos"]
for i in range(100):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    print(f"{first_name} {last_name}")
