# Задача:
# Условие: Целое положительное число
# Выходные данные: сумма всех чисел числа, сумма чисел суммы

def digitSum(number):
    countSum = 0
    for i in str(number):
        countSum += int(i)
    return countSum

myNumber = int(input("Введите целое положительное число: "))

myDigitSum = digitSum(myNumber)
finalSum = digitSum(myDigitSum)

print("Сумма чисел", myNumber, "=", myDigitSum)
print("Сумма чисел", myDigitSum, "=", finalSum)
