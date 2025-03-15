# Dima Pilipenka

# Date: 12/10/2024
# Description: Homework 2
# Grodno IT Academy Python 3.10

# Чтобы запустить тесты и проверить выполнение домашнего задания:
# 

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов/входные данные. Можно менять решение, менять/добавлять return.

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown
# В репозитории не должно быть лишних папок и файлов: файлов IDE, виртуального окружения и тд
# ДЗ не коммититься в ветку main(master)! 

# Вы создаете репозиторий с ДЗ приватным. Чтобы добавить меня к репозиторию: нужно в настройках репозитория добавить collaborator:
# И ввести мой логин в github: karturik


# Напишите программу, ĸоторая считает общую цену.
# Передается m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)

from decimal import Decimal

def common_price(m, n, s, l):
    common_price=Decimal(m)+Decimal(n)/100
    common_price*=s*l
    
    
    common_rables=int(common_price)
    common_kopeks=int((common_price-common_rables)*100)
    return f"Общая цена состовляет{common_rables} рублей и  {common_kopeks} копеек за один{l} товар "
    m=5
    n=20
    s=2
    l=3
    rezult=common_price(m,n,s,l)
    print(rezult)
    
    
    
   



# В функцию передаются аргументы: a, b, c - длины сторон треугольника.
# Требуется: проверить, может ли существовать треугольник с такими длинами сторон.
# Если может - найти его площадь с точностью до четырёх десятичных и вернуть площадь (return).
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если такой треугольник существовать не может - функция должна вернуть False.

def trilangle(a,b,c):
        if a + b > c and a + c > b and b + c > a:  # Проверка условия существования треугольника
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            return round(area, 4 ) # Округляем площадь до четырех десятичных
        else:
            return False
        
        
a = 2
b = 2
c = 2

result=trilangle(a, b, c)
if result:
    print(f"Площадь треугольника  длинами сторон {a}, {b}, {c} равна {result}")
        
else:
    
    print("Треугольник c такими сторонами не существует")


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если передано "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"

import string
def longest_word(sentence):
    translator = str.maketrans('','', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    words = cleaned_sentence.split()
    longest = max(words, key=len)
    return longest

input_sentence = "This is a sample sentence where the longest word is in the middle"

print(longest_word(input_sentence))

# Передается строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было передано "abc cde def", то должно быть выведено "abcdef".

def uniques(repeating_string):
    # Удаляем пробелы
    repeating_string = repeating_string.replace(" ", "")
    # Сохраняем порядок символов с помощью списка
    unique_chars = []
    for carh in repeating_string:
        if char not in unique_chars:
            unique_chars.append(char)
    # Объединяем уникальные символы в строку
    return ''.join(unique_chars)

#  Использования
result = uniques("abc cde def")
print(result)  

# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.

def count_string_capitalization(mixed_string):
    lowercase_count = 0
    uppercase_count = 0
    
    for char in mixed_string:
        if char.islower():  # Проверка на строчные буквы
            lowercase_count += 1
        elif char.isupper():  # Проверка на прописные буквы
            uppercase_count += 1
            
    return lowercase_count, uppercase_count

# Пример 
result = count_string_capitalization("Hello World!")
print(result)
