# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
data = open('file.txt', 'r')
data2 = open('file2.txt', 'r')
lst = data.read().splitlines()
a=0
for line in lst:
    a+=int(line)

print(a)
