# Задача "Налоги"
# Входные данные: цена товара (float), Величина налога (int);
# Выходные данные: Итоговая цена(int?)

def calcilate_tax(price, tax):
    tax += 10    # Налог увеличивается на 10%
    total = price + (price * tax / 100)    # Стоимость с налогоом
    return total

myPrice = float(input("Введите цену: "))    # Стоимость товара
myTax = int(input("Введите налог: "))    # Налог 1

totalPrice = calcilate_tax(myPrice, myTax)
print()
newTax = int(input("Введите новый налог: "))    # Сверхналог
totalPrice = calcilate_tax(totalPrice, newTax)    # Новая цена

print("Итоговая цена:", totalPrice)
