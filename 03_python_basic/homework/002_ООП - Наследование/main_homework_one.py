# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод edit_document
# выводит на экран информацию о том, что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён. Введите с клавиатуры лицензионный
# ключ и, если он корректный, создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.

while True:
	number_one = int(input('Введите первое натуральное число: '))
	number_two = int(input('Введите второе натуральное число: '))
	print('='*40, end='\n\n')

	if number_one < number_two:
		for number in range(number_one, number_two + 1):
			print(f'В диапазоне натуральное число: {number}')
		break
	else:
		print('\nПервое натуральное число не может быть больше второго. Повторите ввод.')
		print('=' * 70, end='\n\n')
