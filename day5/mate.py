# Para definir una función, utilizamos "def"

PI = 3.1415927

def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if (num2 == 0):
        print("División por cero. El segundo parámetro no debe de ser cero")
        return
    
    return num1 / num2

#  v                 
# 15, 6, 64, 8, 14, 33
def smallest(nums):
    if (len(nums) == 0):
        print("La lista debe tener al menos un elemento")
        return
    
    sm = nums[0]
    
    for num in nums:
        if num < sm:
            sm = num
    
    return sm
    

    