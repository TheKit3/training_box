import time

file_size_MB = None  # размер файла в МБ
net_speed = None  # скорость интернет-соединения
perсent = 0  # для расчета
percentage_output = 0  # для вывода на экран
error_message = (
    "Вы ввели неверное значение! \nИспользуйте целые положительные значения."
)
max_length_size = 6  # максимальный размер файла  (100 Гб)
max_length_speed = 4  # максимальная скорость 9,999 Гбит/с

while True:
    try:
        print()
        file_size_MB = int(input("Введите размер файла в МБ и нажмите Enter: "))
        if file_size_MB > 0 and len(str(file_size_MB)) <= max_length_size:
            break
        else:
            print()
            print(
                "Ошибка! \nМинимальный размер файла 1 МБ; \nМаксимальный размер файла 999999 МБ (100 ГБ)"
            )
    except ValueError:
        print()
        print(error_message)

while True:
    try:
        print()
        net_speed = int(
            input("Введите скорость вашего соединения в Мбит/с и нажмите Enter: ")
        )
        if net_speed > 0 and len(str(net_speed)) <= max_length_speed:
            break
        else:
            print()
            print(
                "Ошибка! \nМинимальная скорость 1 Мбит/с; \nМаксимальная скорость 9999 Мбит/с"
            )
    except ValueError:
        print()
        print(error_message)

file_size_Mbit = file_size_MB * 8  # переводим МБ в Мбиты

if file_size_Mbit < net_speed:
    print()
    print("Быстрее быстрого! \nФайл загружен менее чем за секунду.")
else:
    download_time_sec = int(file_size_Mbit / net_speed)  # Время скачивания в секундах
    download_time = time.gmtime(download_time_sec)
    download_confirm = None

    if download_time.tm_hour > 1:
        print()
        print("Скачивание займет", download_time.tm_hour, "часов.")
        print("Вы уверены, что хотите продолжить?")
        print('Введите "да" или "нет"')
        while True:
            download_confirm = input().lower()
            if download_confirm == "да" or download_confirm == "нет":
                break
            else:
                print()
                print('Неверный ввод, необходим ответ "да" или "нет"')

    if download_confirm == "да" or download_confirm == None:
        print()
        print("Началась загрузка обновления...")
        print()
        # start_time = time.time()
        for i in range(1, download_time_sec + 1):
            perсent = int(
                net_speed * i / file_size_Mbit * 100
            )  # вычисляем текущий процент загрузки

            if (
                percentage_output != perсent
            ):  # Если предыдущее значение не равно текущему
                percentage_output = (
                    perсent  # Передаем новое значение в переменную для вывода
                )
                print(
                    "Прошло секунд:",
                    i,
                    " - Скачано",
                    (net_speed * i) / 8,
                    "из",
                    file_size_MB,
                    "Мб",
                    "(" + str(percentage_output) + "%)",
                    end="\r",
                )
            else:  # если проценты повторяются - выводим символы
                print(i, "...", end="\r")

            time.sleep(0.99)  # "синхронизация" времени с реальным

        if file_size_Mbit % net_speed != 0:
            print(
                "Прошло",
                i + 1,
                "секунд. Скачано",
                file_size_MB,
                "из",
                file_size_MB,
                "Мб (100%)",
            )
        # end_time =time.time()
        print()
        print("Загрузка обновления завершена.")

    elif download_confirm == "нет":
        print()
        print("Загрузка отменена пользователем")

    # execution_time = end_time - start_time
    # print(f"Время выполнения: {execution_time} секунд")    # Посмотреть реальное время выполнения цикла
input()  # чтобы не закрывалась консоль
