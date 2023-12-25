def mainMenu():
    print("1. Сделать что-то хорошее")
    print("2. Cделать что-то плохое")
    choice = int(input("Введите номер действия: "))
    if choice == 1:
        good()
    elif choice == 2:
        bad()
    else:
        print("Ошибка ввода: нужно вввести 1 или 2.")
        mainMenu()

def good():
    print("Все хорошо.")
    input("Нажмите любую кнопку, чтобы вернуться в меню.")
    mainMenu()

def bad():
    print("Все плохо.")

mainMenu()
