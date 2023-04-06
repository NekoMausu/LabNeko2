# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compression(tx):
    count = 0
    current = tx[0]
    coding = ''
    for i in tx:
        if (i != current):
            coding = coding + str(count) + current
            current = i
            count = 0
        if (i == current):
            count += 1
    coding = coding + str(count) + current
    print(f"{coding}")
    return (coding)

def decompression(tx):
    uncoding = ''
    b = 0
    n = 0
    i = 0
    j = 1
    while (b < (len(tx)/2)):
        while (int(tx[i]) > n):
            uncoding = uncoding + f'{tx[j]}'
            n += 1
        n = 0
        i+=2
        j+=2
        b+=1
    print(uncoding)
    return(uncoding)

data=open('file3.txt','r+')
data.write(f'\n{compression(data.read())}')