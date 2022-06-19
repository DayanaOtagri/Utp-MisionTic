import pandas as pd 

diccionraio =  {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
        }

dataF = pd.DataFrame(diccionraio)
print(dataF, "\n" )

# Para crear un CSV utilizo el to.csv 
# (nombre que le quiero poner al archivo)
# Si quiero agregarlo a una ruta especifica con doble \\
# C:\\Users\\heidy\\Desktop\\UTP-MINTIC\\Ciclo_1\\sincronicasCiclo_1\\semana6\\datos.csv
dataF.to_csv("datos.csv")
