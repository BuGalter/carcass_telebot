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

Functions
---------

"""

from commands import BOT_COMMANDS


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


def get_chat_id(update: dict) -> int:
    """функция для получения номера чата.

    Описание - получает номер текущего чата

    Parameters
    ----------
        update : dict
            словарь, который содержит текущий ответ от сервера телеграм

    Returns
    -------
        update['message']['chat']['id'] : int
            номер текущего чата

    """
    return update['message']['chat']['id']


def get_name_user(update: dict) -> str:
    """функция для получения имя юзера от которого пришло сообщение.

    Описание - получает имя юзера от которого пришло сообщение

    Parameters
    ----------
        update : dict
            словарь, который содержит текущий ответ от сервера телеграм

    Returns
    -------
        update['message']['chat']['first_name'] : str
            имя пользователя текущего чата

    """
    return update['message']['chat']['first_name']


def get_text_update(update: dict) -> str:
    """функция для получения текста сообщения.

    Описание - функция получает текст сообщения от пользователя

    Parameters
    ----------
        update : dict
            словарь, который содержит текущий ответ от сервера телеграм

    Returns
    -------
        update['message']['text'] : str
            сообщение от пользователя

    """
    return update['message']['text']


def parsing_text_update(text: str) -> str:
    """функция для проверки текста на совпадение с командами бота.

    Описание - функция проверяет, есть ли в тексте команды, которые знает бот,
    если то возвращает текст, соответствующий команде, если нет, то стандартное
    сообщение в котором содержиться перечень команд.

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
