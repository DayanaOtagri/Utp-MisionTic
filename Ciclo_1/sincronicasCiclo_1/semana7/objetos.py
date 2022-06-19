# 7 mayo 2022 
# Programación Orientada a Objetos 
# Python es un lenguaje orientado a objetos
# En Python casi todo es un objeto
# Una clase es un modelo, patrón o plantilla de la cual se crean objetos
# Al crea una clase se definen: 
#   Los atributos o caracteristicas -> variables
#   Los métodos -> funciones

# Crear una clase: 
class Persona: 
    
    #  métodos 
    def crear(self, nombre:str):
        self.name = nombre 
        
    def mostrar(self)->str:
        return self.name
    
    
# instancio a Persona 
instancia = Persona()
print(type(instancia))
instancia.crear("Maria")
print(instancia.mostrar())


# El método __init__ es un método especial
# Este método se ejecuta automaticamente 
# cuando se crea el objeto (es el constructor)

#self siempre tiene que ser el primer parámetro 
class Estudiante: 
    def __init__(self): 
        self.nombre = input("Digite el nombre del estudiante: \n ")
        self.materia = input("Digite la materia: \n ")
        self.nota = float(input("Digite la nota del estudiante: \n "))
    def imprimir(self):
        print("Nombre: ", self.nombre) 
        print("Materia: ", self.materia)
        print("Nota:", self.nota)  
    def aprobar(self):
        if self.nota >= 3.0:
            print("Aprobó")
        else: 
            print("Reprobó")
        
        
estudiante1 = Estudiante()        
estudiante1.imprimir() 
estudiante1.aprobar() 