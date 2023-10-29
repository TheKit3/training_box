import time

file_size = None  # размер файла
net_speed = None  # скорость интернет-соединения
perсent = 0  # для расчета
percentage_output = 0  # для вывода на экран
error_message = "Вы ввели неверное значение. Используйте целые положительные значения."

while True:
    try:
        file_size = int(input("Введите размер файла в Мб: "))
        if file_size > 0:
            break
        else:
            print(error_message)
    except ValueError:
        print(error_message)

while True:
    try:
        net_speed = int(input("Введите скорость вашего соединения в Мб/с: "))
        if net_speed > 0:
            break
        else:
            print(error_message)
    except ValueError:
        print(error_message)

download_time_sec = int(file_size / net_speed)  # Время скачивания в секундах
download_time = time.gmtime(download_time_sec)
download_confirm = None

if download_time.tm_hour > 1:
    print("Скачивание займет", download_time.tm_hour, "часов.")
    print("Вы уверены, что хотите продолжить?")
    print('Введите "да" или "нет"')
    while True:
        download_confirm = input().lower()
        if download_confirm == "да" or download_confirm == "нет":
            break
        else:
            print('Неверный ввод, необходим ответ "да" или "нет"')

if download_confirm == "да" or download_confirm == None:
    print("Загрузка обновления началась.")
    # start_time = time.time()
    for i in range(1, download_time_sec + 1):
        perсent = int(
            net_speed * i / file_size * 100
        )  # вычисляем текущий процент загрузки

        if percentage_output != perсent:  # Если предыдущее значение не равно текущему
            percentage_output = perсent  # Передаем новое значение в переменную для вывода
            print(
                "Прошло",
                i,
                "секунд. Скачано",
                net_speed * i,
                "из",
                file_size,
                "Мб",
                "(" + str(percentage_output) + "%)",
            )
        else:  # если проценты повторяются - выводим символы
            print(i, "sec")

        time.sleep(0.99)  # "синхронизация" времени с реальным

    if file_size % net_speed != 0:
        print(
            "Прошло", i + 1, "секунд. Скачано", file_size, "из", file_size, "Мб (100%)"
        )
    # end_time =time.time()
    print("Загрузка обновления завершена.")

elif download_confirm == "нет":
    print("Загрузка отменена пользователем")


# execution_time = end_time - start_time
# print(f"Время выполнения: {execution_time} секунд")    # Посмотреть реальное время выполнения цикла
input()    # чтобы не закрывалась консоль
