# правильное подключение модулей:
# import os
# import sys
# неправильно:
# import os, sys

# импорты стандартной библиотеки
# импорты сторонних библиотек
# импорты модулей текущего проекта

# неправильное подключение модулей
# import math, random
# правильное подключение нескольких функций модуля
from math import cos, sin


print(cos(45) + sin(75))

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)
# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase. Замечание: когда
# вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
# HTTPServerError лучше, чем HttpServerError.
#  mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
#  Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями —
# уродливо!)
# пробелы не ставятся:
x = cos(45) + sin(75)
# Сразу после открывающей скобки и перед закрывающей:
#  —  так не надо.
print(x)
# print ( int ( input ( ' dfg dfg dfg' ) ) )
# Неправильно:
# print( '    dfg dfg dfg' )
# Правильно:
print('\n\tdfg dfg dfg')
# Перед скобками при вызове аргумента. Неправильно: arg (1). Правильно: 
# arg(1)

# Перед скобками индекса и среза: 
# dict['step'] = map[i]

# Между именем параметра/аргумента, знаком «=» и значением: min(a=10, b=input).

# не выравнивайте код лишними пробелами. По сторонам от «=» ставьте не больше одного пробела. Не пытайтесь  с помощью
# отступов придать блоку вид таблицы или оглавления. Это замедляет чтение и понимание написанного.

# Лучше ставьте по одному пробелу по сторонам от знаков арифметических действий:

# x = (y + 1) * (y — a)
# Не рекомендуется записывать несколько команд в одну строку через точку с запятой. Вместо "act1(); act2(); act3()"  —
# пишите:

# act1()
# act2()
# act3()

# name = '1'
# print(Name)
