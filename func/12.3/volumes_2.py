import math


def sphereArea(R):
    print(4 * math.pi * (R**2))


def sphereVolume(R):
    print(4 / 3 * math.pi * (R**3))


R = int(input("Введите радиус планеты: "))
sphereArea(R)
sphereVolume(R)
