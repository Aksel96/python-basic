def suma(a,b):
    print(a+b)
    
suma(1,2)

def suma2(*numeros):
    resultado = 0
    for numero in numeros:
        resultado = resultado + numero
    print(resultado)

suma2(1,2,3,4,5,6)