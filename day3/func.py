def sum(arg1, arg2):
    print(f"La suma de {arg1} más {arg2} es igual a {arg1 + arg2}")
    
def sum_two(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def saludo(name):
    str = f"Hola {name}"
    print(str)
    
def foo(arg1, arg2, arg3):
    return (arg1 + arg2) / arg3

def print_line(ch = "_", length = 10):
    print(f"{ch * length}")
    
def print_two(*args):
    arg1, arg2 = args
    
    print(f"el primer arg = {arg1}, el seg es {arg2}")
    
print("Ejecutando mi función...")
sum(2, 3)

print("Ejecutando mi segunda función")
result = sum_two(8, 11) # 19

print(f"El resultado de la suma es {result}")

print(f"El resultado de dividir 0 / 0 es {div(120, 3)}")

saludo("Beto")

print(f"Llamando a mi función foo: {foo(8, 9, 3)}")

print_line("e")
print_line()
print_line("-", 3)
print_line("a", 7)


print_two("Hola",  "Hiram")
