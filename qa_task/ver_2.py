import time

file_size = None    # размер файла
net_speed = None    # скорость интернет-соединения
perсent = 0    # для расчета
perсentOutput = 0   # для вывода на экран
message = "Вы ввели неверное значение. Используйте целые положительные значения."

while True:
    try:
        file_size = int(input("Введите размер файла в Мб: "))
        if file_size > 0:
            break
        else:
            print(message)
    except ValueError:
        print(message)

while True:
    try:
        net_speed = int(input("Введите скорость вашего соединения в Мб/с: "))
        if net_speed > 0:
            break
        else:
            print(message)
    except ValueError:
        print(message)

downl_time_sec = int(file_size / net_speed)  # Время скачивания в секундах
download_time = time.gmtime(downl_time_sec)
consent_downl = None

if download_time.tm_hour > 1:
    print("Скачивание займет", download_time.tm_hour, "часов.")
    print("Вы уверены, что хотите продолжить?")
    print("Введите \"да\" или \"нет\"")
    while True:
        consent_downl = input().lower()
        if consent_downl == "да" or consent_downl == "нет":
            break
        else:
            print("Неверный ввод, необходим ответ \"да\" или \"нет\"")

if consent_downl == "да" or consent_downl == None:
    print("Загрузка обновления началась.")
    #start_time = time.time()
    for i in range(1, downl_time_sec + 1):

        perсent = int(net_speed * i / file_size * 100)  # вычисляем текущий процент загрузки

        if perсentOutput != perсent:    # Если предыдущее значение не равно текущему
            perсentOutput = perсent    # Передаем новое значение в переменную для вывода
            print("Прошло", i, "секунд. Скачано", net_speed * i, "из", file_size, "Мб", "(" + str(perсentOutput) + "%)")
        else:    # в противном случае выводим символы, которые показывают, что процесс не стоит на месте
            print(i, "sec")

        time.sleep(0.99)  # "синхронизация" времени с реальным

    if file_size % net_speed != 0:
        print("Прошло", i + 1, "секунд. Скачано", file_size, "из", file_size, "Мб (100%)")
    #end_time =time.time()
    print("Загрузка обновления завершена.")

elif consent_downl == "нет":
    print("Загрузка отменена пользователем")


#execution_time = end_time - start_time
#print(f"Время выполнения: {execution_time} секунд")    # Посмотреть реальное время выполнения цикла
