
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    number = number*(10**ndigits)
    dif = float(number) - int(number)
    if dif > 0.5:
        number = number + dif
    number = number // 1
    number = number/(10**ndigits)
    return number
      
    
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    part1 = ticket_number[0:3]
    sum1 = 0
    for number in part1:
        sum1 += int(number)
    part2 = ticket_number[3:6]
    sum2 = 0
    for number in part2:
        sum2 += int(number)
    if sum1 == sum2:
        return "Ваш билет счастливый!"
    else:
        return "Повезет в следующий раз!"
    

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
           

# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1 2 3 5 8 13 21 34 55 89 144

def fibonacci(n, m):
    lst = [1, 1]
    a = 1
    c = 1
    while a < m and c < m:
        c = c + a 
        a = a + c
        lst.append(c)
        lst.append(a)
    print(lst[n:m])
    
fibonacci(1, 16)



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    a = len(origin_list)
    for x in range(a):
        for i in origin_list:
            if i > origin_list[-1]:
                origin_list.append(i)
                origin_list.remove(i)
    print(origin_list)
     
            
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_func(x):
    if x > 0:
        return 1
    else:
        return 0
    
def my_filter(func, a):
    b = []
    for i in a:
        if func(i) == True:
            b.append(i)
    print(b)

a = [-2, 15, -98, -1, 0, 14]
my_filter(my_func, a)
            
    
    


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
  


# HARD

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


import os

path_ved = os.path.join('files', 'workers.txt')
path_fact = os.path.join('files', 'hours_of.txt')

workers = []
with open(path_ved, 'r', encoding='UTF-8') as ved:
    ved = ved.readlines()
    for i in range(1, len(ved)):
        a = ved[i].strip('\n')
        a = a.split(' ')
        a.remove(a[0])
        for j in a[:]:
            if j == "":
                a.remove(j)
        a.remove(a[2])
        workers.append(a)
       

workers_fact = []
with open(path_fact, 'r', encoding='UTF-8') as fact:
    fact = fact.readlines()
    for i in range(1, len(fact)):
        b = fact[i].strip('\n')
        b = b.split(' ')
        b.remove(b[0])
        for j in b[:]:
            if j == "":
                b.remove(j)
        workers1.append(b)

workers.sort()
workers_fact.sort()

workers_total = []
for i in range(len(workers)):
    x = workers[i] + workers_fact[i]
    workers_total.append(x)


zp_pererabotka = 0
zp_nedorab = 0
for j in workers_total:
    zp_hour = float(int(j[1]) / int(j[2]))
    
    if int(j[4]) >= int(j[2]):
        extra_hours = float(int(j[4]) - int(j[2]))
        zp = round(float(zp_hour * int(j[4]) + zp_hour * extra_hours), 2)
        TEKST = "Зарплата сотрудника {} равна: {} руб.".format(j[0], zp)
        zp_pererabotka += zp
    else:
        zp = round(float(zp_hour * int(j[4])), 2)
        TEKST = "Зарплата сотрудника {} равна: {} руб.".format(j[0], zp)
        zp_nedorab += zp
    print(TEKST)
        
       
print("Заработная плата всех сотрудников равна ", zp_pererabotka+zp_nedorab)


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))    
