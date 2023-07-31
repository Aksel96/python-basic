usuarios = [["Alberto",1],["Raul",2],["Alejandro",3]]

#nombre = []

#for usuario in usuarios:
#    nombre.append(usuario[0])
#print(nombre)

#Otra forma de obtener indices de una lista
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

#Filtrar
filtrar = [usuario for usuario in usuarios if usuario[1] > 1]

print(filtrar)
