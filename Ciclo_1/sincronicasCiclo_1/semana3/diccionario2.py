datosPersonales = dict(
    
    nombre = "Carlos", 
    edad = 25,
    profesion = "Contador",
    
)

print(datosPersonales)

# Diccionario vacío
datosPersonales2 = {}

# se crean variables en la que el usuario ingresará sus datos
nombre = input("Digite el nombre: \n")
edad = int(input("Digite su edad: \n"))
profesion = input("Digite su profesion: \n")

# Crea el par llave-valor y se le asigna al diccionario vacío
datosPersonales2.setdefault("nombre", nombre)
datosPersonales2.setdefault("edad", edad)
datosPersonales2.setdefault("profesion", profesion)


datosPersonales3 = {
    
    "nombre": nombre,
    "edad": edad,
    "profesion": profesion,
    
}


inventario = {}

# por cada ITERACION en un RANGO(Lo hace 4 veces) DE 4 
for i in range(4): 
    # Acción a realizar del for 
    codigo = int(input("Digite el código del articulo \n"))
    cantidad = int(input("Digite la cantidad existente: \n"))
    inventario.setdefault(codigo, cantidad)
    
print(inventario)

urlListas =  "https://tutorial.recursospython.com/colecciones/#listas"