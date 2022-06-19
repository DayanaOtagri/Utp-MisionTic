#Semana 4 / 18 mayo 2022
# Es una coleccion de datos que se utiliza 
# para almacenar varios elementos. 
# No son ordenados, son mutables 


nombres = {"Juan", "Camilo", "Sergio", "Valentina"}
ciudades = set(("Caracas", "Bogotá", "Medellin", "Bucaramanga" ))

print(nombres, type(nombres))
print(ciudades, type(ciudades))

#Anadir elementos a un conjunto
ciudades.add("Sogamoso")
print(ciudades)
# Elimina un elemento del conjungoy
ciudades.remove("Caracas")
print(ciudades)


#Mirar porque imprime cada interacion
for i in ciudades:
    if "Panamá" in ciudades: 
        print("Si esta")
    else: print("No esta")



