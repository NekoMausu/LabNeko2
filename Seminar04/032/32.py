# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

lst = [0, 1, 2, 2, 2, 3, 4, 1, 2]
lst2 = []
for i in lst:
    flag = 0
    for j in lst:
        if (i == j):
            flag += 1
    if (flag == 1):
        lst2.append(i)
print(lst2)