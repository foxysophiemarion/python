# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого 
# множества. m - кол-во
# элементов второго множества. Затем пользователь
# вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = int(input('Введите кол-во элементов 1-го множества -> '))
m = int(input('Введите кол-во элементов 2-го множества -> '))
while True:
   arr_first = input('Введите элементы 1 списка через пробел -> ').split()
   if len(arr_first) == n:
         break
while True:
       arr_second = input('Введите элементы 2 списка через пробел -> ').split()
       if len(arr_second) == m:
               break
print([arr_first[i] for i in range(0, len(arr_first)) for j in range(0, len(arr_second)) if arr_first[i]==arr_second[j]])