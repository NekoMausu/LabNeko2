# Задайте список из n чисел последовательности (1 + 1/n)^n
#  и выведите на экран их сумму.
sum=0
n = int(input("n= "))
for i in range(1, n+1):

    b = (1+1/i)**i
    print(f"{i} = {b}")
    sum+=b
    b = 0
print(f"sum= {sum}")
    
