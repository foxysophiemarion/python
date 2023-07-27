#kolvo = 10
#while kolvo < 20:
#    kolvo += 1
#    print(kolvo)
#else:
#    print(100000)
#print("end")




#for i in range(1, 10, 2):
#    print(i)


#list1 = list(range(10, 20))
#print(type(list1))
#for i in range(len(list1)):
#    print(i)



#list1 = list(range(10, 20))
#dlina = len(list1)
#print(dlina)



#str = "privet"
#for i in str:
#    print(i)
#dlina = len(str)
#print(dlina)



#stroka = "privet"
#stroka2 = stroka[0:5:2]
#print(stroka2)
#stroka2 = stroka[::-1]
#print(stroka2)




#Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

#res = 1
#n = int(input('Введите число -> '))
#while n > 0:
#    res *= n
#    n -= 1
#print(res)

#n = 5
#i = 1
#res = 1
#while i<=n:
#    res *= i
#    i+=1
#print(res)







# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

#n = int(input('Введите число -> '))

#if n == 0:
#    print(1)
#else:
#    frst, scnd, count = 0, 1, 2
#    while scnd <= n:
#        if scnd == n:
#            print(count)
#            break
#        frst, scnd = scnd, frst + scnd
#        count += 1
#    else:
#        print(-1)







