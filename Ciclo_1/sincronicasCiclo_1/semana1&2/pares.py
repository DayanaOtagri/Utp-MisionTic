# Semana 3 / 10 de mayo del 2022
# Operacioón matemática módulo, devuelve el residuo de una división
# Realice un programa que lea un numero entero y diga si es par o impar


numero = int(input("Digite un número entero: \n"))

if numero % 2 == 0:
    print(f"El {numero} es par")
else: 
    print(f"El {numero} es impar")