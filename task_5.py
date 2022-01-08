"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(self.real + other.real, self.indeterminate + other.indeterminate)

    def __mul__(self, other: 'ComplexNumber'):
        a = self.real
        b = self.indeterminate
        c = other.real
        d = other.indeterminate

        return ComplexNumber(a * c - b * d, a * d + b * c)

    def __str__(self):
        return f"({self.real}{'+' if self.indeterminate > 0 else ''}{self.indeterminate}i)"


a = ComplexNumber(7, 33)
b = ComplexNumber(77, 8)
print(a + b)
print(a * b)
