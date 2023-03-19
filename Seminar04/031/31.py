# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('n= '))
lst = [i for i in range(2, n+1)]
count = 0
p = lst[count]
while (p**2 < n):
    i = count+1
    j = 0
    while (i < len(lst)):
        if (lst[i] % p == 0):
            lst.remove(lst[i])
        i += 1
    count += 1
    p = lst[count]
print(lst)
