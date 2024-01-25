ages = [19, 19, 20, 21, 18, 17, 20, 25]


print(f"El siguiente bloque se ejecutará {len(ages)} veces")
for age in ages:
    if age < 18:
        print(f"Este alumno es menor de edad: {age}")

grades = [9, 7, 7, 5, 6, 7, 10, 5, 5, 9, 6, 6]

sum = 0
counter = 0
for g in grades:
    sum = sum + g
    
    if g < 6:
        counter = counter + 1
        print("Este alumno está reprobado")

average = sum / len(grades)

print(f"El número total de calificaciones fue de: {len(grades)}")
print(f"El promedio de calificaciones fue: {average}")                
print(f"En este grupo hay {counter} reprobados")
#           0       1        2         3
colors = ["red", "yellow", "white", "orange"]

for color in colors:
    print(color)

#          0    1    2    3       4     5  6
numbers = [1, "two", 3, "four", "five", 6, 7]

str_numbers = ""
for number in numbers:
    str_numbers = str_numbers + " " + f"{number}"
    # print(f"{number}")
print(str_numbers)

elements = []
print(f"Al inicio mi lista de elementos tiene {len(elements)} elementos")
for i in range(1, 6):
    print(f"Metiendo {i} a la lista de elementos")
    elements.append(i)
    
print(f"Ahora mi lista tiene {len(elements)} elementos")
print(f"el primer elemento es: {elements[0]}")

print("Fin del código")