def rectangle_area(width, height):
    return width * height

def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False

def sum_digits(number):

    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

width = int(input("Введи ширину прямоугольника: "))
height = int(input("Введи высоту прямоугольника: "))
area = rectangle_area(width, height)
print("Площадь прямоугольника:", area)

number = int(input("Введи число: "))
if is_even(number):
    print("Число четное")
else:
    print("Число нечетное")

number = int(input("Введи положительное целое число: "))
digit_sum = sum_digits(number)
print("Сумма цифр в числе:", digit_sum)
