# ToDo

Простое приложение ToDo с возможностью добавлять и удалять задачи, также присутствует флаг выполнения задачи
***

## Технологии

Создан с использованием Python 3.8, Flask 2.0.3 и Flask-SQLAlchemy 2.5.1.
***

## Как начать

Необходимо скопировать репозиторий на свой локальный компьютер. Для этого перейти в каталог (например, рабочий стол)

```
cd desktop
```

и выполнить команду

```
git clone https://github.com/rufreedomman/todo_flask
```

Открыть проект в IDE. Создать виртуальное окружение

```
python3 -m venv venv
. venv/bin/activate
```

Установить или скопировать необходимые пакеты, указанные в файле requirements.txt. 

```
pip install Flask
pip install Flask-SQLAlchemy

или

pip install -r requirements.txt
```

и запустить локальный сервер

```
flask run
```