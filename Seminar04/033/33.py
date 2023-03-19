# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.


data = open('file.txt', 'w')
import random
flag = random.randint(1, 3)
k = input("k= ")
if (flag == 1):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    print(f"{a}x**{k}+{b}x+{c}=0")
    data.write(f"{a}x**{k}+{b}x+{c}=0")
elif (flag == 2):
    c = random.randint(0, 100)
    print(f"x**{k}+{c}=0")
    data.write(f"x**{k}+{c}=0")
else:
    a = random.randint(0, 100)
    print(f"{a}x**{k}=0")
    data.write(f"{a}x**{k}=0")
data.close()