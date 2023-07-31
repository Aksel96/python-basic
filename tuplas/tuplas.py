numeros = (1,2,3,4,5)
print(numeros)

solo123 = numeros[0:3]
print(solo123)

primerelemetos, *otros = numeros

print(primerelemetos,otros)

for numero in numeros:
    print(numero)


