from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copiando del archivo {from_file} al archivo {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"El archivo fuente tiene una longitud de {len(in_data)} bytes")

print(f"¿Existe el archivo destino? {exists(to_file)}")

out_file = open(to_file, "w")
out_file.write(in_data)

print("Operación realizada con éxito")

in_file.close()
out_file.close()
