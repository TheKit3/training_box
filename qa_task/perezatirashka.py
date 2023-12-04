import time

file_size = 800000
net_speed = 10

download_time_sec = int(file_size / net_speed)  # Время скачивания в секундах
print(download_time_sec)
download_time = time.gmtime(download_time_sec)


print(download_time.tm_hour)
print(download_time.tm_min)
print(download_time.tm_sec)
