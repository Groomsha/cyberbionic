# Ввод строки
string = input('Введите строку: ')

# Проверка, есть ли в данной строке символ q
if 'q' in string:
    print('В этой строке есть символ "q"')
else:
    print('В этой строке нет символа "q"')
    string += 'q'
print(string)