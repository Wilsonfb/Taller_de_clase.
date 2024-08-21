# Elabore un algoridmo que calcule el promedio de las edades de la ficha, subir a la segunda rama.
cantidad = int(input("Digite la cantida de estudiantes: "))
promedio = 0
lista = []
while True:
    for i in range (cantidad):
        edad = int(input("Digite la edad del estudiante: "))
        lista.append(edad)
    promedio = (cantidad / lista)
    print(f"El promedio de las edades de la ficha es de: {promedio}. ") 