from sys import argv

script, name = argv
prompt = '>_ '

print(f"Bienvenido {name}. Has ejecutado el programa {script}")

print(f"Ingrese su carrera")
carrera = input(prompt)

print(carrera)
