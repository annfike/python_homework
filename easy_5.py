
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

'''
do = input('Чтобы создать директории dir_1 - dir_9, нажмите 1 ')
if do == '1':
    for i in range(1, 10):
        name = 'dir_' + str(i)
        try:
            os.mkdir(os.path.join(os.getcwd(), name))
        except FileExistsError:
            print('Такая директория уже существует')

do1 = input('Чтобы удалить директории dir_1 - dir_9, нажмите 2 ')
if do1 == '2':            
    for i in range(1, 10):
        name = 'dir_' + str(i)
        try:
            os.rmdir(os.path.join(os.getcwd(), name))
        except FileExistsError:
            print('Такой директории нет')
'''

def create_dir():
    name = input('Введите имя создаваемой директории ')
    try:
        os.mkdir(os.path.join(os.getcwd(), name))
        print('Вы успешно создали папку {}'.format(name))
    except FileExistsError:
        print('Такая директория уже существует')

def del_dir():
    name = input('Введите имя директории, которую вы хотите удалить ')
    try:
        if os.listdir(name) == []:
            os.rmdir(os.path.join(os.getcwd(), name))
            print('Вы успешно удалили папку {}'.format(name))
        else:
            print('Папка содержит файлы {} , вы действительно хотите ее удалить?'.format(os.listdir(name)))
            do = input('Если да, нажмите 1 ')
            if do == '1':
                shutil.rmtree(os.path.join(os.getcwd(), name))
                print('Вы успешно удалили папку {}'.format(name))
            
    except FileExistsError:
        print('Такой директории нет')


 
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# так отображает папки+файлы
def show_files():
    for i in os.listdir():
        print(i)

# так отображает только папки
def show_dirs():
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def create_copy():
    shutil.copy(__file__, __file__+'_copy')






































