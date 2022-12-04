# Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
lst = [0,1]
i=0
n = int(input("n= "))
while (i<(n-1)*2): 
    lst.append(f"{int(lst[i])+int(lst[i+1])}")
    lst.insert(0,int(lst[i+1]))
    i+=2
lst.insert(0,int(lst[i+1]))
if (n%2==0):
    while (n>0):
        if ((n-1)%2==0):
            lst[n-1]=-lst[n-1]
        n-=1
else:
    while (n>0):
        if ((n-1)%2!=0):
            lst[n-1]=-lst[n-1]
        n-=1
print(lst)
