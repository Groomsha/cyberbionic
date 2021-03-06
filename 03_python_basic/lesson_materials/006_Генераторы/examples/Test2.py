"""
Создание бесконечной последовательности

В Python для того, чтобы получить конечную последовательность мы обычно вызываем функцию range(). Затем мы передаем
её значение как аргумент в функцию list():
"""
a = range(5)
print(list(a))

# [0, 1, 2, 3, 4]

"""Создание же бесконечной последовательности стопроцентно потребует использования генератора. Причина проста — 
ограниченность памяти нашего компьютера.
"""


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


"""
Этот блок кода не велик и хорошо смотрится. Сперва, задаем переменную num и создаем бесконечный цикл. Затем 
немедленно извлекаем num с помощью yield в ее исходном состоянии (это во многом повторяет то, что делает range()). 
После этого мы увеличиваем num на 1.

Если попробовать запустить этот код в теле цикла for, то увидим, что на самом деле он бесконечный:
"""


for i in infinite_sequence():
    print(i, end=" ")

"""
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39 40 41 42
[...]
6157818 6157819 6157820 6157821 6157822 6157823 6157824 6157825 6157826 6157827
6157828 6157829 6157830 6157831 6157832 6157833 6157834 6157835 6157836 6157837
6157838 6157839 6157840 6157841 6157842
Traceback (most recent call last):
  File "D:\CBS\Модуль 3 - Python Базовый\006_Генераторы\examples\Test2.py", line 34, in <module>
    print(i, end=" ")
KeyboardInterrupt

Эта программа будет исполняться, до тех пор, пока ее не остановите вручную.
Вместо использования Loop, вы также можете использовать на генераторе функцию next(). Это окажется особенно удобным при 
тестировании работы генератора в консоли:
"""
gen = infinite_sequence()
next(gen)
# 0
next(gen)
# 1
next(gen)
# 2
next(gen)
# 3
"""
Здесь у нас показан генератор, под названием gen, который мы можем вручную перебирать с помощью вызова функции next(). 
Это работает как отличная проверка. Она позволяет нам убедиться что генератор выдает результат, который мы от него 
ожидаем.

Примечание: Когда мы используем next(), Python вызывает метод .__next__(), для функции, которая передается в качестве 
аргумента. При этом существуют специальные возможности. Если интересно, попробуйте поменять аргументы, которые
передаются в next() и посмотрите на результат.
"""
