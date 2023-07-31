nombres = {"nombre1":2,"nombre2":10}

print(nombres)

print(nombres["nombre1"])

nombres["z"] = 30 #agregar un elemento en el ultimo indice


print(nombres)

print(nombres.get("nombre1"))

del nombres["z"]
print(nombres)


for valor in nombres:
    print(valor,nombres[valor])
    
for llave,valor in nombres.items():
    print(llave,valor)
