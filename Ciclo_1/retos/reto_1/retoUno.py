# Declarar una Funcion con nombre CDT que reciba 3 parámetros
def CDT(usuario:str, cantidad:int, tiempo:int):

    #  Creo una variable llamada ValorIntereses donde realizo la operación de los intereses
    valorIntereses = (cantidad * 0.03 * tiempo) / 12
    # Creo una variable llamada Valor total que al valor total le suma los intereses 
    valorTotal = valorIntereses + cantidad

    
    # Creo un condicional (if) que verifique si son
    # menos de 2 meses o 2 meses exactos entonces a la cantidad le resta el 2% 
    if(tiempo <= 2):
        
        #Creo una variable llamada valorAPerder que contiene la resta del valor total - 2%
        valorAPerder = cantidad * 0.02
        # Si se cumple la condición entonce el valor total será cantidad - valorAPerder
        valorTotal = cantidad - valorAPerder


    # Esto es lo que la funcion CDT me va a devolver(mostrar) cuando la imprima en Consola(Terminal)
    # Un string que concatena(une los parámetros dentro del texto)
    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valorTotal}"


# Llamando a la función CDT para que se muestre en la terminal
##print(CDT("AB1012", 100000, 6))
#print(CDT("AB1012", 100000, 4))
print(CDT("ER3366", 650000, 2))