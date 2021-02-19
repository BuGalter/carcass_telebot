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

Основное назначение - запуск бота, в модуле реализованна основная логика
работы бота

Functions
---------
main()
    основная функция, содержит логику работы бота и вызов вспомогательных
    методов
"""
import sys
import logging
from urls import get_token, get_base_url, get_method_url
from bot_methods import get_updates_longpolling, send_message
from parsing import (get_id_update,
                     get_data_update,
                     get_chat_id,
                     get_text_update,
                     parsing_text_update,
                     get_name_user)
from checks import check_url, check_status_code


def main() -> None:
    """Основная функция, содержит логику работы бота.

    Описание - функция содержит инициализацию бота, получение токена,
    формирование базового урла для запросов. Основной цикл в котором
    происходит запрос к апи телеграм для получения сообщений от
    пользователей. Обработка полученного сообщения и отправка ответного.
    Используется метод при котором запрос к серверу происходит 1 раз
    в 100 секунд, если за этот промежуток сообщений не было, делается
    повторный. Если ответ поступил, он обрабатывается и бот посылает
    ответное сообщение, при этом помечает полученное сообщение, как
    прочитанное, чтобы сервер телеграма его больше не передавал.
    Для вывода сообщений используется logging, чтобы можно было легко
    перейти к записи в реальные лог файлы при необходимости.
    Если бот не работал, отвечаем на все сообщения, которые поступили.

    Parameters
    ----------
    token
        содержит токен
    base_url
        содержит базовый урл
    offset
        идентификаторов ранее полученных обновлений.
        Обновление считается подтвержденным, как только вызывается getUpdates
        со смещением, превышающим его update_id.
    response
        ответ от апи телеграм
    code
        код статуса ответа

    """
    token = get_token()
    if token is None:
        logging.warning('An error occurred while running the bot!')
        sys.exit('Bot - finished work, not correct!!!')
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
        if len(data_result) > 0:
            for update in data_result:
                print(update)
                """Получаем из отсортированого списка ключей, который содержит статус message"""
                key_update = sorted(update.keys())[0]
                print(key_update)
                print(update[key_update].keys())
                offset = get_id_update(update)
                chat_id = get_chat_id(update, key_update)
                send_message_url = get_method_url(base_url, 'send_message')
                check_url(send_message_url)
                if 'text' in update[key_update].keys():
                    text = get_text_update(update, key_update)
                    user_name = get_name_user(update, key_update)
                    answer = parsing_text_update(text)
                    answer = 'Hay, %s! ' % user_name + answer
                    code = send_message(send_message_url, chat_id, answer)
                else:
                    code = send_message(send_message_url, chat_id)
                check_status_code(code)
                offset += 1
                answer = ''
        else:
            logging.warning('Not possible!!! Check the bot!!!')


if __name__ == '__main__':
    print('Bot - start work!')
    main()
