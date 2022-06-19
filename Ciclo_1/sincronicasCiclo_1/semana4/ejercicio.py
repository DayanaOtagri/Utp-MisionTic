# Semana 4 / 17 mayo 2022 
# Realice un programa que lea el código numérico de un producto como llave de un 
# diccionario y dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario, debe permitir consultar un producto 
# por su llave, actualizar precio y/o cantidad de un producto
# y eliminar productos

# Aplicación CRUD, create, read, update, delete

#Definimos las funciones 
def crear():
    codigo = int(input("Digite el codigo del producto: \n"))
    nombre = input("Digite el nombre del producto: \n")
    precio = int(input("Digite el precio uniterio del producto: \n"))
    cantidad = int(input("Digite el cantidad del producto: \n"))
    precioTotal = precio * cantidad
    productos[codigo] = [nombre, precio, cantidad, precioTotal]
    print("Producto creado: ", productos[codigo])
 
#Función que muestra el diccionario     
def mostrar():
    print("Listado de productos: ")
    print("Código", "Nombre", "Precio", "Cantidad", sep="\t\t")
    for i in productos:
        print(i, productos[i][0], productos[i][1], productos[i][2], sep="\t\t")

def consultar():
    codigo = int(input("Digite el código del producto que desea consultar: \n"))
    if codigo in productos:
        print("Código", "Nombre", "Precio", "Cantidad", sep="\t\t")
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2], sep="\t\t")
    else:
        print("No es un código valido")
    
def actualizar():
    codigo = int(input("Digite el código del producto que desea actualizar: \n"))
    if codigo in productos:
        precio = int(input("Digite el nuevo precio del producto: \n"))
        cantidad = int(input("Digite la cantidad actualizada del producto: \n"))
        productos[codigo][1] = precio
        productos[codigo][2] = cantidad
        print("Producto actualizado: " + productos[codigo])
    else:
        print("El código del producto no existe")
        
def borrar():
    codigo = int(input("Digite el código del producto que desea eliminar \n "))
    if codigo in productos:
        print("Producto eliminado:", productos.pop(codigo))
    else: 
        print("El código del producto no existe")

#Diccionraio
productos ={
    1: ['manzana', 2500, 60],
    2: ['pera', 2800, 85],
    3: ['banana', 500, 680]   
}

#Consulta al usuario la opción que desean
continuar = 's'
while continuar == 's' or continuar == 'S':
  
    try:
        print("Menú: \n", "1. crear", "2.Mostrar", "3.Consultar", "4.Actualizar", "5.Eliminar", sep="\t")
        
        opcion = int(input('Digite una opción [1/2/3/4/5]:\n' ))
        if opcion == 1:
            crear()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            consultar()
        elif opcion == 4:
            actualizar()
        elif opcion == 5:
            borrar()
        else:
            print('Digite una opción valida')
            
    except: 
        print('Digite una opción valida')        
    continuar = input('Digite "s" para continuar o culquier tecla para salir\n')