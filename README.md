# carcass_telebot

Создан для того, чтобы изучить апи телеграм.

## Introduction

Пакет содержит каркас простого чат-бота для работы с апи телеграм. Он поможет
быстро узнать возможности апи телеграм. Бот реализован в процедурном стиле,
чтобы было проще понять, как осуществляется взимодействие с сервером телеграм.
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

## Installing

## Getting started


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

Папка tests содержит юнит тесты всех модулей, кроме основного, который содержит функции
main и используется для запуска бота.

Для тестирования используется pytest.

Для запуска тестов, необходимо перейти в папку с тестами и запустить с помощью команды:

`(venv) \carcass_telebot\tests>python -m pytest -v`

## Authors

Nick - **BuGalter**

Name - *Valery Yakubchik*

## License

Этот проект лицензируется в соответствии с лицензией Apache License 2.0 — подробности 
см. в файле LICENSE.