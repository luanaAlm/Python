"""
Map: faz mapeamento de valores para função.
"""
import math
def area(r):
    "Calcule a area de um círculo com raio 'r'"
    return math.pi * (r ** 2)

print(area(6))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
#forma comum
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

#Utilizando o map
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

#map com lambda
print(list(map(lambda r: math.pi *(r ** 2), raios)))