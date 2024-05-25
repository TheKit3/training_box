def simpie(number1, number2):
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))

print(simpie(firstNumber, secondNumber))
