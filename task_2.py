"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnZeroDivisionError(Exception):
    pass


class OwnValueError(Exception):
    pass


def get_number():
    num = input('Введите делимое число >>> ')
    if num == 'q':
        print('Выход из программы')
        exit()
    if not num.isdigit():
        raise OwnValueError
    return int(num)


def get_divider():
    num = input('Введите делитель или q для выход >>> ')
    if num == 'q':
        print('Выход из программы')
        exit()
    if not num.isdigit():
        raise OwnValueError
    if int(num) == 0:
        raise OwnValueError
    return int(num)


while True:
    try:
        number = get_number()
        divider = get_divider()
        print(f'{number} / {divider} = {number / divider}')
    except OwnValueError:
        print('Неверный формат данных')
        break

    except OwnZeroDivisionError:
        print('Невозможно делить на 0')
        break

