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

Functions
---------
get_updates_longpolling()
    Получает сообщения от сервера телеграм
send_message()
    Отправляет сообщения серверу телеграма
"""

import requests


def get_updates_longpolling(update_url, update_id=0):
    """Получает сообщения от сервера телеграм

    Функция получает на вход урл и номер сообщения, по умолчанию 0
    делает запрос к серверу телеграм и возвращает ответ в виде
    json-объекта и код статуса ответа

    Parameters
    ----------
        update_url : str
            урл для запроса, чтобы получить новые сообщения
        update_id : int
            номер последнего обновления

    Returns
    -------
        r.json() : dict json
            новые сообщения от бота
        r.status_code : int
            код статуса ответа

    """
    params = {'timeout': 100, 'offset': update_id}
    r = requests.get(update_url, data=params)
    return r.json(), r.status_code


def send_message(send_message_url, chat_id, text='Hay, I am a bot!!!'):
    """Отправляет сообщения серверу телеграма

    Описание - на вход получает урл для отправки сообщений, номер чата
    и текст, по умолчанию - 'Hay, I am a bot!!!'. Возвращает код статуса
    ответа.

    Parameters
    ----------
        send_message_url : str
            урл для отправки сообщений
        chat_id : int
            номер чата, куда отправлять сообщение
        text : str
            текст сообщения, по умолчанию 'Hay, I am a bot!!!'

    Returns
    -------
        r.status_code : int
            код стутуса ответа

    """
    params = {'chat_id': chat_id, 'text': text}
    r = requests.post(send_message_url, data=params)
    return r.status_code
