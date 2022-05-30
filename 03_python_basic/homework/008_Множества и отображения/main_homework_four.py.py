# Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает произвольное
# количество именованных параметров. Вызовите её с созданным словарём и явно указывая параметры.

class YearException(Exception):
	def __init__(self) -> None:
		pass

	def __str__(self) -> str:
		return f"Недопустимое значение:"


class YouYear:
	def __init__(self, year: int) -> None:
		if year == 2022:
			self.__year: int = year
		else:
			raise YearException


if __name__ == '__main__':
	my_year = YouYear(2021)
