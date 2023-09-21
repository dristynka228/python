import math

print("Калькулятор")

while True:
    print("Выбери операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Синус")
    print("6. Косинус")
    print("7. Тангенс")
    print("8. Квадратный корень")
    print("9. Факториал")
    print("10.Возведение в степень")
    print("0. Выход")

    choice = input("Введи номер того, что хочешь сделать (0-10): ")

    if choice == '0':
        print("Пока-пока")
        break

    elif choice in ['1', '2', '3', '4']:
        num1 = float(input("Введи первое число: "))
        num2 = float(input("Введи второе число: "))

        if choice == '1':
            result = num1 + num2
            print("Результат: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Результат: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Результат: ", result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("Результат: ", result)
            else:
                print("Ошибка, нельзя делить на ноль")

    elif choice in ['5', '6', '7']:
        angle = float(input("Введи значение угла: "))
        radian = math.radians(angle)

        if choice == '5':
            result = math.sin(radian)
            print("Результат: ", result)
        elif choice == '6':
            result = math.cos(radian)
            print("Результат: ", result)
        elif choice == '7':
            result = math.tan(radian)
            print("Результат: ", result)

    elif choice == '8':
        number = float(input("Введи число для извлечения квадратного корня: "))
        result = math.sqrt(number)
        print("Результат: ", result)

    elif choice == '9':
            number = int(input("Введи число для нахождения факториала: "))
            if number >= 0:
                result = math.factorial(number)
                print("Результат факториала:", result)
            else:
                print("Факториал есть только для положительных чисел")

    elif choice == '10':
        num1 = float(input("Введи число, которое хочешь возвести в степень: "))
        num2 = float(input("Введи степень: "))
        result = num1 ** num2
        print("Результат степени: ", result)
    else:
        print("Сказано, от 0 до 10 и никакой другой символ")