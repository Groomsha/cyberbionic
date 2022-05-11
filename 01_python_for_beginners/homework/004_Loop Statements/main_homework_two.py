# Факториалом числа n называется число 𝑛! = 1 ∙ 2 ∙ 3 ∙ … ∙ 𝑛. Создайте программу,
# которая вычисляет факториал введённого пользователем числа.

number_one = int(input('Введите число для определения его факториала: '))

result = 1
for number in range(1, number_one + 1):
	if number <= number_one:
		result = result * number
	else:
		break

print(f'\nФакториал числа {number_one}! = {result}')
