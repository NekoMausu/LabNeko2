
    
def menu():
    print("0: Выйти")
    print("1: Показать список контактов")
    print("2: Добавить контакт")
    print("3: Удалить контакт")
    print("5: Редактирование контакта")
    return int(input("Выберите пункт в меню: "))

def contacts_show(data):
    for i in enumerate(data):
        print(i)
    print('\n')



