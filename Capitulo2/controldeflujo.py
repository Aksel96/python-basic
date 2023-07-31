edad = int(input("Ingrese la edad: "))
if edad > 0 or edad < 18:
    print("Eres menor de edad")
elif edad < 0:
    print("Ingresa una edad verdadera")
elif edad > 120:
    print("Ingresa una edad verdadera")
else:
    print("Eres mayor de edad")