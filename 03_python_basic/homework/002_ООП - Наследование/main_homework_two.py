# Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши.
# Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.

number_one = int(input('Введите число для определения его факториала: '))

result = 1
for number in range(1, number_one + 1):
	if number <= number_one:
		result = result * number
	else:
		break

print(f'\nФакториал числа {number_one}! = {result}')
