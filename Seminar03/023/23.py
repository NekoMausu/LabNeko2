# Напишите программу, которая найдёт 
# произведение пар чисел списка. Парой считаем первый и 
# последний элемент, 
# второй и предпоследний и т.д.

count=0
lst = [i for i in range(1,6)]
print(lst)
while(round(len(lst)-1)/2>count):
    print(f"{count+1} пара = {lst[count]+lst[-(count+1)]}")
    count+=1

