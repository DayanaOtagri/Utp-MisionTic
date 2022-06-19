#Semana 5 / 25 mayo 2022
from functools import reduce






# ----------------------------------------------------------------
lista = [
    
    #Nro Factura, cantidad de produtos y precio unitario
    [1525,[4,2500],[3,8500], [5,12600]],
    [1520,[3,2500],[2,8500]],
    [1522,[1,2500],[5,8500], [2,12600]]
    
]


# Generar una lista de listas de la forma [[No. factura, total factura]....[]]
# [No. factura, total1, total2, total3, total4, total5, total6, totaln]

# Map primero una funcion y luego lo que se quiere recorrer

# Un map que recorre la lista general
listaTotal = list(map(lambda x:[x[0]] + list(map(lambda y:y[0]* y[1], x[1:])), lista))
print(listaTotal)
listaTotal = list(map(lambda x:[x[0]] +  [reduce(lambda a,b: a+b,x[1:])], listaTotal))
print(listaTotal)
