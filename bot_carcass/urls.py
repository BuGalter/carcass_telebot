# !/usr/bin/env python
# Copyright [2021] [Valeriy Yukubchik]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Модуль для хранения урлов и функций для их формирования.

Основное назначение - хранение урлов и создание урлов для работы
с апи телеграм

Global variable
---------------
URL : str
    базовый урл для запросов к апи телеграм
BOT_METHODS : dict
    содержит методы доступные для бота, чтобы взаимодействия с апи телеграм

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
import logging
from typing import Union
from dotenv import dotenv_values

URL = 'https://api.telegram.org/bot'

BOT_METHODS = {
    'get_updates': 'getUpdates',
    'send_message': 'sendMessage',
    'edit_message': 'editMessageText'
}


def get_token(name_env_file: str) -> Union[str, None]:
    """Получает токен из .env.

    Функция получает токен из .env. Для хранения и получения секретной
    информации используется python-dotenv

    Parameters
    ----------
    TOKEN : (dict key)
        переменная в файле .env, содержит токен для апи телеграм

    name_env_file : str
        содержит путь к файлу в котором храниться токен

    Returns
    -------
    token : (string)
        string в случае, если переменная задана
        если переменная не определенна сообщает об ошибке
    None
        если нет в списке загруженных переменных из .env или
        если файл .env пустой

    """
    my_env_variables = dotenv_values(name_env_file)
    if len(my_env_variables) == 0:
        logging.warning('Not token in file!!!')
        return None
    keys = dict.keys(my_env_variables)
    if 'TOKEN' in keys:
        return my_env_variables['TOKEN']
    logging.warning('Not token in dict!!!')
    return None


def get_base_url(token: str) -> str:
    """Собирает базовый урл для доступа  к апи телеграм.

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


def get_method_url(base_url: str, name_method: str) -> Union[str, None]:
    """Собирает урл для определенного метода взаимодействия с апи телеграм.

    Функция склеивает базовый урл и метод, определенный в словаре BOT_METHODS,
    возвращает урл необходимый для работы с апи телеграм

    Parameters
    ----------
    base_url : (string)
        переменная, содержит, базовый урл

    name_method : (string)
        переменная, содержит, имя метода - ключ в словаре BOT_METHODS


    Returns
    -------
    method_url : (string)
        переменная содержит урл для работы с апи телеграм
    None
        если метод не определен в словаре BOT_METHODS

    """
    if name_method in BOT_METHODS:
        method_url = base_url + BOT_METHODS[name_method]
        return method_url
    return None
