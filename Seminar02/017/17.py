# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в
# одной строке одно число.

n = int(input("n= "))
summ=1
path = 'file.txt'
data = open(path, 'r')
lis=[i for i in range(-n,n+1)]
for a in data:
    summ*=lis[int(a)]
print(f"произведение= {summ} ")
data.close()
