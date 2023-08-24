#Ejercicio 1.
def area_rectangulo(base, altura):
    area = base * altura
    return area

print(area_rectangulo(4,5))


#Ejercicio 2.
PI = 3.14159

def area_circulo(radio):
    area = PI * (radio**2)
    return area

print(area_circulo(2))


#Ejercicio 3.
def relacion(num1,num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0
    
print(relacion(7,3))


#Ejercicio 4.
def intermedio(num1,num2):
    numIntermedio = (num1+num2) / 2
    return numIntermedio

print(intermedio(89,97))


#Ejercicio 5.
def recortar(nro,limInf,limSup):
    if nro < limInf:
        return limInf
    elif nro > limSup:
        return limSup
    else:
        return nro
    
print(recortar(23,20,30))
    