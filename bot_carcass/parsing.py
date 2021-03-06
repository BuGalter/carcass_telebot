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

"""Модуль для хранения методов необходимых для получения данных.

Основное назначение - получение данных из ответа от апи телеграм,
которые необходимы для работы бота

Global variable
---------------
BOT_COMMANDS : dict
    Словарь для хранения команд бота

Functions
---------
get_data_update()
    функция возвращает список, который содержит сообщения,
    которые не были прочитанны
get_id_update()
    получает номер обновления из полученного словаря
get_chat_id()
    получает номер текущего чата
get_name_user()
    получает имя юзера от которого пришло сообщение
get_text_update()
    функция получает текст сообщения от пользователя
parsing_text_update()
    функция проверяет, есть ли в тексте команды, которые знает бот,
    если да то возвращает текст, соответствующий команде, если нет,
    то стандартное сообщение в котором содержиться перечень команд.
get_message_status()
    функция получает статус сообщения, сортируя
    ключи и выбирая первый элемент, полученого словаря, который
    содержит сообщение от бота
get_message_id()
    функция получает номер сообщения от пользователя
"""

BOT_COMMANDS = {'/start': 'Добрый день! Чем могу Вам помочь?',
                '/help': 'Список доступных команд:\n /start\n/help\n/settings',
                '/settings': 'Список возможных настроек:\n',
                'not_command': 'Команды:\n /start\n/help\n/settings'}


def get_data_update(response: dict) -> list:
    """Функция для получения списка, который содержит ответы.

    Описание - функция возвращает список, который содержит
    сообщения, которые не были прочитанны

    Parameters
    ----------
    response : dict
        словарь, который содержит ответ от сервера телеграм

    Returns
    -------
    response['result'] : list
        список сообщений от апи телеграм

    """
    return response['result']


def get_id_update(update: dict) -> int:
    """Функция для получения номера обновления.

    Описание - получает номер обновления из полученного словаря

    Parameters
    ----------
    update : dict
        словарь, который содержит текущий ответ от сервера телеграм

    Returns
    -------
    update['update_id'] : int
        номер текущего обновления

    """
    return update['update_id']


def get_chat_id(update: dict, status_update: str) -> int:
    """функция для получения номера чата.

    Описание - получает номер текущего чата

    Parameters
    ----------
    update : dict
        словарь, который содержит текущий ответ от сервера телеграм
    status_update : str
        состояние сообщения, изменено или новое

    Returns
    -------
    update['message']['chat']['id'] : int
        номер текущего чата

    """
    return update[status_update]['chat']['id']


def get_name_user(update: dict, status_update: str) -> str:
    """функция для получения имя юзера от которого пришло сообщение.

    Описание - получает имя юзера от которого пришло сообщение

    Parameters
    ----------
    update : dict
        словарь, который содержит текущий ответ от сервера телеграм
    status_update : str
        состояние сообщения, изменено или новое

    Returns
    -------
    update['message']['chat']['first_name'] : str
        имя пользователя текущего чата

    """
    return update[status_update]['chat']['first_name']


def get_text_update(update: dict, status_update: str) -> str:
    """функция для получения текста сообщения.

    Описание - функция получает текст сообщения от пользователя

    Parameters
    ----------
    update : dict
        словарь, который содержит текущий ответ от сервера телеграм
    status_update : str
        состояние сообщения, изменено или новое

    Returns
    -------
    update['message']['text'] : str
        сообщение от пользователя

    """
    return update[status_update]['text']


def get_message_status(update: dict) -> str:
    """функция для получения статуса сообщения от бота.

    Описание - функция получает статус сообщения, сортируя
    ключи и выбирая первый элемент, полученого словаря, который
    содержит сообщение от бота

    Parameters
    ----------
    update : dict
        новое сообщение от бота

    Returns
    -------
    message_status : str
        статус сообщения, если новое, то message, если отредактированое
        edited_message

    """
    message_status = sorted(update.keys())[0]
    return message_status


def get_message_id(update: dict, status_update: str) -> int:
    """функция для получения номера сообщения.

    Описание - функция получает номер сообщения от пользователя

    Parameters
    ----------
    update : dict
        новое сообщение от бота
    status_update : str
        состояние сообщения, изменено или новое

    Returns
    -------
    message_status : str
        статус сообщения, если новое, то message, если отредактированое
        edited_message

    """
    return update[status_update]['message_id']


def parsing_text_update(text: str) -> str:
    """функция для проверки текста на совпадение с командами бота.

    Описание - функция проверяет, есть ли в тексте команды, которые знает
    бот, если да то возвращает текст, соответствующий команде, если нет,
    то стандартное сообщение в котором содержиться перечень команд.

    Parameters
    ----------
    text : str
        текст сообщения от пользователя

    Returns
    -------
    BOT_COMMANDS[text] : str
        ответ бота

    """
    if text in BOT_COMMANDS.keys():
        return BOT_COMMANDS[text]
    return BOT_COMMANDS['not_command']
