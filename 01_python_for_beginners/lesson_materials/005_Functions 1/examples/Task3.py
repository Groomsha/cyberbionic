# Функция с использованием опциональных параметров
def add(a, b=1, c=1):
    return a + b + c


a1 = int(input('Введите первое значение: '))
a2 = int(input('Введите второе значение: '))
a3 = int(input('Введите третье значение: '))
print(add(a1)) # значение будет = a1 + 1 + 1
print(add(a1, a2)) # значение будет = a1 + a2 + 1
print(add(a1, a2, a3))

