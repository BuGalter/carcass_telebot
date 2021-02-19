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

"""Модуль хранения функций для проверок.

Основное назначение - хранение функций, которые служат для проверки
корректности данных, используемых ботом в работе

Functions
---------
check_url()
    Функция для проверки существования урла
check_status_code()
    Функция для проверки статуса кода ответа
"""

import sys
import logging


def check_url(url: str) -> None:
    """Функция для проверки существования урла.

    Описание - функция нужна для проверки передан корректынй урл
    или None

    Parameters
    ----------
    url : str
        проверяемый урл

    Returns
    -------
    Ничего, если все в порядке, а иначе прерывает работу бота и выводит
    сообщение об этом

    """
    if url is None:
        logging.warning('Сommand not defined!')
        sys.exit('Bot - finished work, not correct!!!')


def check_status_code(code: int) -> None:
    """Функция для проверки статуса кода ответа.

    Описание -

    Parameters
    ----------
    code : int
        проверяемый код ответа

    Returns
    -------
    Ничего, если все в порядке, а иначе прерывает работу бота и выводит
    сообщение об этом

    """
    if code != 200:
        logging.warning('Work bot, stoped!!! Error %d!' % code)
        sys.exit('Bot - finished work, not correct!!!')
