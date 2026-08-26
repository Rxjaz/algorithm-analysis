import random

def generate_array():

    arrays = []
    start = int(input("Inicio:")) 
    increase = int(input("Incremento: "))
    end = int(input("Final: "))

    for i in range(start, end+1, increase):
        sublist = []
        for j in range(i):
            sublist.append(random.randint(1, end))
        arrays.append(sublist)

    return arrays

res = generate_array()
print("\n")
print(res, "\n")
print("--------------------------")