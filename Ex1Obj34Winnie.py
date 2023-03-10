# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

# а и е ё о у ы э ю я


# Импорт функции.
import os

os.system('cls')
# Пример гласных.
example = 'аиеёоуыэюя'
# Введенный стих с разбитием на элементы.
list_str = 'пара-па-рам рам-пам-рапам па-ра-ра-пам рам-пам-папам папам-рам-пам рапам-папам'.split()
print(list_str)
# Список для подсчета.
list_len = []
# Основная функция подсчета гласных.
for i in list_str:
    list_vowels = list(filter(lambda x: x in example, i))
    list_len.append(len(list_vowels))
# Вывод данных.
print('Парам пам-пам' if len(set(list_len)) == 1 else 'Пам парам')
