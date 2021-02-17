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

"""Основной, запускаемый модуль, содержит код бота.

Основное назначение -

Global variable
---------------


Functions
---------
get_updates_longpolling()
    делает запрос к серверу телеграм для получения сообщений
"""
import logging
from urls import get_token, get_base_url, get_method_url
from bot_methods import get_updates_longpolling, send_message


def check_url(url: str):
    """Функция для проверки существования урла

    Описание -
    """
    if url is None:
        logging.warning('Сommand not defined!')
        exit('Bot - finished work, not correct!!!')


def main():
    """Модуль-

    Описание-

    """
    token = get_token()
    if token is None:
        logging.warning('An error occurred while running the bot!')
        return
    base_url = get_base_url(token)
    print(base_url)
    update_url = get_method_url(base_url, 'get_updates')
    check_url(update_url)
    request, code = get_updates_longpolling(update_url)
    if code != 200:
        logging.warning('Work bot, stoped!!! Error{}'.format(code))
    print(code)
    print(request)
    send_message_url = get_method_url(base_url, 'send_message')
    check_url(send_message_url)
    code = send_message(send_message_url, 990665431)
    if code != 200:
        logging.warning('Work bot, stoped!!! Error{}'.format(code))
    print(code)


if __name__ == '__main__':
    print('Bot - start work!')
    main()
    print('Bot - finished work!')
