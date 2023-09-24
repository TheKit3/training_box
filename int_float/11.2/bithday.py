age = int(input("Возраст: "))
bodyTemp = float(input("Температура тела: "))

donat = round(age * bodyTemp * 1.5, 0)

print("Донат:", donat)