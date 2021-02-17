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


def get_id_last_update(response: dict) -> int:
    """Функция для получения номера последнего обновления

    Описание -

    """
    data_last_update_id = response['result'][len(response['result']) - 1]
    last_update_id = data_last_update_id['update_id']
    return last_update_id


def get_data_last_update(response: dict) -> dict:
    """функция для получения тела последнего сообщения

    Описание -

    """
    result = response['result']
    number_last_update = len(result) - 1
    return result[number_last_update]


def get_chat_id(last_update: dict) -> int:
    """функция для получения тела последнего сообщения

    Описание -

    """
    chat_id = last_update['message']['chat']['id']
    return chat_id
