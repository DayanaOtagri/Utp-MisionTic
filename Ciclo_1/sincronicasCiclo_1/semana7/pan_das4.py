# Semana 7 / June 6th, 2022

import pandas as pd
dataF = pd.read_csv("surveys.csv")

# Hacer subConjuntos 
# SubConjuntos por Columna
dF = dataF["month"]
#print(dF, type(dF))

df3 = dataF[["species_id", "plot_id"]]
#print(df3, type(df3))

#print(dataF[15:26])
#print(dataF.iloc[0,4,5,6,7])
#print(dataF.iloc[[2,4,6], 1:4])
#print(dataF[dataF.year == 1985].to_String())
print(dataF[(dataF.year >= 1985) & (dataF.year <= 1990)]) # cuando se utiliza pandas: and = &, or = |, not = ~ 