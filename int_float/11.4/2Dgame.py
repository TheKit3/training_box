import math

distance = int(input("Эвведите пройденное расстоянние: "))
angle = int(input("Введите угол поворота: "))

angle /= 57.2958

x = math.cos(angle) * distance
y = math.sin(angle) * distance


print("Персонаж находится в координатах:", x, y)
