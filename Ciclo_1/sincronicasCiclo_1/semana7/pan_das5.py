# Semana 7 / June 6th, 2022
import pandas as pd

diccionario = {
    'Nombre': ['Laura','Laura','Laura','Laura','Juan','Juan','Juan','Juan'],
    'Fecha':['03/05/2022','04/05/2022','05/05/2022','05/05/2022','03/05/2022','04/05/2022','05/05/2022','05/05/2022'],
    'Cantidad': [8,2,5,6,8,7,1,2]   
}


data = pd.DataFrame(diccionario)
#print(data)

# tabla dinámica = pivot table
tablaDinamica = pd.pivot_table(data, index =  "Nombre")
print(tablaDinamica)

