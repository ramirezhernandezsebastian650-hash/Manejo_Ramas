cuantos = int(input("Cuantos usuarios quiere crear?"))

usuarios = []
for i in range(cuantos):
    nombre = input("Inserte el nombre del suario: ")
    usuarios.append(nombre)
print(usuarios)