file_size = int(input("Введите размер файла в Мб: "))
net_speed = int(input("Введите скорость вашего соединения в Мб/с: "))

time = int(file_size / net_speed)    # Время скачивания в секундах
perсent = 0

print(time)

for i in range(1, time+1):
    perсent = int(net_speed * i / file_size * 100)
    print("Прошло", i, "секунд. Скачано", net_speed * i, "из", file_size, "Мб", "(" + str(perсent) + "%)")

if file_size % net_speed != 0:
    print("Прошло", i + 1, "секунд. Скачано", file_size, "из", file_size, "Мб (100%)")
