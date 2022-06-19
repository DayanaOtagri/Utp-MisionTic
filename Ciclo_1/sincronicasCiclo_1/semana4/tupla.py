#Semana 4  / 16 mayo 2022 
# tuplas son una colección de datos que 
# se utilizan para almacenar varios elementos 
# son colecciones indexadas, son inmutables 

#Crear una tupla: 
ciudades = ("Cali", "Medellin", "Barranquilla", "Bogotá")

"""ciudades[1] = "Montería" No se puede porque son inmutables 
 
    En las tuplas no están  los siguientes métodos:

    #append()
    # extend()
    # remove()
    #clear()
    # sort()
    
 """
 
variosDatos = ("Bogotá", 1997, True, 34.6)

for i in variosDatos: 
     print(i, type(i))
     
lista = list(variosDatos)
print(lista, type(lista))


def operaciones(a,b):
    suma = a + b 
    resta = a - b 
    mult = a * b
    div = a / b
    return suma, resta, mult, div

resulatos = operaciones(25, 5)
"""print(resulatos, type(resulatos))
print(f"El resultado de la suma es {resulatos[0]}")

"""