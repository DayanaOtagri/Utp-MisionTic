# Realizar un programa que indique si una persona debe 
# presentar la declaracion de renta. Las conodiciones son:
# Ser mayor de edad y tener ingresos anuales superiores o iguales a $50.831.000 

def renta(edad, ingresos): 
    if edad >= 18 and ingresos >= 50831000:
        return f"Usted debe declarar renta"
    else:
        return f"Usted no debe declarar renta"
    
print(renta(12, 7000))
print(renta(60, 7000000000))
print(renta(40, 1800000))
print(renta(25, 5000000))