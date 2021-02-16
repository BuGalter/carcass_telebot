"""Модуль для хранения урлов и функций для их формирования

Основное назначение - хранение урлов и создание урлов для работы
с апи телеграм

Global variable
---------------
URL : str
    базовый урл для запросов к апи телеграм

GET_UPDATES : str
    часть урла для получения новых сообщений

SEND_MESSAGE : str
    часть урла для отправки ответных сообщений

Functions
---------
get_token()
    Получает токен из .env
get_base_url()
    Формирует базовый урл из токена и начального урла из переменной URL
get_update_url()
    Формирует урл из переменной GET_UPDATES и базового урла
"""

from dotenv import dotenv_values
import logging

URL = 'https://api.telegram.org/bot'

GET_UPDATES = 'getUpdates'

SEND_MESSAGE = 'sendMessage'


def get_token():
    """Получает токен из .env

    Функция получает токен из .env. Для хранения и получения секретной
    информации используется python-dotenv

    Parameters
    ----------
    TOKEN : (dict key)
        переменная в файле .env, содержит токен для апи телеграм

    Returns
    -------
    token : (string)
        string в случае, если переменная задана
        если переменная не определенна сообщает об ошибке
    """

    my_env_variables = dotenv_values(".env")
    if len(my_env_variables) == 0:
        logging.warning('Not token in file!!!')
        return None
    keys = dict.keys(my_env_variables)
    if 'TOKEN' in keys:
        return my_env_variables['TOKEN']
    else:
        logging.warning('Not token in dict!!!')
        return None


def get_base_url(token: str) -> str:
    """Собирает базовый урл для доступа  к апи телеграм

    Функция склеивает урл и полученный токен, возвращает базовый урл

    Parameters
    ----------
    token : (string)
        переменная, содержит токен для апи телеграм

    Returns
    -------
    base_url : (string)
        переменная сожержит базовый урл для запросов к апи
    """

    base_url = URL + token + '/'
    return base_url


def get_update_url(base_url: str) -> str:
    """Собирает урл для получения новых сообщений от апи телеграм

    Функция склеивает базовый урл и и константу GET_UPDATES, возвращает урл
    необходимый для получения обновлений от апи телеграм

    Parameters
    ----------
    base_url : (string)
        переменная, содержит, базовый урл

    Returns
    -------
    update_url : (string)
        переменная сожержит урл для для получения новых сообщений
    """

    update_url = base_url + GET_UPDATES
    return update_url
