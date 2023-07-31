numeros = {1,2,3,4,5,5}
numeros2 = {6,7,8,9,1}
print(type(numeros))

numeros.remove(5)
numeros.add(10)
numeros.pop()
print(numeros)

print(numeros | numeros2) #union
print(numeros & numeros2) #interseccon
print(numeros - numeros2) #diferencia
print(numeros ^ numeros2) #diferencia simetrica