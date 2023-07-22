#В некоторой школе решили набрать три новых 
#математических класса и оборудовать кабинеты для 
#них новыми партами. За каждой партой может сидеть 
#два учащихся. Известно количество учащихся в 
#каждом из трех классов. Выведите наименьшее 
#число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32


#class1=int(input("Введите кол-во учеников 1го класса: "))
#class2=int(input("Введите кол-во учеников 2го класса: "))
#class3=int(input("Введите кол-во учеников 3го класса: "))

#tables = (class1+1)//2 +(class2+1)//2 +(class3+1)//2
## tables = (round((class1+1+class2+1+class3+1)//2))
#print("Количество необходимых парт:",tables)

firstCountStudy=int(input("Введите кол-во учеников 1го класса: "))
secondCountStudy=int(input("Введите кол-во учеников 2го класса: "))
thirdCountStudy=int(input("Введите кол-во учеников 3го класса: "))

firstCountDesk= firstCountStudy//2+firstCountStudy%2
secondCountDesk= secondCountStudy//2+secondCountStudy%2
thirdCountDesk= thirdCountStudy//2+thirdCountStudy%2

print(firstCountDesk+secondCountDesk+thirdCountDesk)