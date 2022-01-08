"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_str: str):
        date_list = Date.date_extractor(date_str)
        self.date_validate(date_list)
        self.day, self.month, self.year = date_list

    @classmethod
    def date_extractor(cls, date_str: str):
        return [int(el) for el in date_str.split('-')]

    @staticmethod
    def date_validate(date_list: list):
        day, month, year = date_list
        assert 1950 <= year <= 2077, 'Неверные данные года, 1950 - 2077'
        assert 1 <= month <= 12, 'Неверные данные месяца, 1 - 12'
        if month == 2:
            if year % 4 == 0:
                assert 1 <= day <= 29, 'Неверные данные числа, февраль високосный год, 1 - 29'
            else:
                assert 1 <= day <= 28, 'Неверные данные числа, февраль невисокосный год, 1 - 28'
        elif month == 4 or month == 6 or month == 9 or month == 11:
            assert 1 <= day <= 30, 'Неверные данные числа, 1 - 30'
        else:
            assert 1 <= day <= 31, 'Неверные данные числа, 1 - 31'

    def __str__(self):
        return f'{self.day:02}.{self.month:02}.{self.year}'


date = Date('17-01-2022')
print(date)
# date_001 = Date('29-02-2022')
# date_002 = Date('31-04-2022')
# date_003 = Date('32-01-2021')
# date_004 = Date('15-13-2021')
# date_005 = Date('17-01-1949')
# date_006 = Date('14-01-2078')
