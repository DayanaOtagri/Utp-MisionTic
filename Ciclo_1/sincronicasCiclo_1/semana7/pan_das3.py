# Semana 7 / June 6th, 2022
import pandas as pd
dataF = pd.read_csv("surveys.csv")

#print(dataF)
#print(dataF.head(10)) # Imprime las primeras n filas
#print(dataF.tail(8)) # Imprimer las últimas n filas
#print(dataF.shape) # Es un método 
#print(dataF.columns) # un array con el nombre de cada columna
#print(pd.unique(dataF["species_id"])) # Retorna una lista con los valores únicos de una columna
#print(dataF["species_id"].value_counts()) # Cuenta la cantidad por valores únicos de la columna
#print(dataF["weight"].describe()) # Devuelve datos de estadística descriptiva
#print(dataF["weight"].max()) # Máximo - estadística 
#print(dataF.groupby("species_id").count())
print(dataF.groupby("species_id")["record_id"].count()["AH"]) 
