#20. Crear una función que determine si un número es positivo, negativo o cero

def Num(x):
    if x > 0:
       return  x,"es positivo"
    elif x == 0:
        return "es 0"
    else:
        return x,"es negativo"
    
Num1 = Num(980)
print(Num1)