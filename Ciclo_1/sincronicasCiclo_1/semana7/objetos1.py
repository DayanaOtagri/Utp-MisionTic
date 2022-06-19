# 8th June, 2022
# Herencia 
# Existen varias relaciones entre las clases, una de ellas es la herencia 
# Se puede definir una clase que herede las propiedades y métodos de otra clase
# Clase padre (Clase principal) es aquella de la que se hereda
# Clase hija (Clase secundaria) es la clase que hereda 

class Persona: #Clase padre 
    
    # Constructor 
    def __init__(self, nombre:str, apellido:str, edad:int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    #Método    
    def imprimir(self):
        print(self.nombre,self.apellido,self.edad)
        
        
p1 = Persona("Alejandro", "Castro", 18)
p1.imprimir 


class Estudiante(Persona): #Clase hija 
    
    #Método propio de la clase hija 
    def saludo(self): 
        print(f" ¡Hola {self.nombre}!")


e1= Estudiante("Carlos", "Perez", 30)
e1.imprimir()
e1.saludo()