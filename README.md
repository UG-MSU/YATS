# YATS – Backend

# Использование

**Примечание.** Программу необходимо запускать на операционной системе с ядром Linux. Для работы провеляющей системы также необходим установленный `docker`

Клонируем репозиторий проекта и переходим в его папку:

    $ git clone https://github.com/UG-MSU/YATS
    $ cd YATS
    
Создаем и активируем `virtualenv` при необходимости

Клонируем репозиторий библиотеки для контейниризации и устанавливаем её

    $ git clone https://github.com/UG-MSU/container-lib
    $ cd container-lib
    $ pip install .
    $ cd ..

Устанавливаем необходимые зависимости:

    $ pip install -r requirements.txt
    
    
Применяем миграции базы данных:

    $ python manage.py migrate
    

Запускаем сервер

    $ python manage.py runserver