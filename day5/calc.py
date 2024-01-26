import mate

print("Inserte un valor para a: ", end=' ')
a = int(input())
print("Escriba un valor para b: ", end=' ')
b = int(input())

suma = mate.sum(a, b)
print(f"La suma es igual a {suma}")

dif = mate.sub(a, b)
print(f"El resultado de la resta es {dif}")

prod = mate.mult(a, b)
print(f"El producto es igual a {prod}")

coc = mate.div(a, b)
print(f"El cociente es igual a {coc}")

print(f"El valor para PI está definido como {mate.PI}")

lista = []
sm = None

sm = mate.smallest(lista)
print(f"El más pequeño es: {sm}")

lista = [2]
sm = mate.smallest(lista)
print(f"El más pequeño es: {sm}")

lista = [8, 6 , 11, 45, 7, 4, 66, 89]
sm = mate.smallest(lista)
print(f"El más pequeño es: {sm}")

lista = [8, 6 , 4, 11, 45, 7, 4, 66, 89]
sm = mate.smallest(lista)
print(f"El más pequeño es: {sm}")
