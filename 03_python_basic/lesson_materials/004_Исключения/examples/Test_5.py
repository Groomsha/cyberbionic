print('Как расшифровывается ВОЗ?\n1-Всемирная организация здравоохранения\n2-Всероссийская организация защиты\n'
      '3-Всероссийская особая здравница\n4-Владение особого значения')
while True:
    try:
        answer = int(input('Введите Ваш вариант ответа(целое число): '))
        break
    except:
        print('Ошибка! Введите номер правильного ответа')
if answer == 1:
    print('Абсолютно верно!')
else:
    print('Нет. ВОЗ - это Всемирная организация здравоохранения')
