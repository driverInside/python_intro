import math
'''
calcular las raices de ax^2 + bx + c


'''
print("Inserte un valor para a: ", end=' ')
a = int(input())
print("Escriba un valor para b: ", end=' ')
b = int(input())
print("Ingrese un valor para c:", end=' ')
c = int(input())

d = (b * b) - 4 * (a * c)

if d > 0:
    print("Calculando x1 y x2")
    e = math.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    
    print(f"Las raices de la ec son: x1 {x1} y x2 {x2}")
elif d == 0:
    print("Existe solo una raíz real")
else:
    r = -b / (2 * a)
    im = math.sqrt(-d) / (2 * a)
    
    x1 = f"{r} + {im}i"
    x2 = f"{r} - {im}i"
    
    print(f"Las raices son: x1 {x1} y x2 {x2}")
