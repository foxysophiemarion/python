#За день машина проезжает n километров. Сколько 
#дней нужно, чтобы проехать маршрут длиной m 
#километров? При решении этой задачи нельзя 
#пользоваться условной инструкцией if и циклами.

n=int(input('Введите количество километров, которые машина проезжает за день: '))
m=int(input('Введите длину марщрута в километрах: '))
print((f'(Для прохождения маршрута длинной', m, 'километров потребуется',m//n, 'дней'))