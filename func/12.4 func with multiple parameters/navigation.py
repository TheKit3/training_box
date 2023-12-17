import math


def myDistance(x, y):
    disctance = math.sqrt(x**2 + y**2)
    print(disctance)


def betweenDistance(x_1, y_1, x_2, y_2):
    disctance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(disctance)


choice = int(
    input("1 - расстояние от вас до точки; 2 - расстояние между двумя точками: ")
)

if choice == 1:
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    myDistance(x, y)
elif choice == 2:
    x_1 = float(input("Введите координату x: "))
    y_1 = float(input("Введите координату y: "))
    x_2 = float(input("Введите координату x: "))
    y_2 = float(input("Введите координату y: "))
    betweenDistance(x_1, y_1, x_2, y_2)
else:
    print("Ошибка ввода!")
