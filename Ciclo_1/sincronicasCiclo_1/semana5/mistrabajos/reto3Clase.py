# Semana 5 / 23 mayo 2022

ventas = [
    
    #Posición 0 de la lista
    # idProducto = 2001 / Este esta en la posicion 0 de la tupla
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    
    # Posición 1 de la lista
    # idProducto = 2010  / Este esta en la posicion 0 de la tupla
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    
    # Posición 2 de la lista 
    # idProducto = 2010  / Este esta en la posicion 0 de la tupla
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    
    #Posición 3 de la lista 
    # idProducto = 3578 / Este esta en la posicion 0 de la tupla
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    
    #Posición 4 de la lista 
    # idProducto = 9251 / Este esta en la posicion 0 de la tupla
    (9251,'piñón', 'EN5698',0,8,'Juan Peña',565,'12/06/2020')

]

def AutoPartes(ventas:list):
    
    #Variable con diccionario VACÍO 
    diccionario = {}
    
    
    #Recorre la lista de tuplas 
    for i in ventas:
        
        # Si la llave en la posición 0 es none, entonces se crea el diccionario
        if diccionario.get(i[0]) == None: 
        
            diccionario[i[0]] = [ ]
        
        diccionario[i[0]].append((i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        
                    
     #Retorna un diccionario con listas y dentro de ellas tuplas 
    return diccionario



def consultaRegistro(ventas, idProducto): 
    
    # Si el parámetro esta en el diccionario 
    if idProducto in ventas: 
        
        for i in ventas[idProducto]:
            
            print(f'Producto consultado : {idProducto}  Descripción  {i[0]}  #Parte  {i[1]}  Cantidad vendida  {i[2]}  Stock  {i[3]}  Comprador {i[4]}  Documento  {i[5]}  Fecha Venta  {i[6]}')

    else:
        print('No hay registro de venta de ese producto')
        

(consultaRegistro(AutoPartes(ventas), 20))
