# YATS – Backend

# Использование

Клонируем репозиторий проекта и переходим в его папку:

    $ git clone https://github.com/UG-MSU/YATS
    $ cd YATS
    
Создаем и активируем `virtualenv` при необходимости
    
Устанавливаем необходимые зависимости:

    $ pip install -r requirements.txt
    
    
Применяем миграции базы данных:

    $ python manage.py migrate
    

Запускаем сервер

    $ python manage.py runserver