# Используя сервис https://jsonplaceholder.typicode.com/ попробуйте построить различные типы запросов и
# обработать ответы. Необходимо попрактиковаться с urllib и библиотекой requests. Рекомендуется сначала
# попробовать выполнить запросы, используя urllib, а затем попробовать реализовать то же самое используя requests

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
