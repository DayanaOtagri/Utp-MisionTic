# Función que tiene como parámetro un diccionario 
def cliente (informacion:dict): 
    
    # Estas son las condiciones cuando el primer_ingreso es FALSE  y NO APLICA DESCUENTO:
    # Si la edad de la persona es mayor a 18 Y no es el primer_ingreso:
    if (informacion["edad"] > 18 and informacion["primer_ingreso"] == False):
        
        #Valores que tomaras las llaves: 
        atraccion = "X-Treme"
        apto =  True
        total_boleta = 20000 
        
    # Si la edad de la persona es mayor o igual a 15 Y la edad es mayor o igual a 18 Y no es el primer_ingreso
    elif ((informacion["edad"] >= 15 and informacion["edad"] <= 18 ) and informacion["primer_ingreso"] == False):
        
        #Valores que tomaras las llaves: 
        atraccion = "Carros chocones"
        apto =  True
        total_boleta = 5000
        
    # Si la edad de la persona es mayor o igual a 7 Y la edad es mayor o igual a 15 Y no es el primer_ingreso
    elif ((informacion["edad"] >= 7 and informacion["edad"] <= 15 ) and informacion["primer_ingreso"] == False):
        
        #Valores que tomaras las llaves: 
        atraccion = "Sillas voladoras"
        apto = True
        total_boleta = 10000
        
        
    
    # Estas son las condiciones cuando el primer_ingreso es TRUE y aplica DESCUENTO:
    #Si la edad de la persona es mayor a 18 Y es el primer_ingreso:
    elif (informacion["edad"] > 18 and informacion["primer_ingreso"] == True):
        
        #Valores que tomaras las llaves: 
        atraccion = "X-Treme"
        apto =  True
        boletaDescuento = 20000 * 0.05 
        total_boleta = 20000 - boletaDescuento
        
    # Si la edad de la persona es mayor o igual a 15 Y la edad es mayor o igual a 18 Y es el primer_ingreso   
    elif ((informacion["edad"] >= 15 and informacion["edad"] <= 18 ) and informacion["primer_ingreso"] == True):
        
        #Valores que tomaras las llaves: 
        atraccion = "Carros chocones"
        apto =  True
        boletaDescuento = 5000 * 0.07
        total_boleta = 5000 - boletaDescuento
        
    # Si la edad de la persona es mayor o igual a 7 Y la edad es mayor o igual a 15 Y es el primer_ingreso
    elif ((informacion["edad"] >= 7 and informacion["edad"] <= 15 ) and informacion["primer_ingreso"] == True):
        
        #Valores que tomaras las llaves: 
        atraccion = "Sillas voladoras"
        apto = True
        boletaDescuento = 10000 * 0.05
        total_boleta = 10000 - boletaDescuento
        
    # De no cumplir con ninguna de las condiciones dadas entonces estos serán los valores que tomaran las llaves:    
    else: 
        atraccion = "N/A"
        apto = False
        total_boleta = "N/A"
        
    # Crea un nuevo diccionario
    nuevaInformacion = {
        "nombre": informacion["nombre"],
        "edad": informacion["edad"],
        "atraccion": atraccion,
        "apto": apto,
        "primer_ingreso": informacion["primer_ingreso"],
        "total_boleta": total_boleta
        }
    
    # Retorna el nuevo diccionario
    return nuevaInformacion
    
# Pruebas con cada diccionario de informacion  
"""informacion = {
    "id": 1,
    "nombre": "Johana Fernandez",
    "edad": 20,
    "primer_ingreso": True 
}
"""

 
"""informacion = {
    "id": 1,
    "nombre": "Johana Fernandez",
    "edad": 20,
    "primer_ingreso": False 
} """

"""informacion = {
    "id": 2,
    "nombre": "Gloria Suarez",
    "edad": 3,
    "primer_ingreso": True 
}"""

"""informacion = {
    "id": 3,
    "nombre": "Tatiana Suarez",
    "edad": 17,
    "primer_ingreso": True 
}"""

"""informacion = {
    "id": 3,
    "nombre": "Tatiana Suarez",
    "edad": 17,
    "primer_ingreso": False 
}"""

informacion = {
    "id": 4,
    "nombre": "Tatiana Ruiz",
    "edad": 8,
    "primer_ingreso": True 
}


"""informacion = {
    "id": 3,
    "nombre": "Tatiana Suarez",
    "edad": 8,
    "primer_ingreso": False 
}"""


# Llamado a la función para que se imprima en la Terminal. 
# Recibe como argumento el diccionario
print(cliente(informacion))