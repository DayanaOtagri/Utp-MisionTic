#Semena 3 / Clase 9 de mayo de 2022

# Dado un n cantidad de números enteros diga el mayor y el menor de ellos
# Datos de entrada = n: cantidad de números
#                    número: cada uno de los números ingresados por el usuario
# Datos de salida =  mayor: el número mayor
#                    menor: el número menor 


n = int(input("Digite la cantidad de números que desea ingresar \n")); 
for i in range(n): # La variable i va a contar de 0 hasta n-1 
    numero = int(input(f"Digite el número {i+1}: \n"))
    if i == 0: 
        mayor = numero
        menor = numero
    elif numero > mayor:
          mayor = numero
    
    elif numero < menor:
         menor = numero
          
print(f"El mayor de los números {n} números ingresados es {mayor} \n ")  
print(f"El menor de los números {n} números ingresados es {menor} \n ")  

