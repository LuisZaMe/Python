import random

names_list = []
npersonas = int(input("Cuantas personas entran en la ruleta? "))

for name in range(npersonas):
    sname = input(f"name:")
    names_list.append(sname)

print (names_list)

random_number = random.randint(1, len(names_list))
print(names_list[random_number - 1], "is going to buy the meal today")