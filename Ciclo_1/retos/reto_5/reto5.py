import pandas as pd
# ruta file 
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str) -> str:
   ruta = rutaFileCsv.split(".")
   if "csv" in ruta[-1]:
       try: 
          dataF = pd.read_csv(rutaFileCsv)
          # Hace un sub conjunto de el archivo 
          subDataF = dataF[["Country", "Language", "Gross Earnings"]]
          # Trae solo los indices que le indiquemos
          table = pd.pivot_table(subDataF, index = ["Country", "Language"])
          return table.head(10)
       except: 
           return f"Error al leer el archivo de datos"
   else:
        return f"Extensión inválida"
       

print(listaPeliculas(rutaFileCsv))
