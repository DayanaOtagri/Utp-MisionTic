# Semana 4 / 16 mayo 2022 
# Una lista es una colección de datos que se utiliza para guardar varios elementos
# Es indexada de forma númerica 
# Son mutables 

#Crear lista: 




ciudades = ["New York", "Londres", "Madrid"]
variosDados = ["Bogotá", 1997, True, 34.6] 
frutas = list(("manzana", "pera", "coco"))


"""
print(ciudades, type(ciudades))
print(frutas, type(frutas))

frutas[0] = "banana"
print(frutas)"""


"""for i in variosDados:
    print(i, type(i))
"""

# La variable i toma el valor de los elementos de la lista 
posicion = 0
for i in ciudades: 
    if i == "Londres":
        print("Londres está en la lista")
        print(f"Londres está en la posicion {posicion} de la lista")
    posicion += 1
    # print(i) # Imprime cada iteración mostrando la ciudades
    
print(ciudades.index("Londres")) # Imprime la posicion en la que se encuentra Londres en la lista
    

"""ciudades.append("Caracas") #Añade un elemento a la lista 
ciudades.remove("New York") # Elimina un elemento a la lista  
print(ciudades)"""

# print("Londres" in ciudades) # Arroja un booleano sobre si existe x elemento en la lista 


"""numeros = []
for i in range(10):
    #Agrega numeros de 2 en 2 a la lista
    numeros.append(i*2)
    
print(numeros)"""