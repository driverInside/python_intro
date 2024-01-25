i = 0

numbers = []

while i < 10:
    #  print("Este print está dentro del while")
    i = i + 2
    numbers.append(i)
    
for j in numbers:
    print(f"{j}")
