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

"""Модуль содержит тесты urls.py.

Основное назначение - тестирование функции, которые содержит модуль urls.py

Functions
---------
test_get_token()
    тест, когда в файле содержится переменная TOKEN,
    которая содержит коректный токен для апи телеграм.
test_get_token_none()
    тест, когда в файле содержится любая другая пременная,
    а не TOKEN.
test_get_token_absent()
    тест, когда файл пуст.
test_get_base_url()
    тест для подтверждения корретной работы функции.
test_get_method_url()
    тест для подтверждения корректной работы, если передаются
    имена методов, которые использует бот.
test_get_method_url_none()
    тест для подтверждения корректной работы, если передаются
    имена методов, которые бот не знает.
"""
from bot_carcass import urls


def test_get_token():
    """Тест для корректных данных.

    Описание - тест, когда в файле содержится переменная TOKEN,
    которая содержит коректный токен для апи телеграм.
    """
    result = urls.get_token(".env1")
    assert result == 'FFFFFFF'


def test_get_token_none():
    """Тест для корректных данных, но не верное имя переменной.

    Описание - тест, когда в файле содержится любая другая пременная,
    а не TOKEN.
    """
    result = urls.get_token('.env2')
    assert result is None


def test_get_token_absent():
    """Тест для пустого файла.

    Описание - тест, когда файл пуст.
    """
    result = urls.get_token('.env3')
    assert result is None


def test_get_base_url():
    """Тест функции get_base_url().

    Описание - тест для подтверждения корретной работы функции.
    """
    result = urls.get_base_url('allokey')
    assert result == 'https://api.telegram.org/botallokey/'


def test_get_method_url():
    """Тест функции get_method_url, когда передаются существующие методы.

    Описание - тест для подтверждения корректной работы, если передаются
    имена методов, которые использует бот.

    Variables
    ---------
    url : str
        произвольный урл

    methods : dict
        набор методов, которые определенны для бота
    """
    url = 'https://api.telegram.org/'
    methods = {'get_updates': 'get_updates',
               'send_message': 'send_message',
               'edit_message': 'edit_message'}
    result = urls.get_method_url(url, methods['get_updates'])
    assert result == 'https://api.telegram.org/getUpdates'
    result = urls.get_method_url(url, methods['send_message'])
    assert result == 'https://api.telegram.org/sendMessage'
    result = urls.get_method_url(url, methods['edit_message'])
    assert result == 'https://api.telegram.org/editMessageText'


def test_get_method_url_none():
    """Тест функции get_method_url, когда передаются не существующие методы.

    Описание - тест для подтверждения корректной работы, если передаются
    имена методов, которые бот не знает.
    """
    result = urls.get_method_url('https://api.telegram.org/', 'none')
    assert result is None
