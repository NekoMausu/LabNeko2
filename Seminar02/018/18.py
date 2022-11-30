# Реализуйте алгоритм перемешивания списка.

import random
a = ["1", "2", "3", "4", "5", "6"]
for i in a:
    f1 = random.randint(0, len(a)-1)
    f2 = random.randint(0, len(a)-1)
    a[f1], a[f2] = a[f2], a[f1]
print(a)
