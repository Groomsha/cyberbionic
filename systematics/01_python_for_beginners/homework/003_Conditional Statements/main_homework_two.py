# Напишите программу, которая вычисляет значение функции
# в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
#
# y = x2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
#
# Вычисление значения функции оформить в виде программной функции,
# которая принимает значение x, а возвращает полученное значение функции (y).

number_x = int(input("Введите значение X: "))
number_y = None

if -5 <= number_x <= 5:
	number_y = number_x * 2
elif number_x < -5:
	number_y = 2 * number_x -1
elif number_x > 5:
	number_y = 2 * number_x

print(number_y)
