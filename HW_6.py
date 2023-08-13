# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

#while True:
#    user_input = input("Введите первый элемент, разность и количество элементов прогрессии (через пробел)! : ").split()
#    if len(user_input) == 3:
#        break

#first_el, difference, amount = int(user_input[0]), int(user_input[1]), int(user_input[2]) - 1

#result = []
#result.append(first_el)

#for i in range(0, amount):
#    result.append(result[i] + difference)

#print(result)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
#Ввод:
#3 4 2 5 7
#[4,6]
#Вывод:
#1, 3

#n, arr, res = int(5), [], []

#while n > 0:
#    a = int(input('Введите элемент массива : '))
#    arr.append(a)
#    n -= 1

#max_val, min_val = int(input('Введите максимум : ')), int(input('Введите минимум : '))

#for i in range(1,len(arr)):
#    if arr[i] >= min_val and arr[i] <= max_val:
#        res.append(i)

#print(res)