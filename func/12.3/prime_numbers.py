def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


numbersInSequence = int(input("Введите количество чисел в последовательности: "))

for n in range(numbersInSequence):
    number = int(input("Введите число: "))
    if isPrime(number):
        print(number, "- простое число")
    else:
        print(number, "- не является простым числом")
