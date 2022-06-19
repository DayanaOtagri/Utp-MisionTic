import pandas as pd 
import numpy as np

inventario = {
    
    "impresoras" : ["Hp","Canon", "Epson"],
    "cantidad" : [10,34,50]
    
}

#ejecutarla para ver la difentecia
# entre esta y la que tiene el index
# dataF = pd.DataFrame(inventario) 

# Index me modifica los indices que esta por defecto 
dataF = pd.DataFrame(inventario, index = ["p1", "p2", "p3"])
"""print(dataF)"""
"""print(type(dataF))"""

# Acceder a los diferentes 
# elementos que tengo dentro del DataFrame
"""print(dataF.iloc[0])"""
"""print(dataF.loc["p3"])"""

# Crear un DataFrame a partir de un array numpy
# Arreglo bidimensional en numpy 

arreglo = np.array([[4,5,2], [5,7,8], [7,3,1]])
print(arreglo)
# cada fila y columna  le da un indice númerico 
"""dataFrame1 = pd.DataFrame(arreglo)"""


# Aquí le estamos asignando el nombre a filas y columnas 
dataFrame1 = pd.DataFrame(arreglo, columns=["María", "Juan", "Carlos"], index = ["Enero", "Febrero", "Marzo"])
print(dataFrame1)