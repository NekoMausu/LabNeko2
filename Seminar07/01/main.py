#Создать телефонный справочник с возможностью импорта и экспорта
#данных в нескольких форматах
#ТЗ
#Операции с телефонным справочником:
#1. Вывод контактов
#2. Добавление контафта ФИО и телефон
#3. Удаление контакта
#4. Поиск контакта по имени и вывести список найденных контаков с заданным именем
#5. Выгрузка в формате CSV,txt или JSON (экспорт)
#6. Загрузка списка контактов из файлика выбранного формата
#7. Редактирование контакта

from view import menu
from controller import operations

while True:
   operations(menu())
    

