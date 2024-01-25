from sys import argv

script, filename = argv

print(f"Bienvenido. Borremos el archivo {filename}")
print("Presione enter para continuar")

input("_")

# Le puedo poner el nombre que yo quiera a mi variable
target = open(filename, "w")

print("Borrando el archivo...")
target.truncate()

print("Ingresando líneas de texto")

linea1 = input("Linea 1: ")
linea2 = input("Linea 2: ")
linea3 = input("Linea 3: ")

# El método write escribe en el archivo
target.write(linea1)
target.write("\n")
target.write(linea2)
target.write("\n")
target.write(linea3)
target.write("\n")

print("Cerrando el archivo")
target.close()
