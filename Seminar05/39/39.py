# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

import random

def candy_game():
    total_candy = 200
    flag = random.randint(0, 1)
    while (total_candy > 28):
        ai_take_candy = random.randint(1, 28)
        player = 'AI' if flag == 0 else "Player"
        print(f"Конфет осталось: {total_candy}")
        if (flag == 0):
            print(f"Ход делает {player}: ")
            print("Возьмите от 1 до 28 конфет")
            print(f"Конфет взято игроком {player}: {ai_take_candy}")
            total_candy -= ai_take_candy
        else:
            print(f"Ход делает {player}: ")
            print("Возьмите от 1 до 28 конфет")
            take_candy = int(input(f"Конфет взято игроком {player}: "))
            total_candy -= take_candy
        print('\n')
        flag = 1 if flag == 0 else 0
    print(f"Конфет осталось {total_candy}")
    print(f"Победитель {player} ")

candy_game()