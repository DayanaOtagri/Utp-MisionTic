# Es una estructura de datos que se utiliza para almacenar valores
# de forma llave : valor

datosPersonales = {
    "nombre": "Carlos",
    "apellido": "Gutierrez",
    "edad" : 30,
    "casado": True,
    "ventas": {
        1 : 10,
        2 : 30,
        3 : 2,
        4 : 15
    },
    "algo" : ("a", "b", 1)
}

# Así modifico el valor de cada llave 
datosPersonales["casado"] = False
datosPersonales["ventas"][3] = 5 

print(datosPersonales)
print (datosPersonales["algo"][1])

# Muestra el tipo de datos que es
#print (type(datosPersonales), type (datosPersonales["casado"]))

# Muestra del diccionario datosPersonales
# de la llave venta (que a su vez es un diccionario) 
# el valor de la llave 3 

#print(datosPersonales["ventas"][3]) 

# Me imprime la llave sin el valor
#for i in datosPersonales:
    #print (i)

# Me imprime el valor de la llave  
#for i in datosPersonales:
    #print (datosPersonales[i])