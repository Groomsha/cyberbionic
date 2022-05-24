# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.


class Base:
	def __init__(self) -> None:
		pass

	def method(self) -> str:
		return "Hello from Base"


class Child(Base):
	def __init__(self) -> None:
		super(Child, self).__init__()

	def method(self) -> str:
		return 'Hello from Child'


if __name__ == '__main__':
	base = Base()
	child = Child()

	print(base.method(), end='\n')
	print(child.method())
