"""Модуль для хранения урлов и функций для их формирования

Основное назначение - хранение урлов и создание урлов для работы
с апи телеграм

Global variable
---------------
URL : str
    базовый урл для запросов к апи телеграм
BOT_METHODS : dict
    содержит методы доступные для бота для взаимодействия с апи телеграм

Functions
---------
get_token()
    Получает токен из .env
get_base_url()
    Формирует базовый урл из токена и начального урла из переменной URL
get_method_url()
    Формирует урл из словаря методов для работы с апи телеграм BOT_METHODS
    и базового урла
"""

from dotenv import dotenv_values
import logging

URL = 'https://api.telegram.org/bot'

BOT_METHODS = {
    'get_updates': 'getUpdates',
    'send_message': 'sendMessage'
}


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


def get_method_url(base_url: str, name_method: str) -> str:
    """Собирает урл для определенный методов взаимодействия с апи телеграм

    Функция склеивает базовый урл и метод, определенный в словаре BOT_METHODS,
    возвращает урл необходимый для работы с апи телеграм

    Parameters
    ----------
    base_url : (string)
        переменная, содержит, базовый урл

    name_method : (string)
        переменная, содержит, имя метода


    Returns
    -------
    method_url : (string)
        переменная сожержит урл для работы с апи телеграм
    None
        если метод не определен
    """

    if name_method in BOT_METHODS:
        method_url = base_url + BOT_METHODS[name_method]
        return method_url
    else:
        return None
