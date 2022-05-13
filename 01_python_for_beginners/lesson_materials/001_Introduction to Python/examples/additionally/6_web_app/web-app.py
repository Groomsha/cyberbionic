# Пример простейшего веб-приложения.
# Он предназначен лишь для демонстрации создания
# приложений разных видов. Данные возможности языка Python подробно будут
# рассмотрены в следующих уроках данного курса и в следующих курсах.

# Для данного примера используется фреймворк Flask (http://flask.pocoo.org)
# Сначала установить Flask. Это можно сделать командой в консоли:
# pip install Flask

# Импортируем всё необходимое из библиотеки flask
from flask import Flask, request, render_template

# Создаём объект веб-приложения
app = Flask(__name__)


@app.route('/')
def hello_world():          # объявление пользовательской функции
    """
    Если нужно объявить большую строку (в смысле строки в Python)
    из нескольких строк текста (в обычном понимании слова "строка"),
    то она обрамляется сразу тремя одинарными или двойными кавычками
    с обоих сторон.

    Если такая строка стоит в самом начале функции, то она играет
    роль особого вида комментариев — документационной строки (docstring).

    Декоратор app.route (о декораторах в курсе Python Essential)
    указывает, что функция будет вызываться, когда пользователь
    переходит по определённому адресу в браузере.

    Данная функция будет выдавать строку 'Hello World!', когда
    пользователь заходит на главную страницу сайта
    """
    return 'Hello World!'


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    """
    По адресу http://адрес.сайта/hello/ у нас будет находится страница,
    на которой пользователь сможет ввести своё имя и получить приветствие.

    Здесь мы указываем не только URL-адрес, но и разрешённые HTTP-методы.
    Таким образом, по этому адресу можно будет и получать страницу,
    и отправлять данные формы, в которой пользователь вводит своё имя
    """

    if request.method == 'POST':     # если пользователь ввёл своё имя
        name = request.form['name']  # то получаем его
    else:
        name = None                  # иначе присвоим name значение None
    # После этого отдаём пользователю HTML-страницу на основе шаблона
    # hello_form.html, в который мы передаём имя пользователя
    # (HTML можно изучить на соответсвующем курсе по фронтенд-разработке).
    return render_template('hello_form.html', name=name)


@app.route('/<name>')
def hello_buddy(name):
    """
    Любой другой адрес мы считаем именем пользователя
    и выдаём соответствующее приветствие.
    """
    return 'Hello, ' + name + '!'


# Если данный файл был запущен как главный, а не импортирован
# из другого модуля, то запускаем сервер веб-приложения.
# По умолчанию он будет доступен по адресу http://localhost:5000/
if __name__ == '__main__':
    app.run()