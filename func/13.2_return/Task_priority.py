# Задача "Приоритет задач"
# Условие: Даны два числа; Сравнивается кол-во цифр
# Выходные данные: Сообщение о том, где больше цифр(либо равно)

def numeral_count(number):
    # if number < 0:
    #     print("Число отрицательное - обнуляю.")
    count = 0
    while number > 0:
        number //= 10
        count += 1

    return count

firstTask = int(input("Введите первое число: "))
secondTask = int(input("Введите второе число: "))

firstNumeral = numeral_count(firstTask)
secondNumeral = numeral_count(secondTask)

if firstNumeral > secondNumeral:
    print("Цифр больше в первом числе.")
elif secondNumeral > firstNumeral:
    print("Цифр больше во втором числе.")
else:
    print("Числа равны")
