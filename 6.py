
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        # стороны: s = ((x2 - x1)^2+(y2-y1)^2)^(1/2) 
        self.a = math.sqrt(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))
        self.b = math.sqrt(((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2))
        self.c = math.sqrt(((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2))

    def area(self):
        p = 0.5*(self.a + self.b + self.c) #полупериметр
        S = math.sqrt((p*(p - self.a)*(p - self.b)*(p - self.c)))
        print('Площадь треугольника равна: ', round(S, 2))

    def perim(self):
        pr = self.a + self.b + self.c
        print('Периметр треугольника равен: ', round(pr, 2))

    def heigth(self):
        p = 0.5*(self.a + self.b + self.c)
        S = math.sqrt((p*(p - self.a)*(p - self.b)*(p - self.c)))
        HA = S*2/self.a
        HB = S*2/self.b
        HC = S*2/self.c
        print('Высота к стороне 'a' равна: ', round(HA, 2))
        print('Высота к стороне 'b' равна: ', round(HB, 2))
        print('Высота к стороне 'c' равна: ', round(HC, 2))
        

triangle1 = Triangle(1, 1, -2, 4, -2, -2)
triangle1.area()
triangle1.perim()
triangle1.heigth()              


# Задача-2: Написать Класс 'Равнобочная трапеция', заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы+
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате 'Фамилия И.О.')+
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)+
# 4. Узнать ФИО родителей указанного ученика+
# 5. Получить список всех Учителей, преподающих в указанном классе+


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_short_name(self):
        return  self.surname + ' ' + self.name[0] + '.'


class Student(Person):
    def __init__(self, name, surname, schoolclass, mother, father):
        Person.__init__(self, name, surname)
        self.schoolclass = schoolclass
        self.mother = mother
        self.father = father

    def get_parents(self, student):
        a = input('Введите имя, фамилию ученика ')
        for Student in students:
            if ((Student.name + ' ' + Student.surname) == a.title()) or ((Student.surname + ' ' + Student.name) == a.title()):
                print('Родители ученика {}: '.format(a.title()),Student.mother + ', ' + Student.father)
                return
        print('Ученик не найден')
            
    def list_of_schoolclasses(self, students):
        list_of_schoolclasses = []
        for Student in students:
            if Student.schoolclass not in list_of_schoolclasses:
                list_of_schoolclasses.append(Student.schoolclass)
        print('Список всех классов школы: ', list_of_schoolclasses)

    def list_of_students(self, students):
        list_of_schoolclasses = []
        for Student in students:
            if Student.schoolclass not in list_of_schoolclasses:
                list_of_schoolclasses.append(Student.schoolclass)
        print('Список всех классов школы: ', list_of_schoolclasses)
        a = input('Введите класс, который вас интересует ')
        for i in list_of_schoolclasses:
            list_of_students = []
            if i == a.upper():
                for Student in students:
                    if i == Student.schoolclass:
                        list_of_students.append(Student.get_short_name())
                        b = Student.schoolclass
                print('Список учеников класса {}: {}'.format(b, list_of_students))
                return
        print('Такого класса не существует')


class Teacher(Person):
    def __init__(self, name, surname, item, teach_classes):
        Person.__init__(self, name, surname)
        self.item = item
        self.teach_classes = list(teach_classes)

    def list_of_items(self):
        a = input('Введите имя, фамилию ученика ')
        for Student in students:
            list_of_items = []
            if ((Student.name + ' ' + Student.surname) == a.title()) or ((Student.surname + ' ' + Student.name) == a.title()):
                b = Student.schoolclass
                for Teacher in teachers:
                    if b in Teacher.teach_classes:
                        list_of_items.append(Teacher.item)
                print('Список всех предметов ученика {} из класса {}: '.format(a.title(), b), list_of_items)
                return
        print('Ученик не найден')

    def list_of_teachers(self):
        list_of_schoolclasses = []
        for Student in students:
            if Student.schoolclass not in list_of_schoolclasses:
                list_of_schoolclasses.append(Student.schoolclass)
        print('Список всех классов школы: ', list_of_schoolclasses)
        a = input('Введите класс, который вас интересует ')
        for i in list_of_schoolclasses:
            list_of_teachers = []
            if i == a.upper():
                for Teacher in teachers:
                    if a.upper() in Teacher.teach_classes:
                        list_of_teachers.append(Teacher.name+' '+Teacher.surname)
                print('Список учителей класса {}: {}'.format(a, list_of_teachers))
                return
        print('Такого класса не существует')

        

students = [Student('Иван', 'Пчелинцев', '9Б', 'Делалой Анна', 'Пчелинцев Алексей'),
            Student('Николай', 'Пчелинцев', '5В', 'Делалой Анна', 'Пчелинцев Алексей'),
            Student('Богдан', 'Кулаков', '5В', 'Кулакова Ольга', 'Кулаков Евгений'),
            Student('Дарья', 'Дроздова', '3А', 'Давыдова Анастасия', 'Дроздов Денис'),
            Student('Дарья', 'Иванова', '8В', 'Иванова Оксана', 'Иванов Михаил'),
            ]

teachers = [Teacher('Иван', 'Иванов', 'Математика', ['9Б', '5В', '8В']),
            Teacher('Петр', 'Петров', 'Литература', ['9Б', '8В']),
            Teacher('Сидр', 'Сидоров', 'Физра', ['9Б', '5В', '3А', '8В']),
            Teacher('Влад', 'Путин', 'История', ['9Б']),
            Teacher('Николай', 'Дроздов', 'Окружающий мир', ['5В', '3А']),
            ]

print('Полный список всех учеников:')
for num, Student in enumerate(students, start=1):
   print(num, Student.get_full_name(), Student.schoolclass)

# полный список всех классов школы
Student.list_of_schoolclasses(students)

# список всех учеников в указанном классе
Student.list_of_students(students)

# Получить список всех предметов указанного ученика Ученик --> Класс --> Учителя --> Предметы)
Teacher.list_of_items(teachers)

#Узнать ФИО родителей указанного ученика
Student.get_parents(students)

#список всех Учителей, преподающих в указанном классе
Teacher.list_of_teachers(teachers)


