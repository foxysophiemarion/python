# print("Введите первое число: ")

# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, ' + ', b, ' = ', a + b)


# a = 5.6262
# b = 6.325235
# print(round(a*b, 3))  # округление


# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter = iter - 3
# iter *= 5  # iter = iter * 3
# iter /= 5  # iter = iter / 3
# iter //= 5  # iter = iter // 3
# iter %= 5  # iter = iter % 3
# iter **= 5  # iter = iter ** 3


# Логические операции
# > Больше
# >= Больше или равно
# < Меньше
# <= Меньше или равно
# == Равно (проверяет, равны ли числа)
# != Не Равно (проверяет, не равны ли значения)
# not Не(отрицание)
# and И(коньюкция)
# or Или(дизконьюкция)


# a = 1 > 4
# print(a)  # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 2
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10 > 5
# print(a)  # True


# "if/if-else"

# if condition:
#    operator 1
#    operator 2
# else
#    operator n + 1
#    operator n + 2


# "else-if(elif)""

# if condition1:
#    operator
# elif condition1:
#    operator
# elif condition3:
#    operator
# else:
#    operator


# Сложные условия and, or, not

# if condition1 and condition2 # выполняется, когда оба условия верны
#    operator
# if condition1 or condition2 # выполняется, когда хотя бы одно из условий окажется верным
#    operator


# username = input('Введите имя: ')
# if username == 'Маша':
#    print('Удали свое имя!')
# elif username == 'Марина':
#    print('Твое имя ничто!')
# elif username == 'Глеб':
#    print('Вы лучший!')
# else:
#    print('Привет, ', username)


# Цикл While
# while condition:
#    operator1
#    operator2

# Пример
# n = 563
# summa = 0
# while n > 0:
#    x = n % 10
#    summa = summa + x
#    n = n//10
# print(summa)  # 9


# While-else

# while	condition:
#    operator 1
#    operator2
# else:
#    operator n+1
#    operator n+2

# Блок esle выполняется, когда основное тело цикла перестает работать самостоятельно, с помощью конструкции brak

# Пример
# i = 0
# while i < 5:
#    if i == 3:
#        break
#    i = i+1
# else:
#    print('Пожалуй')
#    print('хватит )')
# print(i)


# n = int(input())
# flag = True
# i = 2
# while flag:
#    if n % i == 0:  # если остаток при делении числа n на i равен 0
#        flag = False
#        print(i)
#    elif i > n // 2:  # делитель числа не может превышать введеное число, деленое на 2
#        print(n)
#        flag = False
#    i += 1


# Цикл for, фунцкия range()
# Range выдает значения из диапазона с шагом 1.
# Если указано только одно число - от 0 до заданного числа
# Если нужен другой шаг, третьим аргументом можно задать приращивание
# ПРИМЕР
# r = range(5)  # 0 1 2 3 4
# r = range(2, 5)  # 2 3 4
# r = range(0, -5)  # ----
# r = range(1, 10, 2)  # 1 3 5 7 9
# r = range(100, 0, -20)  # 100 80 60 40 20

# r = range(100, 0, -20)
# for i in r:
#    print(i)


# a = 'qwerty'

# for i in a:
#    print(i)


# line = ""
# for i in range(5):
#    line = ""
#    for j in range(5):
#        line += "*"
#    print(line)

# text = 'Поешь говна'
# print(len(text))
# print('говна' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('говна', 'ГОВНА'))


# text = 'cъещь ещё этих мягких французких булок'
# print(text[0])										# у
# print(text[1])										# с
# print(text[len(text)-1])						# ъ
# print(text[-5])									# к
# print(text[:])										# Съещь еще этих мягких французких булок
# print(text[:2])									# съ
# print(text[len(text)-2:])						# ок
# print(text[2:9])									# ешь еще
# print(text[6:-17])								# еще этих мягких
# print(text[0:len(text):6])						# сеикаио
# print(text[::6])									# сеикаио
# text = text[2:9] + text[-5] + text[:2]		# ...

#import os
#clear = lambda: os.system('cls') #ОЧИСТКА КОНСОЛИ
#clear()

name = 'string\tstring2' #вывод через двойной пробел
name2 = 'string\nstring2' #вывод через перенос строки
name3= "\"string\"" #вывод кавычек
name_input = int(input())

print(name)
print(name2)
print(name3)
print(name_input)
print(type(name_input))

