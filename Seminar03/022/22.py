# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
num=0
result=0
lst = [i for i in range(0,11)]
print(lst)
while (num<len(lst)):
    if (num%2!=0):
        result+=lst[num]
    num+=1
print (result)