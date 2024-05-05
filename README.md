# Test task

Используемые технологии:
- [Docker](https://www.docker.com) - платформа разворачивания приложений
- [Python 3.12](https://www.python.org) - язык программирования Python


Параметры окружения приложения
------------------------------
Название параметра| Допустимые значения | Пример    |Описание
-------------------|---------------------|-----------|---------
HOST| `[a-zA-Z0-9]+`      | `0.0.0.0` |Хост
PORT| `INT`               | `5000`    |Порт

## Сборка в Docker

Для сборки и запуска в Docker контейнере следует выполнить команду

(предварительно заполните .env файл по 
примеру .env.example)

    $ sudo chmod +x docker_build.sh && ./docker_build.sh

## Удаление контейнера Docker

Для удаления контейнера выполнить команду

    $ docker stop test_image
