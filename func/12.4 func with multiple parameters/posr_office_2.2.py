# Почта 2:
# В почтовом извещении нужно указывать 7 аргументов:
# фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.
# Реализуйте функцию, которая получает все эти данные и выводит на экран.
# В программе вызовите функцию три раза с разными значениями аргументов.


def myAdress(surname, name, country, city, street, house_number, flat_number):
    print("Фамилия:", surname)
    print("Имя:", name)
    print("Страна:", country)
    print("Город:", city)
    print("Улица:", street)
    print("Дом:", house_number)
    print("Квартира:", flat_number)
    print()


myAdress("Иванов", "Василий", "Россия", "Москва", "Ленина", "5", "50")
myAdress("Петров", "Геннадий", "Россия", "Владивосток", "Пушкина", "30", "19")
myAdress("Сидоров", "Владимир", "Республика Беларусь", "Бобруйск", "Лесная", "15", "103")
