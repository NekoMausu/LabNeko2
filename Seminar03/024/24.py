# Задайте список из вещественных чисел. Напишите 
# программу, которая найдёт разницу между максимальным 
# и минимальным значением 
# дробной части элементов.
lst = [3.25, 6.40, 1.50]
min_num=lst[0]-int(lst[0])
max_num=lst[0]-int(lst[0])
for item in lst:
    if(min_num>item-int(item)):
        min_num=item-int(item)
    if(max_num<item-int(item)):
        max_num=item-int(item)
print(max_num-min_num)