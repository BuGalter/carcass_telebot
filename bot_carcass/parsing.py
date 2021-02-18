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

"""Модуль для хранения доступных боту методов.

Основное назначение - хранение методов бота для работы с апи телеграм

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

from commands import BOT_COMMANDS


def get_data_update(response: dict) -> list:
    """Функция для получения списка, который содержит ответы

    Описание -

    """
    return response['result']


def get_id_update(update: dict) -> int:
    """Функция для получения номера обновления

    Описание -

    """
    return update['update_id']


def get_chat_id(update: dict) -> int:
    """функция для получения номера чата

    Описание -

    """
    return update['message']['chat']['id']


def get_name_user(update: dict) -> str:
    """функция для получения номера чата

    Описание -

    """
    return update['message']['chat']['first_name']


def get_text_update(update: dict) -> str:
    """функция для получения текста сообщения

    Описание -

    """
    return update['message']['text']


def parsing_text_update(text: str) -> str:
    """функция для получения текста сообщения

    Описание -

    """
    if text in BOT_COMMANDS.keys():
        return BOT_COMMANDS[text]
    else:
        return BOT_COMMANDS['not_command']
