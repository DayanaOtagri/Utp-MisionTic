#Semana 5 / 23 mayo 2022
# *arg  permite pasar un n cantidad de argumentos


def suma(*args):
    
    #Contador en 0 
    total = 0
    
    for i in args:
        total += i
    return total
    
    # return sum(args)

print(suma(4,5,6,7,8,9,10,11,12,13,14,))

# **kwargs lo que llega es un diccionario llave : valor
def suma2(**kwargs):
    return sum(kwargs.values())