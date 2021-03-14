# carcass_telebot

Создан для того, чтобы изучить апи телеграм.

## Introduction

Пакет содержит каркас простого чат-бота для работы с апи телеграм. Он помог
узнать возможности апи телеграм. Бот реализован в процедурном стиле,чтобы было 
проще понять, как осуществляется взимодействие с сервером телеграм.
Если добавить пару принтов, можно посмотреть в каком виде поступают ответы от
сервера телеграм. Данная реализация не является эталонной))).

## Note

Проект исключительно для обучения, был задуман, чтобы изучить возможности апи телеграм.
Параллельно попробовать оформить полноценный проект, используя различные инструменты
языка Python. Строго не судите))). Буду рад **разумной критике**, чтобы стать лучше.

## Preconditions

* Для корректной работы необходим Python версии от 3.8.
* Для управления зависимостями, используется poetry.
* Для тестирования, используется pytest.
* Для хранения токена используется файл .env.
* Для скачивания кода необходим установленный git

## Installing

Пакет создан в учебных целях. Его распространение не предусматривается.

* Код можно скачать, использую команду: 

`git clone https://github.com/BuGalter/carcass_telebot.git`

* Далее необходимо перейти в директорию: `carcass_telebot` и создать виртуальное
окружение:

`python -m venv venv`

* Активировать виртуальное окружение:
    * Windows:
    `.\venv\Scripts\activate.bat`

    * Linux:
    `source venv/bin/activate`

* Установить poetry:

`pip install poetry`

* Установить зависимости:
    * Без модулей, которые использовались для раработки:

    `poetry install --no-dev`

    * Все модули:

    `poetry install`

Пакет готов к использованию.

## Getting started

Чтобы начать пользоваться, необходимо:

1. Зарегистрировать своего бота у BotFather https://core.telegram.org/bots
1. Получить токен
1. Создать в директории bot_carcass файл .env и поместить в него строку TOKEN=Ваш токен
1. Запустить бота, находясь в директории `bot_carcass`, с помощью команды:

`python bot.py`

## Documentation

Документация находится в файла проекта.
Посмотреть документацию можно с помощью команды python - m pydoc, пример для файла init.py:

```
(venv) \carcass_telebot\bot_carcass>python -m pydoc __init__ 
```

Имя файла без расширения. Таким образом, можно посмотреть документацию для всех
файлов с расширением - py.

**При работе в консоле Windows возможно некорректное отображение символов в кодировке utf-8.
Чтобы это исправить, используйте команду *chcp 1251* в консоли.**

## Testing

Папка tests содержит юнит тесты всех модулей, кроме bot.py и bot_commands.

Для тестирования используется pytest.

Для запуска тестов, необходимо перейти в папку с тестами и запустить с помощью команды:

`(venv) \carcass_telebot\tests>python -m pytest -v`

## Authors

Nick - **BuGalter**

Name - *Valery Yakubchik*

## License

Этот проект лицензируется в соответствии с лицензией Apache License 2.0 — подробности 
см. в файле LICENSE.