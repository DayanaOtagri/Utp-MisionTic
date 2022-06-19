# Semana 6 / 31 mayo 2022


import numpy as np
# matriz de solo ceros
matriz = np.zeros((4,4), dtype=np.int8)
print(matriz)

# matriz de solo unos
matriz = np.ones((2,2))
print(matriz)

# matriz de un valor
matriz = np.full((2,2),True)
print(matriz)

# matriz de un valor
matriz = np.full((2,2),5)
print(matriz)

# matriz de número aleatorios
matriz = np.random.random((3,3))
print(matriz)

matriz100 = np.full((3,3),100)
print(matriz * matriz100, matriz.multiply(matriz100))