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