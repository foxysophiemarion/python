import os
import os.path
import re
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

filepath = os.path.join("C:/Users/Palindrom.FSM/Desktop/GEEK BRAINS/Python seminar/HW_8_phonebook",'Users_data.txt') # Путь к списку контактов

def checking_for_input_length(arr):
    if len(arr) > 4:
        arr = arr[:4]
    if len(arr) < 4:
        a = len(arr)
        while a < 4:
            arr.append('None')
            a += 1
    return arr

# Выбор функций
def choose():
    while True:
        choise = input('Введите действие:  ').lower()
        if choise == '1': return zapis(checking_for_input_length(input('Введите Фамилию Имя Отчество и Номер телефона человека через пробел:  ').split()))
        if choise == '2': return read_search(input('Введите Фамилию контакта, которого вы ищите: '))
        if choise == '3': return delete(input('Введите Фамилию для удаления контакта: '))
        if choise == '4': return change(input('Введите Фамилию для изменения контакта: '), input('Введите, что вы хотите изменить (1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Номер): ') , input('Введите новые данные: '))
        if choise == '5': return read_all() 
        if choise == '6': exit()

# Открытие и запись в список контактов информации (если файл уже есть, то добавляем данные)
def zapis(arr):
    dict = {0: 'Фамилия:', 1: 'Имя:', 2: 'Отчество:', 3: 'Номер:'}
    counter = 0
    if os.path.exists(filepath):
        with open(filepath,'a',encoding = 'utf-8') as f:
            f.writelines('-'*5 + 'Контакт' + '-'*5 + '\n')
            for i in arr:
                f.writelines(dict[counter] + ' ' + i + '\n')
                counter += 1
            f.write('\n')
            return print(f'Данные контакта были успешно добавлены!')         
    else:
        with open(filepath,'w+',encoding = 'utf-8') as f:
            f.writelines('-'*5 + 'Контакт' + '-'*5 + '\n')
            for i in arr:
                f.writelines(dict[counter] + ' ' + i)
                f.write('\n')
                counter += 1
            f.write('\n')
            return print(f'Данные контакта были успешно добавлены!')
            
# Поиск данных контакта и их печать
def read_search(teg):
    if os.path.exists(filepath):
        with open(filepath,'r',encoding = 'utf-8') as f:
            new_array = [re.sub('\s+','',line) for line in f.readlines()]
            for i in range(0,len(new_array)):
                if teg in new_array[i]:
                    return print(f'По ващему запросу {teg} удалось найти: \n {new_array[i]} \n {new_array[i+1]} \n {new_array[i+2]} \n {new_array[i+3]}')
            return print(f'По вашему запросу "{teg}" ничего не найдено')
    else: print('Файла не существует!')

# Чтение всех контактов
def read_all():
    with open(filepath,'r',encoding = 'utf-8') as f:
        for line in f:
            print(line)

# Удаление данных контакта из файла
def delete(teg):
    check = False
    with open(filepath,'r',encoding = 'utf-8') as f:
        arr = [line for line in f.readlines()]
        for i in range(len(arr)):
            if teg in arr[i]:
                check = True
                arr[i-1], arr[i], arr[i+1], arr[i+2], arr[i+3], arr[i+4] = '', '', '', '', '', ''
    if check == True:
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные контакта "{teg}" были успешно удалены!')
    return print(f'По вашему запросу "{teg}" ничего не найдено!')

# Изменение данных в файле
def change(teg, diction, new_teg):
    check = False
    dict = {'1': 'Фамилия:', '2': 'Имя:', '3': 'Отчество:', '4': 'Номер:'}
    if diction not in dict.keys():
        return print(f'Ваше значение "{diction}" не подходит условию!')
    with open(filepath,'r',encoding = 'utf-8') as f:
        arr = [line for line in f.readlines()]
        for i in range(len(arr)):
            if teg in arr[i]:
                check = True
                if diction == '1': arr[i] = dict[diction] + ' ' + new_teg + '\n'
                if diction == '2': arr[i+1] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '3': arr[i+2] = dict[diction] + ' '  + new_teg + '\n'
                if diction == '4': arr[i+3] = dict[diction] + ' '  + new_teg + '\n'    
    if check == True:               
        with open(filepath,'w',encoding = 'utf-8') as f:
            f.writelines(arr)
            return print(f'Данные контакта "{teg}" были успешно изменены!')
    else: return print(f'По вашему запросу "{teg}" ничего не найдено!')


while True:
    clear()
    print('Выберите действие: \n 1 - Добавить контакт \n 2 - Найти контакт по Фамилии \n 3 - Удалить контакт  \n 4 - Изменить контакт \n 5 - Вывод списка контактов \n 6 - Выйти из программы')
    choose()
    input('Нажимите "ENTER", чтобы продолжить.')