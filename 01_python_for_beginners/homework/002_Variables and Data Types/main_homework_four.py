# Напишите программу, которая запрашивает у пользователя радиус круга
# и выводит его площадь. Формула площади круга S = pi*r^2

PI = 3.141592653589793238462643
radius = float(input("Введите радиус круга: "))

result = round(PI * radius ** 2, 2)

print("=" * 45)
print(f"Результат площади круга: {result}", end="\n\n")
print("Слава Україні! Героям слава! Смерть ворогам!")