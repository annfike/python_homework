
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создание копии файла')
    print('rm <file_name> - удаление файла')
    print('cd <full_path or relative_path> - изменение текущей директории')
    print('ls - отображение полного пути текущей директории')


def make_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print('pong')

def create_copy():
    file_name = input('Введите имя копируемого файла с расширением: ')
    shutil.copy(file_name, 'copy_'+file_name)
    print('копия файла {} создана'.format(file_name))

def del_file():
    os.remove(os.path.join(os.getcwd(), input('Введите имя удаляемого файла: ')))
    print('Указанный файл удалён')

def go_dir():
    name = input('Введите название папки, в которую хотите перейти: ')
    path = os.path.join(os.getcwd(), name)
    try:
        os.chdir(path)
        print('Вы успешно перешли в папку {}'.format(name))
    except FileExistsError:
        print('Такой директории нет')

def current_dir():
    print(os.path.abspath(os.curdir))

do = {
    'help': print_help,
    'mkdir': make_dir,
    'ping': ping,
    'cp': create_copy,
    'rm': del_file,
    'cd': go_dir,
    'ls': current_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')

































