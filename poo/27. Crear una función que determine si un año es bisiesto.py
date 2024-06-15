#27. Crear una función que determine si un año es bisiesto

def Año(A):

    if A%4 == 0:
        return A,"es un año bisiesto"
    else:
        return A,"no es un año bisiesto"
    
Año1 = Año(2020)
print(Año1)