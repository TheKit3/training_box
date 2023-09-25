print("Введите местоположение фигуры")
x = float(input("Расположение по горизонтали: "))
y = float(input("Расположеие по вертикали: "))

xSquare = int(x * 10)
ySquare = int(y * 10)

xAdj = (float(xSquare) * 0.1 + 0.05) - x  # мать
yAdj = (float(ySquare) * 0.1 + 0.05) - y  # жива?

print("Фигура находится в клетке:", xSquare, ySquare)
print("Поправьте фигуры на", round(xAdj, 3), round(yAdj, 3))
