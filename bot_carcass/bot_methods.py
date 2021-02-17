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

import requests


def get_updates_longpolling(update_url, update_id=None):
    """Получает сообщения от сервера телеграм

    Функция получает на вход урл и номер сообщения, по умолчанию None
    делает запрос к серверу телеграм и возвращает ответ в виде
    json-объекта

    Parameters
    ----------
        update_url : str
            урл для запроса, чтобы получить новые сообщения
        update_id : str
            номер последнего обновления

    Returns
    -------
        r.json() : dict json
            новые сообщения от бота
        r.status_code : int
            код ответа сервера

    """
    params = {'timeout': 100, 'offset': update_id}
    r = requests.get(update_url, data=params)
    return r.json(), r.status_code


def send_message(send_message_url, chat_id, text='Hay, I am a bot!!!'):
    """Отправляет сообщения серверу телеграма

    Описание

    Parameters
    ----------

    Returns
    -------

    """
    params = {'chat_id': chat_id, 'text': text}
    r = requests.post(send_message_url, data=params)
    return r.status_code
