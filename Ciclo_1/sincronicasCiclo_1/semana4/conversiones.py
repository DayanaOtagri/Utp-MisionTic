# Semana 4 / 18 mayo 2022
# Listas, cadenas, tuplas y conjuntos hacia diccionarios
import os
os.system("cls")

#Cadena a lista
cadena = "Colombia"
lista = list(cadena)
print(cadena)



cad =  " ".join(lista)
print(cad)

nombre = "Pedro"
diccionario = dict(zip(1, len(nombre)+1,nombre))
print(diccionario)

lista1 = ["Enero", "Febrero", "Marzo", "Abril"]
lista2 = [150.000, 160.000, 170.000, 180.000]
diccionario2 = dict(zip(lista1,lista2))
print(diccionario2)
print(diccionario.values())
print(diccionario.keys())
print(diccionario.items())
cadena2 = " ".join(diccionario.values())
print(cadena2)


