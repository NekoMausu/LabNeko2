# Создайте программу для игры в "Крестики-нолики"

import random
ar = " 0 1 2\n 3 4 5\n 6 7 8\n"
print(ar)
flag = random.randint(0, 1)
i = 0
while (i != 9):
    player = 'AI (O)' if flag == 0 else "Player (X)"
    print(f"{player} выберите позицию")
    choise = int(input(f"{player} выбрал позицию: "))
    if (choise < 0 or choise > 9) or (ar.split()[choise] == 'X') or (ar.split()[choise] == 'O'):
        print("//////////////////////////\nОШИБКА, ПОВТОРИТЕ ДЕЙСТВИЕ\n//////////////////////////")
        print(ar)
        continue
    if (flag == 1):
        ar = ar.replace(f'{choise}', 'X')
    else:
        ar = ar.replace(f'{choise}', 'O')
    print(ar)
    if (ar.split()[0] == ar.split()[1] == ar.split()[2]) or\
            (ar.split()[3] == ar.split()[4] == ar.split()[5]) or\
            (ar.split()[6] == ar.split()[7] == ar.split()[8]) or\
            (ar.split()[0] == ar.split()[3] == ar.split()[6]) or\
            (ar.split()[1] == ar.split()[4] == ar.split()[7]) or\
            (ar.split()[2] == ar.split()[5] == ar.split()[8]) or\
            (ar.split()[0] == ar.split()[4] == ar.split()[8]) or\
            (ar.split()[2] == ar.split()[4] == ar.split()[6]):
        print(f"Победитель {player}")
        break
    flag = 1 if flag == 0 else 0
    i += 1
    if (i == 9):
        print("Ничья")
