'''
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал 'зачеркнуть':
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал 'продолжить':
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
'''

import random


barrels = random.sample(range(1, 91), 90)
barrels_count = 90
card1 = random.sample(range(1, 91), 15)
card1_count = 15
card2 = random.sample(range(1, 91), 15)
card2_count = 15

card1_field = [card1[:5], card1[5:10], card1[10:]]
card2_field = [card2[:5], card2[5:10], card2[10:]]

for line1 in card1_field:
    line1.sort()
    line1.insert(random.randint(0, 6), ' ')
    line1.insert(random.randint(0, 7), ' ')
    line1.insert(random.randint(0, 8), ' ')
    line1.insert(random.randint(0, 9), ' ')

for line2 in card2_field:
    line2.sort()
    line2.insert(random.randint(0, 6), ' ')
    line2.insert(random.randint(0, 7), ' ')
    line2.insert(random.randint(0, 8), ' ')
    line2.insert(random.randint(0, 9), ' ')


def field():
    print('{:-^26}'.format(' Ваша карточка '))
    for line1 in card1_field:
        for n1 in line1:
            print('{0:>2}'.format(n1), end=' ')
        print()
    print('{:-^26}\n'.format('-'))
    print('{:-^26}'.format(' Карточка компьютера '))
    for line2 in card2_field:
        for n2 in line2:
            print('{0:>2}'.format(n2), end=' ')
        print()
    print('{:-^26}\n'.format('-'))

for i in barrels:
    print('-' * 50)
    print()
    print('Новый бочонок: {}, осталось {} '.format(i, barrels_count))
    print()
    field()
    do = input('Чтобы зачеркнуть цифру - нажмите Y,\nпропустить - любую клавишу ')
    if do == 'y' or do == 'Y':
        if i in card2:
            for l in card2_field:
                try:
                    l.insert(l.index(i), '-')
                    l.pop(l.index(i))
                    card2_count -= 1
                except ValueError:
                    continue
        if i in card1:
            for m in card1_field:
                try:
                    m.insert(m.index(i), '-')
                    m.pop(m.index(i))
                    card1_count -= 1
                except ValueError: # я так и не поняла, почему возникает эта ошибка??
                    continue
        else:
            print('Вы проиграли')
            break
    else:
        if i in card2:
            for l in card2_field:
                try:
                    l.insert(l.index(i), '-')
                    l.pop(l.index(i))
                    card2_count -= 1
                except ValueError:
                    continue
        if i in card1:
            print('Вы проиграли')
            break

    if card1_count == 0:
        print ('Вы выиграли')
        break
    if card2_count == 0:
        print ('Вы проиграли')
        break
    barrels_count -= 1


# Чем генератор бочонков был бы лучше такого цикла? 
