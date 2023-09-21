import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Ошибка: извлечение корня из отрицательного числа"

def percentage(x, y):
    return (x * y) / 100

def factorial(x):
    if x < 0:
        return "Ошибка: факториал определен только для неотрицательных чисел"
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

print("Сумма:", add(number1, number2))
print("Разность:", subtract(number1, number2))
print("Произведение:", multiply(number1, number2))
print("Частное:", divide(number1, number2))
print("Возведение в степень:", power(number1, number2))
print("Квадратный корень первого числа:", square_root(number1))
print("Процент от первого числа:", percentage(number1, number2))
print("Факториал первого числа:", factorial(int(number1)))
print("Синус: " , sin(number1))
print("Косинус: " , cos(number1))
print("Тангенс: " , tan(number1))
