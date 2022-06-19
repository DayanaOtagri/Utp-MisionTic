# Semama 5 // 25 mayo 2022
from functools import reduce

lista = [5, 8, 5,4]
total = reduce(lambda acumulador, elemento: acumulador + elemento, lista)
print(total)
