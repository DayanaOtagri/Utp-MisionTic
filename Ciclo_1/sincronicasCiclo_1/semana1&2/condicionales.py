""" Trabajando con Condicionales en Python: 
    Un programa que verifica si un número mayor o igual a 100 """

#Es como el prompt en JS - Scanner en Java
# \n hace un salto de línea 
#el int convierte un String en Integer 
respuesta = input("Digite el numero:\n")
numero1 = int(respuesta)

#Indentacion: tiene que estar tabulado. 
if numero1 >= 100:  
    print(f"El número {numero1} es mayor o igual a 100 ")
else: 
    print(f"El numero {numero1} es menor a 100")



#Declaramos una variable que tiene
# como valor "True" es decir, es verdadera

haceSol = False

"""El if comprueba SI UNA CONDICION SE CUMPLE O NO """
# Si hace sol: 
if haceSol:
    # Accion a realizar
    print("Vamos a salir") #Imprime en consola el resultado
else: # else indica que si la condicion "haceSol" no es verdadera hará otra accion
    print("No salimos")