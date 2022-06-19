#pandas es una biblioteca de software escrita como extensión de
#Numpy para manipulación y análisis de datos para el lenguaje de programación Python.


import pandas as pd

diccionario  = {
    "Enero" : 24,
    "Febrero" : 28,
    "Marzo" : 29,
    "Abril" : 30,
    "Mayo" : 31,
}

# indicies implicios (No se ven)
serie = pd.Series(diccionario)
#print(serie) 

lista = [24,28,29,30,130]

# indicies explicitos (Se ven) // con el index 
# le estamos asignando como inidices los meses de año
# Sin el index quedan en  0, 1, 2, 3, 4, 5
# Las series tiene métodos 
serie1 = pd.Series(lista, index = diccionario.keys())
# serie1 = pd.Series(lista, index = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"], dtype = int8)
print(serie1[1])
# Método loc = se puede acceder del indice explicito 
print(serie1.loc["Mayo"])
print(serie1.iloc[2])
print(serie1[2:5])