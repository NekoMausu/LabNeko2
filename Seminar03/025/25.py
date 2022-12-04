# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
def bin (num):
    result=[]
    while(int(num)!=0):
        result.insert(0,int(num%2))     
        num/=2
    return result

n=int(input("n= "))
print(f"{bin(n)}")
