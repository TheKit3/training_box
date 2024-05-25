# Задача:
# Условие: Целое положительное число
# Выходные данные: сумма всех чисел числа, сумма чисел суммы

def lineSum(number):
    counterSum = 0
    while number:
        counterSum += number
        number -= 1
    return counterSum

myNumber = int(input("Введите целое положительное число: "))
newNumber = lineSum(myNumber)

print(lineSum(myNumber), lineSum(newNumber))
