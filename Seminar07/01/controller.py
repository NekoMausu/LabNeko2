from view import contacts_show
from modul import contacts


def contact_add():
    print("\nДобавление контакта\nВведите -1 для выхода в меню")
    key_fio = input("FIO: ")
    if (key_fio == '-1'):
        return
    key_number = input("Number: ")
    if (key_number == '-1'):
        return
    contacts.append({f'{key_fio}': f"{key_number}"})


def contact_remove():
    while True:
        print("\nУдаление контакта\nВведите -1 для выхода в меню")
        key_index = int(input("index of FIO: "))

        if (key_index > len(contacts)-1 or key_index < -1):
            print("Ошибка, неверный индекс")
            continue
        if (key_index == -1):
            return
        del contacts[key_index]


def contact_change():
    while True:
        print("\nИзменение контакта\nВведите -1 для выхода в меню")
        key_index = int(input("index of FIO: "))
        if (key_index > len(contacts)-1 or key_index < -1):
            print("Ошибка, неверный индекс")
            continue
        if (key_index == -1):
            return
        key_FIO = input("FIO: ")
        new_number=input("New number: ")
        contacts[key_index][key_FIO] = f"{new_number}"


def operations(choise):
    if (choise == 0):
        exit()
    if (choise == 1):
        contacts_show(contacts)
    if (choise == 2):
        contact_add()
    if (choise == 3):
        contact_remove()
    if (choise == 5):
        contact_change()
