"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
year = {"зима": [12, 1, 2],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11]}
month = int(input("Введите месяц: "))

for key, value in year.items(): # получаем ключ значение
    if month in value: # проверяем месяц в значение
        print(key) # выводим ключ который соответсвут значению
        break # выходим из цикла
