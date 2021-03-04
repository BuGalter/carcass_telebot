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

"""Модуль содержит тесты функцию для получения токена.

Основное назначение - тестирование функции get_token

Functions
---------
tes_get_token()
    Тесты для функции get_token, получены корректные данные

tes_get_token_none()
    Тесты для функции get_token, когда указан неверный ключ

tes_get_token_absent()
    Тесты для функции get_token, файл не содержит данные
"""
from bot_carcass import urls


def test_get_token():
    result = urls.get_token(".env1")
    assert result == 'FFFFFFF'


def test_get_token_none():
    result = urls.get_token('.env2')
    assert result is None


def test_get_token_absent():
    result = urls.get_token('.env3')
    assert result is None


def test_get_base_url():
    result = urls.get_base_url('allokey')
    assert result == 'https://api.telegram.org/botallokey/'


def test_get_method_url():
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
    result = urls.get_method_url('https://api.telegram.org/', 'none')
    assert result is None
