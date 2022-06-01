# Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.

if __name__ == '__main__':
	homework = 'Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable'
	iterable = iter(homework[::-1])

	while True:
		try:
			print(next(iterable))
		except StopIteration:
			break
