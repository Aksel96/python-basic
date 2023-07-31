usuarios = [["Alberto",1],["Raul",2],["Alejandro",3]]

nombres = list(map(lambda usuario: usuario[0],usuarios))

print(nombres)

menosusuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(menosusuarios)


