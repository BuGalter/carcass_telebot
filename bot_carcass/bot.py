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
    get_name_method = get_method_url(base_url, 'get_updates')
    if get_name_method is None:
        logging.warning('Сommand not defined!')
        return
    print(get_name_method)


if __name__ == '__main__':
    print('Bot - start work!')
    main()
    print('Bot - finished work!')
