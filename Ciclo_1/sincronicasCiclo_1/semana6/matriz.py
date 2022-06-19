# Semana 6 / 31 de mayo 2022 
# Libreria numpy
import numpy as np 
import pandas as pd 
matriz = np.array([4,8,7])
print(matriz, matriz.shape, type(matriz), type(matriz), type(matriz[1]))


# Matriz de dos dimensiones
matriz1 = np.array([[4,5,7],[3,5,4], [1,9,7]])
print(matriz1, matriz1.shape, type(matriz1), type(matriz1[0,1]))

# Matriz de tres dimensiones 
matriz2 = np.array([
    
    [[1,2], [3,4], [5,8]],
    [[3,8], [5,7], [2,3]],
    [[3,8], [1,2], [6,40]],
    [[3,8], [1,2], [6,4]]    
    
])

print(matriz2)
print(matriz2.shape)
print(matriz2[2,2,1])