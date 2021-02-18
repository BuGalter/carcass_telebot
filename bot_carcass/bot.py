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
from parsing import (get_id_update,
                     get_data_update,
                     get_chat_id,
                     get_text_update,
                     parsing_text_update,
                     get_name_user)


def check_url(url: str):
    """Функция для проверки существования урла

    Описание -
    """
    if url is None:
        logging.warning('Сommand not defined!')
        exit('Bot - finished work, not correct!!!')
    return


def check_status_code(code: int):
    """Функция для проверки статуса ответа

    Описание -
    """
    if code != 200:
        logging.warning('Work bot, stoped!!! Error{}'.format(code))
        exit('Bot - finished work, not correct!!!')
    return


def main():
    """Модуль-

    Описание-

    """
    token = get_token()
    if token is None:
        logging.warning('An error occurred while running the bot!')
        exit('Bot - finished work, not correct!!!')
    base_url = get_base_url(token)
    offset = 0
    while True:
        update_url = get_method_url(base_url, 'get_updates')
        check_url(update_url)
        response, code = get_updates_longpolling(update_url, offset)
        check_status_code(code)
        data_result = get_data_update(response)
        if len(data_result) == 0:
            continue
        elif len(data_result) > 0:
            for update in data_result:
                offset = get_id_update(update)
                chat_id = get_chat_id(update)
                text = get_text_update(update)
                user_name = get_name_user(update)
                answer = parsing_text_update(text)
                send_message_url = get_method_url(base_url, 'send_message')
                check_url(send_message_url)
                answer = 'Hay, %s! ' % user_name + answer
                code = send_message(send_message_url, chat_id, answer)
                check_status_code(code)
                offset += 1
        else:
            logging.warning('Not possible!!! Check the bot!!!')
    return


if __name__ == '__main__':
    print('Bot - start work!')
    main()
