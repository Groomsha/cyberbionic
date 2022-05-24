# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение,
# деление и возведение в степень. Программа должна выдавать сообщения об ошибке и продолжать работу при вводе
# некорректных данных, делении на ноль и возведении нуля в отрицательную степень.


class English:
	@staticmethod
	def greeting() -> None:
		print('Glory to Ukraine. Glory to heroes!')


class Spanish:
	@staticmethod
	def greeting() -> None:
		print('Gloria a Ucrania. ¡Gloria a los héroes!')


if __name__ == '__main__':
	def hello_friend():
		eng_speak.greeting()
		spa_speak.greeting()

	eng_speak = English()
	spa_speak = Spanish()
	hello_friend()
