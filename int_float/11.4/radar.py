import math

distance = int(input("Введите расстояние до танка: "))
angle = int(input("Введите угол в градусах: "))

angle /= 57.2958

x = math.cos(angle) * distance
y = math.sin(angle) * distance

print("Координаты вражеского танка:", x, y)
